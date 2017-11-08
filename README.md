# EC601HWopencv
Opencv exercises

Exercise 1:

The CV::MAT contains the columns and rows, when it create or read a image, the program read the image from the matrix format.

Exercise 2:

1.	After implement the python code, ten images are outputted. At the beginning, the original Lenna picture is shown. And for the RGB, YCbCr, HSV model, the images represent the images in each channel with the name of the channel type.

2.	The output of the values of the pixel at (20,25) of different channels is shown below.
R: 122 G: 106 B: 225, Range:0-255
Y: 151 Cr: 181 Cb: 103, Range: Y:0-255, Cr and Cb: 16-255
H: 4 S: 135 V: 225, Range: H:0-360, S and V:0-100.

Exercise 3:

After implement the python code, the results show different noise values outputs in Gaussian case and salt-and-pepper case with the kernel size from 3x3 to 5x5 to 7x7.
In this exercise, I also use the Lenna picture. For the Gaussian case, the sigma value has more effects to the image. For the salt-pepper noise case, the pa value has effect on the black pixels, the pb value has effect on the white pixels.

Exercise 4:

1.  From the result images, it shows that the adaptive threshold image gives the best results.

2.  Near the threshold pixel value, the perfromance of the image doesn't present well. It can not distinguishi the subtle changes.

3.  The adaptive threshold is useful when there are the lightness of the image is quite different in different area of the image

In-class Exercises: Template matching.

I put the specific codes in the template python file, after running the program, the result is almost the same as the TA shown in clase. The location of the template image in the source image is [240,160] 
