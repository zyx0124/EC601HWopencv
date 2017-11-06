import cv2
import numpy as np

def Add_gaussian_Noise(src,mean,sigma):
    noiseArr = src.copy()
    cv2.randn(noiseArr,mean,sigma)
    cv2.add(src,noiseArr,src)
    
    return noiseArr;

def Add_salt_pepper_Noise(src,pa,pb):
    amount1 = (int)(src.size * pa)
    amount2 = (int)(src.size * pb)
    
    for counter in range (0,amount1):
        src[(int)(np.random.uniform(0,src.shape[0]))][(int)(np.random.uniform(0,src.shape[1]))] = 0

    for counter in range (0,amount2):
        src[(int)(np.random.uniform(0,src.shape[0]))][(int)(np.random.uniform(0,src.shape[1]))] = 255

image = cv2.imread('Test_images/Lenna.png')

cv2.imwrite('Original'+".jpg",image)

kernelv =[3,5,7]

meanv = [0,5,10,20]
sigmav = [0,20,50,100]
pav = [0.01,0.03,0.05,0.4]
pbv = [0.01,0.03,0.05,0.4]
for kernel in kernelv:
		for mean in meanv:
			for sigma in sigmav:
				noise_img = image.copy() 
				Add_gaussian_Noise(noise_img, mean, sigma)
				cv2.imwrite("GaussNoise"+"mean"+str(mean)+"sigma"+str(sigma)+".jpg",noise_img)
				noise_dst = noise_img.copy()
				cv2.blur(noise_dst, (kernel,kernel))
				cv2.imwrite("BoxFilter"+"mean"+str(mean)+"sigma"+str(sigma)+"kernel"+str(kernel)+".jpg",noise_dst)
				noise_dst1 = noise_img.copy()
				cv2.GaussianBlur(noise_dst1, (kernel,kernel), 1.5)
				cv2.imwrite("GaussFilter"+"mean"+str(mean)+"sigma"+str(sigma)+"kernel"+str(kernel)+".jpg",noise_dst1)
				noise_dst2 = noise_img.copy()
				cv2.medianBlur(noise_dst2, kernel)
				cv2.imwrite("MedianFilter"+"mean"+str(mean)+"sigma"+str(sigma)+"kernel"+str(kernel)+".jpg",noise_dst2)
				
		for pa in pav:
			for pb in pbv:
				noise_img2 = image.copy()
				Add_salt_pepper_Noise(noise_img2, pa, pb); 
				cv2.imwrite("S&PNoise"+"pa"+str(pa)+"pb"+str(pb)+".jpg",noise_img2)
				noise_dst3 = noise_img2.copy()
				cv2.blur(noise_dst3, (kernel,kernel))
				cv2.imwrite("S&P_BoxFilter"+"pa"+str(pa)+"pb"+str(pb)+"kernel"+str(kernel)+".jpg",noise_dst3)
				noise_dst4 = noise_img2.copy()
				cv2.GaussianBlur(noise_dst4, (kernel,kernel), 1.5)
				cv2.imwrite("S&P_GaussFilter"+"pa"+str(pa)+"pb"+str(pb)+"kernel"+str(kernel)+".jpg",noise_dst4)				
				noise_dst5 = noise_img2.copy()
				cv2.medianBlur(noise_dst5, kernel)
				cv2.imwrite("S&P_MedianFilter"+"pa"+str(pa)+"pb"+str(pb)+"kernel"+str(kernel)+".jpg",noise_dst5)	
cv2.waitKey(0)
