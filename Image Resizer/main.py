import cv2

src=cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)
#cv2.imshow('I am a cat', src)

#percent by which image needs to be resized
scale_percent=30

#calculate 20 percent of original dimensions
new_width=int(src.shape[1] * scale_percent / 100)
new_height=int(src.shape[0] * scale_percent / 100)

#resize image
output=cv2.resize(src,(new_width,new_height))

#imwrite creates and stores output image in new_image.png file
cv2.imwrite('new_image.jpg',output)

#holds image until key is pressed
cv2.waitKey(0)
