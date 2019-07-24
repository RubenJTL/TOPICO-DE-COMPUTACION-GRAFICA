import numpy as np
import cv2
from matplotlib import pyplot as plt
from numpy import linalg
from numba import jit , cuda
from numba import njit



height_img=5
width_img=10

height_tem=3
width_tem=3

def normalizar(X,xmin,xmax):
    return ((X-xmin)*255)/(xmax-xmin)

@jit('void(uint8[:,:,:],uint8[:,:],float64[:,:])')
def rectangulo(img,template,imgD):
    count=0
    cantidad=80
    mean=20
    for i in range(len(imgD)):
        for j in range(len(imgD[0])):
            if(imgD[i][j]==0 and count<cantidad):
                for x_i in range(j+(-1)*len(template[0])/2,j+len(template[0])/2):
                    img[i+(-1)*len(template)/2,x_i]=(0,255,0)
                    img[i+len(template)/2,x_i]=(0,255,0)
                for y_i in range(i+(-1)*len(template)/2,i+len(template)/2):
                    img[y_i,j+(-1)*len(template[0])/2]=(0,255,0)
                    img[y_i,j+len(template[0])/2]=(0,255,0)
                count=count+1
    for i in range(len(imgD)):
        for j in range(len(imgD[0])):
            if(imgD[i][j]<mean and count<cantidad):
                for x_i in range(j+(-1)*len(template[0])/2,j+len(template[0])/2):
                    img[i+(-1)*len(template)/2,x_i]=(0,255,0)
                    img[i+len(template)/2,x_i]=(0,255,0)
                for y_i in range(i+(-1)*len(template)/2,i+len(template)/2):
                    img[y_i,j+(-1)*len(template[0])/2]=(0,255,0)
                    img[y_i,j+len(template[0])/2]=(0,255,0)
                count=count+1
                #cv2.rectangle(imgD,(i+(-1)*len(template)/2,j+(-1)*len(template[0])/2),(i+(-1)*len(template)/2,j+(-1)*len(template[0])/2),(0,255,0),3)
                #for k in range((-1)*len(template)/2,len(template)/2):
                #    for m in range((-1)*len(template[0])/2,len(template[0])/2):
                #        if(i+k>=0 and j+m>=0 and i+k<len(imgD) and j+m<len(imgD[0])):
                #            img[i+k,j+m]+=50
                            #print(i+k,j+m)

@jit('void(uint8[:,:],uint8[:,:],float64[:,:])')
def template_matching(img,template,imgD):
    for y_img in range(len(img)):
        for x_img in range(len(img[0])):
            sum=0
            ypri=len(template)/2
            xpri=len(template[0])/2
            for y_tem in range((-1)*ypri,ypri):
                for x_tem in range((-1)*xpri,xpri):
                    if(y_img+y_tem<0 or x_img+x_tem<0 and y_img+y_tem>=len(img) and x_img+x_tem>=len(img[0])):
                        imgD[y_img][x_img]+=pow(template[ypri+y_tem][xpri+x_tem],2)
                    elif(y_img+y_tem>=0 and x_img+x_tem>=0 and y_img+y_tem<len(img) and x_img+x_tem<len(img[0])):
                        #print(y_img+y_tem,x_img+x_tem)
                    #if(y_img+y_tem>0 and y_img+y_tem<height_img and x_img+x_tem>0 and x_img+x_tem<width_img ):
                        imgD[y_img][x_img]+=pow(template[ypri+y_tem][xpri+x_tem]-img[y_img+y_tem][x_img+x_tem],2)

            #imgD[y_img][x_img]=sum
matriz=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,0,1,0,1,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,0,1,0,0,0,0],
]


matrizT=[
    [0,0,0],
    [0,1,0],
    [0,0,0],
]

#print(matrizT[0][2])
template=np.array(matrizT)


img=np.array(matriz)
#print(type(template))
#img = cv2.imread("goku.jpg",0)
#img2 = cv2.imread("goku.jpg")
#template = cv2.imread("ojogoku.jpg",0)

img = cv2.imread("mario_img.jpg",0)
img2 = cv2.imread("mario_img.jpg")
template = cv2.imread("mario_img_template.jpg",0)


if img.size == 0:
    sys.exit("Error: the image has not been correctly loaded.")

#img = np.random.randint(5, size=(100, 100))
#template = np.random.randint(5, size=(3, 3))
imgD = np.zeros((len(img),len(img[0])), dtype=float)
imgD2 = np.copy(img)
#print(img)
#print(template)
#print(imgD)
imgD=np.array(imgD)
template_matching(img,template,imgD)
#print(imgD)
xmin=np.amin(imgD)
xmax=np.amax(imgD)

#print(np.amin(imgD) )
for i in range(len(imgD)):
    for j in range(len(imgD[0])):
        #if round(normalizar(imgD[i][j],xmin,xmax))<np.mean(imgD):
        imgD[i][j]=round(normalizar(imgD[i][j],xmin,xmax))
        #else:
            #imgD[i][j]=255
mean=np.mean(imgD)
print(int(mean))
print(img2)
for i in range(len(imgD)):
    for j in range(len(imgD[0])):
       imgD2[i][j]=int(imgD[i][j])
#print(imgD)

rectangulo(img2,template,imgD)
cv2.imshow('imag2',imgD2)
cv2.imshow('image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
