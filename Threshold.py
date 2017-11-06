import cv2

image = cv2.imread('Test_images/Lenna.png')

gray= cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imshow("Input Image",image)
cv2.imwrite("Input Image"+".jpg",image)

threshold_type=2
threshold_value=128

ret,dst=cv2.threshold(gray,threshold_value,255,threshold_type)
cv2.imshow("Thresholded Image",dst)
cv2.imwrite("Thresholded Image"+".jpg",dst)

current_threshold=128
max_threshold=255

ret,thresholded=cv2.threshold(gray,current_threshold,max_threshold,cv2.THRESH_BINARY)
cv2.imshow("Binary threshold",thresholded)
cv2.imwrite("Binary threshold"+".jpg",thresholded)

threshold1=27
threshold2=125

ret,binary_image1=cv2.threshold(gray,threshold1,max_threshold,cv2.THRESH_BINARY)
ret,binary_image2=cv2.threshold(gray,threshold2,max_threshold,cv2.THRESH_BINARY_INV)

semi_thresholded_image=cv2.bitwise_and(binary_image1,binary_image2)
cv2.imshow("Semi Thresholding",semi_thresholded_image)
cv2.imwrite("Semi Thresholding"+".jpg",semi_thresholded_image)

adaptive_thresh=cv2.adaptiveThreshold(gray,255.0,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,101,10)
cv2.imshow("Adaptive Thresholding",adaptive_thresh)
cv2.imwrite("Adaptive Thresholding"+".jpg",adaptive_thresh)

cv2.waitKey(0)



