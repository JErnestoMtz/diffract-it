# diffract-it

`diffract-it` is an open source computational optics simulation program. The main objective of `diffract-it` is to make a capable optics simulation program  as user friendly as possible, including a graphical user interface `GUI` that allows people with zero coding experience to use it.


## What can it do?

Diffract-it can calculate and plot the **diffraction pattern for an arbitrary shaped apertures**, as well as the propagation path.

### Examples:
**Diffraction of a square aperture**

![alt text](https://github.com/JErnestoMtz/diffract-it/blob/main/images/example1.png)

**Double slid diffraction and propagation**

![alt text](https://github.com/JErnestoMtz/diffract-it/blob/main/images/Captura.PNG)

**Hex grid diffraction at different distances**

![alt text](https://github.com/JErnestoMtz/diffract-it/blob/main/images/hexgrid.PNG)

**Multi intensity diffraction**

![alt text](https://github.com/JErnestoMtz/diffract-it/blob/main/images/fullimag.PNG)

**Triangular aperture**
Fresnel, and Fraunhofer diffraction


![alt text](https://github.com/JErnestoMtz/diffract-it/blob/main/images/example_triangles.PNG)

## Easy to use

There are two main ways to run `diffract-it`: 

**Option 1: Cloning this repository and running `main.py`.**

* Required packages: `numpy`,`matplotlib`, `Pillow`, `opencv-python` 

Step by step instructions:

1. Clone or download the repository . Make sure the folders `data` and `_pycache_` are downloaded among with `diffractionfun.py`, `imgprocessing.py` and `main.py`.

![alt text](https://github.com/JErnestoMtz/diffract-it/blob/main/images/archivosmanual.PNG)

2. Run the file `main.py` in the text editor of your choice. Make sure the folders and files are in the right place. You will get the following window.

![alt text](https://github.com/JErnestoMtz/diffract-it/blob/main/images/ventana.PNG)

3. Among the options, select the **upload image** option, which can be either `JPG`, `PNG` or `JPEG` and upload your image.
4. Then click **Process image**. This wil convert the image to a scale of black and white. Remember, black spots = apertures, while bright spots mean the opposite. A preview of the image will be shown. If the image size is not squared, the program will auto-crop it, taking as the smallest dimension as the new size. 
5. Type in the wavelength to be used, the *real* size of the new length of the image in terms of the wavelength, `d`, and finally, the total distance at which the beam will propagate.

![alt text](https://github.com/JErnestoMtz/diffract-it/blob/main/images/opciones.PNG)

6. Select "Calculate diffraction pattern". 



**Option 2: Executable file, this option doesn’t require any dependencies.** 

* To use this option you need to clone or download the branch `executable` and run `diff.èxe`

Step by step instructions:

1. Go to the branch `executable`, and clone or download the repository . 
2. Make sure the PNG images `1`, `b1`, `b2`, `b3` and the icon file `dd` are in the same folder, as shown in the following image.

![alt text](https://github.com/JErnestoMtz/diffract-it/blob/main/images/archivos.PNG)

3. Execute the `diff.exe` executable. You will get the following window.

![alt text](https://github.com/JErnestoMtz/diffract-it/blob/main/images/ventana.PNG)

3. Among the options, select the **upload image** option, which can be either `JPG`, `PNG` or `JPEG` and upload your image.
4. Then click **Process image**. This wil convert the image to a scale of black and white. Remember, black spots = apertures, while bright spots mean the opposite. A preview of the image will be shown. If the image size is not squared, the program will auto-crop it, taking as the smallest dimension as the new size. 
5. Type in the wavelength to be used, the *real* size of the new length of the image in terms of the wavelength, `d`, and finally, the total distance at which the beam will propagate.

![alt text](https://github.com/JErnestoMtz/diffract-it/blob/main/images/opciones.PNG)

7. Select "Calculate diffraction pattern". 

## Further development.

DIffract-it is an ongoing project, with many more features being developed. 

1. Improving GUI 
2. Direct Fresnel and Fraunhofer diffraction calculations
3. Polychromatic diffraction
4. Angular spectrum method as an alternative to Fourier wave propagation.
5. Selectable resolution
6. Addition of lenses and other optic components
7. Documentation

######  Any contributions is welcome
