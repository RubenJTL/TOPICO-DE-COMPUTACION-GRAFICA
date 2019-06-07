import numpy as np
import cv2
from matplotlib import pyplot as plt
from numpy import linalg


def TransformacionBilineal(A,Bx,By,ImgO,ImgR,height1,width1,height2,width2):
    Solutions2=np.linalg.solve(A,By)
    Solutions1=np.linalg.solve(A,Bx)#cramer(A,B)
    for i in range(height1,height2):
        for j in range(width1,width2):
            vector=[j,i,i*j,1]
            vector=np.array(vector)
            vector=vector.astype(np.float)
            Solutions1=np.array(Solutions1)
            x=int(round(sum(vector*Solutions1)))
            Solutions2=np.array(Solutions2)
            y=int(round(sum(vector*Solutions2)))
            ImgR[y,x]=ImgO[i,j]
    return

def mostrar(img):
    cv2.imshow("My first OpenCV window", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return


img = cv2.imread("goku.jpg")

if img.size == 0:
    sys.exit("Error: the image has not been correctly loaded.")
#hist,bins = np.histogram(img.ravel(),256,[0,256])
print(img.size)
height, width, channels = img.shape
print("width",width,width/2 )
print("height",height, height/2)

RGB=[0,0,0]
type(RGB)
img2=img.copy()
for i in range(height):
    for j in range(width):
        img2[i,j]=RGB


"""X=[(width//4)*0,(width//4)*1,(width//4)*2,(width//4)*3,(width//4)*4]
Y=[(height//4)*0,(height//4)*1,(height//4)*2,(height//4)*3,(height//4)*4]

Xr=[(width//4)*0,(width//4)*1,(width//4)*2,(width//4)*3,(width//4)*4]
Xr=[[(width//4)*0,(width//4)*1,(width//4)*1,(width//4)*0],
    [(width//4)*1,(width//4)*2,(width//4)*2,(width//4)*1],
    [(width//4)*2,(width//4)*3,(width//4)*3,(width//4)*2],
    [(width//4)*3,(width//4)*4,(width//4)*4,(width//4)*3]]

Yr=[[(height//4)*0,(height//4)*0,(height//4)*1,(height//4)*1],
    [(height//4)*1,(height//4)*1,(height//4)*2,(height//4)*2],
    [(height//4)*2,(height//4)*2,(height//4)*3,(height//4)*3],
    [(height//4)*3,(height//4)*3,(height//4)*4,(height//4)*4]]
"""
X=[(width//2)*0,(width//2)*1,(width//2)*2]
Y=[(height//2)*0,(height//2)*1,(height//2)*2]

XR=500
YR=225

Xr=[[(width//2)*0,(width//2)*1,XR,(width//2)*0],
    [(width//2)*1,(width//2)*2,(width//2)*2,XR],
    [(width//2)*0,XR,(width//2)*1,(width//2)*0],
    [XR,(width//2)*2,(width//2)*2,(width//2)*1]]
Yr=[[(height//2)*0,(height//2)*0,YR,(height//2)*1],
    [(height//2)*0,(height//2)*0,(height//2)*1,YR],
    [(height//2)*1,YR,(height//2)*2,(height//2)*2],
    [YR,(height//2)*1,(height//2)*2,(height//2)*2]]
#while(True):
##    for i in range(height):
##        for j in range(width):
##            img2[i,j]=RGB

##    x=int(input("x"))
##    y=int(input("y"))

for i in range(2):
    for j in range(2):
        A=[
        [X[j],Y[i],Y[i]*X[j],1],
        [X[j+1],Y[i],Y[i]*X[j+1],1],
        [X[j+1],Y[i+1],Y[i+1]*X[j+1],1],
        [X[j],Y[i+1],Y[i+1]*X[j],1],
        ]

        Bx=[Xr[j+(i*2)][0],Xr[j+(i*2)][1],Xr[j+(i*2)][2],Xr[j+(i*2)][3]]
        By=[Yr[j+(i*2)][0],Yr[j+(i*2)][1],Yr[j+(i*2)][2],Yr[j+(i*2)][3]]

        A=np.array(A)
        Bx=np.array(Bx)
        By=np.array(By)
        TransformacionBilineal(A,Bx,By,img,img2,Y[i],X[j],Y[i+1],X[j+1])
            #mostrar(img2)

mostrar(img2)

    #break

#mostrar(img)
