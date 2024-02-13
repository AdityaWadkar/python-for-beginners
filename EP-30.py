# Ep-30 News APP

"""
requirements
requests :- pip install requests
PIL :- pip install pillow

API key :- https://newsapi.org/

"""
import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image

root = Tk()
API_KEY = 'Your_API_KEY'

def load_news_app():
    #fetches the news data, loads the GUI, and displays the first news item using load_news_item
    data = requests.get(f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}').json()
    load_gui(data)
    load_news_item(data, 0)

def load_gui(data):
    #Configures the basic properties of the Tkinter window (root).
    root.geometry('350x600')
    root.resizable(0, 0)
    root.title('My NEWS APP')
    root.configure(background='black')

def clear():
    # Destroys all the widgets (children) inside the Tkinter window. 
    # This is used to clear the existing content before loading a new news item.
    for i in root.pack_slaves():
        i.destroy()

def load_news_item(data, index):
    #clear the existing content
    clear()
    # fetch the image from the news data
    try:
        img_url = data['articles'][index]['urlToImage']
        raw_data = urlopen(img_url).read()
        im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
        photo = ImageTk.PhotoImage(im)
    # show blank image
    except:
        img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
        raw_data = urlopen(img_url).read()
        im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
        photo = ImageTk.PhotoImage(im)

    # creates a reference to the image
    label = Label(root, image=photo)
    label.photo = photo  # Keep a reference to the image
    label.pack()

    #Labels for the news title and description
    heading = Label(root, text=data['articles'][index]['title'], bg='black', fg='white', wraplength=350, justify='center')
    heading.pack(pady=(10, 20))
    heading.config(font=('verdana', 15))

    details = Label(root, text=data['articles'][index]['description'], bg='black', fg='white', wraplength=350,
                    justify='center')
    details.pack(pady=(2, 20))
    details.config(font=('verdana', 12))

    frame = Frame(root, bg='black')
    frame.pack(expand=True, fill=BOTH)

    #Buttons for navigation 
    if index != 0:
        prev = Button(frame, text='Prev', width=16, height=3, command=lambda: load_news_item(data, index - 1))
        prev.pack(side=LEFT)

    read = Button(frame, text='Read More', width=16, height=3,
                  command=lambda: open_link(data['articles'][index]['url']))
    read.pack(side=LEFT)

    if index != len(data['articles']) - 1:
        next = Button(frame, text='Next', width=16, height=3, command=lambda: load_news_item(data, index + 1))
        next.pack(side=LEFT)

def open_link(url):
    # open the news article in a web browser 
    webbrowser.open(url)

#start the application
load_news_app()
#running this application in loop
root.mainloop()
