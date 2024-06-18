import cv2

img = cv2.imread("food.jpg", cv2.IMREAD_UNCHANGED)
# cv2.imshow("Mandhi", img)

scale = 150
new_width = int(img.shape[0] * scale/100)
new_height = int(img.shape[1] * scale/100)

output = cv2.resize(img, (new_width,new_height))
cv2.imwrite('resized-food.jpg', output)
cv2.waitKey(0)
cv2.destroyAllWindows()