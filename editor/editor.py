import numpy as np
import cv2
from matplotlib import pyplot as plt


def mostrar(img):
    cv2.imshow("My first OpenCV window", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

def modificar(img,a,b):
    newimg=(a*img)+b
    return newimg

def capas(img):
    b,g,r = cv2.split(img)
    img= cv2.merge((b,g,r))
    #mostrar(r)
    return (b,g,r)

def blending(img):
    return

#img = cv2.imread("goku.jpg")
img = cv2.imread("goku.jpg")

if img.size == 0:
    sys.exit("Error: the image has not been correctly loaded.")
hist,bins = np.histogram(img.ravel(),256,[0,256])
print(img)

print(hist)
b=0
a=1
blue,green,red=capas(img)
blue=modificar(blue,a,b)
green=modificar(green,a,b)
red=modificar(red,a,b)
img=cv2.merge((blue,green,red))
mostrar(blue)

b=10
a=1
blue,green,red=capas(img)
blue=modificar(blue,a,b)
green=modificar(green,a,b)
red=modificar(red,a,b)
img2=cv2.merge((blue,green,red))

b=0
a=3
blue,green,red=capas(img)
blue=modificar(blue,a,b)
green=modificar(green,a,b)
red=modificar(red,a,b)
img3=cv2.merge((blue,green,red))

print (img.shape)
print (img.size)
print (img.dtype)
#print(hist)
#plt.hist(img.ravel(),256,[0,256]); plt.show()
#plt.hist(img2.ravel(),256,[0,256]); plt.show()
#plt.hist(img3.ravel(),256,[0,256]); plt.show()
#plt.hist(img.ravel(),256,[0,256]); plt.show()
mostrar(img)
mostrar(img2)
mostrar(img3)


#capas(img)
# We display our image and ask the program to wait until a key is pressed
#mostrar(img)
