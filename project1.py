#import images from PIL
from PIL import Image

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

#need to get the image width and height
print im1.size
width, height = im1.size
    
redPixelList = []
greenPixelList = []
bluePixelList = []

#create for loop 
# for x in range(pictureWidth):
#     for y in range(pictureHeight):
#         for theImage in listImages:
            
#             imgRed, imgGreen, imgBlue = theImage.getpixel((x,y))
            
#             redPixelList.append(imgRed)
#             greenPixelList.append(imgGreen)
#             bluePixelList.append(imgBlue)
            
#create new pixel for the median of RGB values of each of the 9 images.