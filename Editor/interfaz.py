#try:
    # for Python2
#    import Tkinter as tk   ## notice capitalized T in Tkinter
#except ImportError:
    # for Python3
#    import tkinter as tk   ## notice lowercase 't' in tkinter here
from tkinter import *
import numpy as np
import cv2
from PIL import Image
from PIL import ImageTk
#import Tkinter as tk
ventana=Tk()
img = cv2.imread("goku.jpg")
ventana.title("Primer ventana")
#ventana.geometry('650x350'0)
ventana.configure(background='white')

#ventana.resizable(0,0)

consta=DoubleVar()
constb=DoubleVar()

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


def obtenerdatos(img):
    a=consta.get()
    b=constb.get()
    print(a+b)
    blue,green,red=capas(img)
    blue=modificar(blue,a,b)
    green=modificar(green,a,b)
    red=modificar(red,a,b)
    img = cv2.merge((red,green,blue))

    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im)
    Label(ventana, image=imgtk).pack(side="right")
    return




frame=Frame()
frame.pack(side="left",anchor="n",fill="both",expand="False")
#frame.config(bg="red")
frame.config(width="650",height="350")
frame.config(relief="groove")
frame.config(cursor="hand2")

#-------------------LABELS
labelConsta= Label(frame,text="Constante a")
labelConsta.grid(row=0,column=0)
labelConstb = Label(frame,text="Constante b")
labelConstb.grid(row=1,column=0)


#-------------------Cuadros de Texto
consta=DoubleVar()
constb=DoubleVar()

cuadroTextoConsta=Entry(frame,textvariable=consta)
cuadroTextoConsta.grid(row=0,column=1)
cuadroTextoConstb=Entry(frame,textvariable=constb)
cuadroTextoConstb.grid(row=1,column=1)

#-------------------Buttons

botonConsta=Button(frame,text="insert", command=lambda:obtenerdatos(img))
botonConsta.grid(row=2,column=0)

print(consta)
print(constb)

b,g,r = cv2.split(img)
img = cv2.merge((r,g,b))
im = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(image=im)
Label(ventana, image=imgtk).pack(side="right")
ventana.mainloop()
