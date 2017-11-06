import cv2
image = cv2.imread('Test_images/Lenna.png')


cv2.imwrite("Original Image"+".jpg",image)
input_planes1=cv2.split(image)
cv2.imwrite("RED"+".jpg", input_planes1[2])
cv2.imwrite("Green"+".jpg", input_planes1[1])
cv2.imwrite("Blue"+".jpg", input_planes1[0])

ycrcb_image=cv2.cvtColor(image,cv2.COLOR_BGR2YCrCb)
input_planes2=cv2.split(ycrcb_image)
cv2.imwrite("Y"+".jpg", input_planes2[0])
cv2.imwrite("Cb"+".jpg", input_planes2[1])
cv2.imwrite("Cr"+".jpg", input_planes2[2])

hsv_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
input_planes3=cv2.split(hsv_image)
cv2.imwrite("Hue"+".jpg", input_planes3[0])
cv2.imwrite("Saturation"+".jpg", input_planes3[1])
cv2.imwrite("Value"+".jpg", input_planes3[2])

a=image[20][25]
print('R:',a[1],'G:',a[0],'B:',a[2])

b=ycrcb_image[20][25]
print('Y:',b[0],'Cr:',b[1],'Cb:',b[2])

c=hsv_image[20][25]
print('H:',c[0],'S:',c[1],'V:',c[2])

cv2.waitKey(0)



