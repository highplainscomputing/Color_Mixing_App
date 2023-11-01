# Import required modules
import cv2
import numpy as np

# Create a white canvas
def createCanvas(color):
    # Use NumPy to create an array
    # full of ones
    # We will have the canvas of shape
    # 640x640
    # Datatype used is uint8 which is
    # unsigned 8-bit integer
    canvas = np.ones((640,640,3),dtype=np.uint8)
    # Next, multiply the canvas
    # with the specified color
    # This fills the canvas with the 
    # specified color
    # Again, we will use uint8
    canvas = np.uint8(canvas * color)
    # Return the canvas
    return canvas

# Display an image
def displayImage(image,windowName):
    # Use cv2.imshow function
    cv2.imshow(windowName,image)

# Mouse callback function
def mouseCallbackFunction(event, x, y, flags, param):
    global color1
    # Check if left mouse button was pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        # Set the color to color at the location
        color1 = findColor(colorPalette,x,y)

# Find the color for an image at the given location
def findColor(img,x,y):
    return img[y,x]

# Mix two colors
def mixColors(color1, color2):
    # Return new color mix
    # You can use any other method
    # of your own choice
    # Swap the channels of colors
    # in order to incorporate the
    # BGR <--> RGB conversion
    color1 = color1[::-1]
    color2 = color2[::-1]
    
    return np.uint8((np.sin(color1)+np.cos(color2))*255)

# Load the color palette
colorPalette = cv2.imread("palette.jpg")
# Right now, the color palette
# is way too big, so let's resize it down
colorPalette = cv2.resize(colorPalette, (640,640))

# Create canvas
# Use the createCanvas function
# you have written above
# Let's create a white canvas
# White color in BGR is 255,255,255
# We are using BGR channels because
# OpenCV uses the same
canvas = createCanvas([255,255,255])

# Attach mouse callback function
# to the two display windows
cv2.namedWindow("Canvas")
cv2.namedWindow("Color Palete")
cv2.setMouseCallback("Color Palete",mouseCallbackFunction)

# Initialize global variable
color1 = None

while 1:
    # First find color from color palette
    displayImage(canvas,"Canvas")
    displayImage(colorPalette,"Color Palete")
    if color1 is not None:
        # Find color in canvas
        color2 = findColor(canvas,10,10)
        # Mix colors
        newColor = mixColors(color1,color2)
        # Fill the new color in canvas
        canvas = createCanvas(newColor)
        # Set color1 back to default value
        color1 = None
    k = cv2.waitKey(20)
    # If Esc was pressed, quit...
    if k == 27:
        break
    # If r is pressed, reset...
    elif k == ord('r'):
        canvas = createCanvas([255,255,255])
    # If s is pressed, save...
    elif k == ord('s'):
        cv2.imwrite("ColorBlending.png",canvas)

cv2.destroyAllWindows()
