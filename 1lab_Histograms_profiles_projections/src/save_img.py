import cv2 as cv

img_data_folder = "C:/denFiles/git/technical-vision/2lab/images/"

img = cv.imread(img_data_folder + "winter.jpg", cv.IMREAD_GRAYSCALE)

# scale_percent = 50
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# new_dim = (width, height)
#
# resized_img = cv.resize(img, new_dim, interpolation=cv.INTER_AREA)

cv.imwrite(img_data_folder + "winter_gray.jpg", img)