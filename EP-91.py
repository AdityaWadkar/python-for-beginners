# Import the OpenCV library
#command to install opencv - pip install opencv-python
import cv2

# Specify the path to your image file
image_path = "image.jpeg"  # Replace with the actual path to your image

# Read the image from file
image = cv2.imread(image_path)

#RESIZE IMAGE  
big_image = cv2.resize(image, (518, 388))

# Check if the image was successfully loaded
if image is None:
    print(f"Error: Unable to load the image from {image_path}")
else:
    # Display the image in a window
    cv2.imshow("Hello OpenCV", image)
    
    # Display resized image in a window
    cv2.imshow("Hello OpenCV - big", big_image)

    # Wait for a key event and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
