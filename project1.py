#import images from PIL
from PIL import Image

def medianOdd(myList):
    # Store list length in the variable listLength
    listLength = len(myList)
    # Sort the list
    sortedValues = sorted(myList)
    # Location of middle value. Subtract one because of zero index
    middleIndex = ((listLength + 1)/2) - 1
    # Return the object located at that index
    return sortedValues[middleIndex]

im1 = Image.open("/home/ubuntu/workspace/Project2/Images/1.png")
im2 = Image.open("/home/ubuntu/workspace/Project2/Images/2.png")
im3 = Image.open("/home/ubuntu/workspace/Project2/Images/3.png")
im4 = Image.open("/home/ubuntu/workspace/Project2/Images/4.png")
im5 = Image.open("/home/ubuntu/workspace/Project2/Images/5.png")
im6 = Image.open("/home/ubuntu/workspace/Project2/Images/6.png")
im7 = Image.open("/home/ubuntu/workspace/Project2/Images/7.png")
im8 = Image.open("/home/ubuntu/workspace/Project2/Images/8.png")
im9 = Image.open("/home/ubuntu/workspace/Project2/Images/9.png")

#list of pillow image objects
listImages = [im1, im2, im3, im4, im5, im6, im7, im8, im9]

for i in range(9):
    listImages.append(Image.open("/home/ubuntu/workspace/Project2/Images/"+str(i + 1)+".png"));


#need to get the image width and height
print im1.size
width, height = im1.size
    
redPixelList = [];
greenPixelList = [];
bluePixelList = [];

#create new blank image
newImage = Image.new("RGB", (width, height), "white")

#create for loop 
for x in range(width):
    for y in range(height):
        for theImage in listImages:
            
            imgRed, imgGreen, imgBlue = theImage.getpixel((x,y))
            
            redPixelList.append(imgRed)
            greenPixelList.append(imgGreen)
            bluePixelList.append(imgBlue)
        
#create new pixel for the median of RGB values of each of the 9 images.            
        medianRed = medianOdd(redPixelList)
        medianGreen = medianOdd(greenPixelList)
        medianBlue = medianOdd(bluePixelList)
        
        newImage.putpixel((x,y),(medianRed, medianGreen, medianBlue))
        
        redPixelList = [];
        greenPixelList = [];
        bluePixelList = [];

newImage.save('finalImage.png')


