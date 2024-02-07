import cv2

img = cv2.imread('images/Nil.jpg')

# Some information about image
print("Image Properties")
print("- Number of Pixels: " + str(img.size))
print("- Shape/Dimensions: " + str(img.shape))
