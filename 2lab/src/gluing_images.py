import cv2 as cv
import numpy as np

img_path = "C:/denFiles/git/technical-vision/2lab/images/"
img_top = cv.imread(img_path + "rowan_top.jpg", cv.IMREAD_GRAYSCALE)
img_bot = cv.imread(img_path + "rowan_bot.jpg", cv.IMREAD_GRAYSCALE)

# Match template
template_size = 20
template = img_top[-template_size:, :]
res = cv.matchTemplate(img_bot, template, cv.TM_CCOEFF)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

full_img = np.zeros((img_top.shape[0] + img_bot.shape[0] - max_loc[1] - template_size, img_top.shape[1]), dtype=np.uint8)
full_img[:img_top.shape[0], :] = img_top
full_img[img_top.shape[0]:, :] = img_bot[max_loc[1] + template_size:, :]

cv.imshow("Glued image", full_img)
cv.waitKey(0)
cv.destroyAllWindows()
