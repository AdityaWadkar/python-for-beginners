# Day-60: CrypticCanvas

"""

Stegno
Stegano is a Python library for steganography, which is the practice of 
concealing messages or data within other non-secret data, such as images 
or audio files.

install package stegano using folling command :
pip install stegano

write correct file name with extension
and if it still doesn't works give entire path of file and then try

"""
# code to hide data in image ....

from stegano import lsb
secret = lsb.hide("img.png","message")
secret.save("img1.png")

# code to extract data from text
from stegano import lsb
secret_data=lsb.reveal("YOUR Image name.extension")
print(secret_data)
