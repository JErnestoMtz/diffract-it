import numpy as np
import math as m
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import cv2
import re
import img_processing


def diffr(ima, nd, wevelenght, nlz): 
    nd = int(re.sub('[^0-9]','', nd))
    wevelenght = int(re.sub('[^0-9]','', wevelenght))
    nlz  = int(re.sub('[^0-9]','', nlz))

    n = 2**9



    f = img_processing.img_to_numpynorm(ima,n) # transform image into nupy array


    dlambda = wevelenght*10**(-9)
    l = dlambda*nd

    vn = np.arange(-n/2,n/2)
    dx = 2*l/n
    kmax = m.pi/dx
    v = vn*dx
    x , y = np.meshgrid(v,v)
    kx , ky = np.meshgrid(kmax*2/n*vn,kmax*2/n*vn)


    k = 2*m.pi/ dlambda
    kt = np.sqrt(kx**2 + ky**2)
    
    z = nlz*dlambda
    nz= 600
    dz = z/nz
    #########################################################################

    prop = np.exp(-1j*0.5*dz*(kt**2)/k) #propagator 

    #########################################################################
    ur = np.zeros((n,nz+1), dtype=complex) # z view 
    u0 = f
    ur[:,0]= u0[:,int(n/2+1)]
    ########################################################################

    F = np.fft.fftshift(np.fft.fft2(f))
    F = F * prop
    a = np.fft.ifft2(F)
    absol = np.abs(a)
    h1 = plt.figure(2)
    plt.xticks(np.arange(0, 2**9, step=int(2**9/8)),np.arange(0, int(nd/8)*8, step= int(nd/8)))
    plt.yticks(np.arange(0, 2**9, step=int(2**9/8)),np.arange(0, int(nd/8)*8, step= int(nd/8)))
    plt.xlabel('x in terms of λ')
    plt.ylabel('y in terms of λ')
    plt.imshow(absol)
    plt.title('Initial beam profile z = 0')
    for k in range(nz):
        F = F * prop
        a = np.fft.ifft2(F)
        absol = np.abs(a)
        ur[:,k+1] = a[:,int(n/2)]

    abso = np.abs(ur)
    h2 = plt.figure(3)
    plt.yticks(np.arange(0, 2**9, step=int(2**9/8)),np.arange(0, int(nd/8)*8, step= int(nd/8)))
    plt.xticks(np.arange(0, nz, step=int(nz/10)),np.arange(0, int(nlz/10)*10, step= int(nlz/10)))
    plt.imshow(abso)
    plt.title('Beam propagation in z axis')


    h3 = plt.figure(4)
    plt.xticks(np.arange(0, 2**9, step=int(2**9/8)),np.arange(0, int(nd/8)*8, step= int(nd/8)))
    plt.yticks(np.arange(0, 2**9, step=int(2**9/8)),np.arange(0, int(nd/8)*8, step= int(nd/8)))
    plt.imshow(np.abs(a))
    plt.title('Diffracted beam profile')
    plt.show()

