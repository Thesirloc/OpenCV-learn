import cv2

img = cv2.imread('lena.jpg')

cv2.imshow('img', img)

k = cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png',img)
cv2.destroyAllWindows()