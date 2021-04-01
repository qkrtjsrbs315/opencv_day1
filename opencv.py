import cv2

img_color = cv2.imread('bli.jpg',cv2.IMREAD_COLOR)#imread로 이미지를 읽어온다

cv2.namedWindow('Show Image')
cv2.imshow("Show Image",img_color)

cv2.waitKey(0)

img_gray = cv2.cvtColor(img_color,cv2.COLOR_BGR2GRAY)


cv2.namedWindow('Show Image')
cv2.imshow("Show Image",img_gray) #윈도우 콘솔앱으로 띄우기
cv2.imwrite("hello.jpg",img_gray)#이미지 저장장
cv2.waitKey(0) #키보드입력 무한히 대기
cv2.destroyAllWindows()

