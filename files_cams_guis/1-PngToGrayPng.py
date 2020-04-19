import cv2

grayImage = cv2.imread('chapter02\IMG_0899.jpg', cv2.IMREAD_GRAYSCALE) 
cv2.imwrite('chapter02\MyPicGray.jpg', grayImage)
print(grayImage.shape)
cv2.imshow("Me", grayImage)
cv2.waitKey(0)
cv2.destroyAllWindows()