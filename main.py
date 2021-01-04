import tkinter as tk
from tkinter import filedialog
import numpy as np
import math as m
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import cv2
import re
import diffractionfun, img_processing
# -------------------- request image---------------------------


def Request_img():
    global path
    path = filedialog.askopenfilename()
    print(str(path))
# -------------------- Popup msg---------------------------
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Error")
    label = tk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
# -------------------- pre-process image---------------------------
def show():
    try:
        im1 = Image.open(str(path))
        global pre 
        pre = img_processing.preprocess(im1, width1, height1)  
        canvas1 = tk.Canvas(width=width1-20, height=height1-20, bg='#ac1908')
        canvas1.grid(row=0, columnspan=6)
        f2 = ImageTk.PhotoImage(pre)
        canvas1.create_image(x, y, image=f2)
        root.mainloop()
    except:
        popupmsg('No image selected.')



# ------------------------- Main ---------------------------
def ini():
    global root
    root = tk.Tk()
    global x, y, width1, height1

    root.title("Diffraction")

    root.iconbitmap('data/dd.ico')
    imagefile = "data//1.png"

    f1 = tk.PhotoImage(file=imagefile)
    width1 = f1.width()
    height1 = f1.height()
    x = (width1)/2.0
    y = (height1)/2.0
    canvas1 = tk.Canvas(width=width1-20, height=height1-20, bg='#ac1908')
    canvas1.grid(row=0, columnspan=6)
    canvas1.create_image(x, y, image=f1)

    b1 = tk.PhotoImage(file="data//b1.png")
    b2 = tk.PhotoImage(file="data//b2.png")
    b3 = tk.PhotoImage(file="data//b3.png")

    but = tk.Button(root, image=b2, command=Request_img)
    but.grid(row=2, column=0)

    but2 = tk.Button(root, image=b1, command=show)
    but2.grid(row=2, column=2)

    but3 = tk.Button(root, image=b3, command=lambda: diffractionfun.diffr(pre, d.get(), wevelength.get(), lz.get()))
    but3.grid(row=2, column=4)


    dlablel = tk.Label(root, text='Pattern length:')
    dlablel.grid(row=1, column=0)
    d = tk.Entry(root)
    d.insert(0, '50 λ')
    d.grid(row=1, column=1)

    wevelength_label = tk.Label(root, text='Wevelength in nm:')
    wevelength_label.grid(row=1, column=2)
    wevelength = tk.Entry(root)
    wevelength.insert(0, '633 nm')
    wevelength.grid(row=1, column=3)


    lz_label = tk.Label(root, text='Propagation distance:')
    lz_label.grid(row=1, column=4)
    lz = tk.Entry(root)
    lz.grid(row=1, column=5)
    lz.insert(0, '100 λ')

    root.mainloop()




ini()
