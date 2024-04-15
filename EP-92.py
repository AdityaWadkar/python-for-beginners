# Import the OpenCV library
import cv2

# Specify the path to your image file
image_path = "dog.png"  # Replace with the actual path to your image

# Read the image from file
image = cv2.imread(image_path)
print('Image Width is',image.shape[1])
print('Image Height is',image.shape[0])

# Check if the image was successfully loaded
if image is None:
    print(f"Error: Unable to load the image from {image_path}")
else:
    # Display the original image
    cv2.imshow("Original Image", image)

    # Image resizing
    resized_image = cv2.resize(image, (400, 300))  # Set your desired dimensions
    cv2.imshow("Resized Image", resized_image)

    width = 544
    height = 363
    # Image rotation
    rotation_matrix = cv2.getRotationMatrix2D((width // 2, height // 2), 45, 1)  # Rotate by 45 degrees
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, width))
    cv2.imshow("Rotated Image", rotated_image)

    # Image flipping
    flipped_image = cv2.flip(image, 0)  # 0 for vertical flip, 1 for horizontal flip
    cv2.imshow("Flipped Image", flipped_image)

    # Wait for a key event and then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
