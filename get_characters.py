import cv2
# https://www.pyimagesearch.com/2015/04/20/sorting-contours-using-python-and-opencv/
def sort_contours(cnts,reverse = False):
    i = 0		#left to right
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))
    return cnts

def cut_image_to_2_images(image):
	h, w = image.shape
	bot = int(h*0.55)
	top = int(h*0.45)
	image_top = image[0:bot, 0:w]
	image_bottom = image[top:h, 0:w]
	return image_top, image_bottom

def get_characters_from_image(image):

	#get contour
	cont  = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

	#characters
	crop_characters = []

	digit_w, digit_h = 30, 60

	for c in sort_contours(cont):
	    (x, y, w, h) = cv2.boundingRect(c)
	    ratio = h/w
	    if 1<=ratio<=5: # Only select contour with defined ratio
	        if h/image.shape[0]>=0.3: # Select contour which has the height larger than 50% of the plate
	            # print(111111111111111111111111111111111111111111111111111111111111111111)
	            # Draw bounding box arroung digit number
	            # cv2.rectangle(test_roi, (x, y), (x + w, y + h), (0, 255,0), 2)

	            # Sperate number and gibe prediction
	            curr_num = image[y:y+h,x:x+w]
	            curr_num = cv2.resize(curr_num, dsize=(digit_w, digit_h))
	            _, curr_num = cv2.threshold(curr_num, 220, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
	            # cv2.imshow('2', curr_num) 
	            # cv2.waitKey()
	            crop_characters.append(curr_num)

	return crop_characters

def get_characters(image):
	image_top, image_bottom = cut_image_to_2_images(image)
	charater_top = get_characters_from_image(image_top)
	charater_bot = get_characters_from_image(image_bottom)

	return charater_top, charater_bot


# cont  = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
# # cv2.imshow('1',cont[0])
# # cv2.waitKey()
# # creat a copy version "test_roi" of plat_image to draw bounding box
# test_roi = img.copy()

# # Initialize a list which will be used to append charater image
# crop_characters = []

# # define standard width and height of character
# digit_w, digit_h = 30, 60

# for c in sort_contours(cont):
#     (x, y, w, h) = cv2.boundingRect(c)
#     ratio = h/w
#     if 1<=ratio<=5: # Only select contour with defined ratio
#         if h/img.shape[0]>=0.3: # Select contour which has the height larger than 50% of the plate
#             # print(111111111111111111111111111111111111111111111111111111111111111111)
#             # Draw bounding box arroung digit number
#             cv2.rectangle(test_roi, (x, y), (x + w, y + h), (0, 255,0), 2)

#             # Sperate number and gibe prediction
#             curr_num = img[y:y+h,x:x+w]
#             curr_num = cv2.resize(curr_num, dsize=(digit_w, digit_h))
#             _, curr_num = cv2.threshold(curr_num, 220, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#             # print(curr_num)
#             cv2.imshow('2', curr_num) 
#             cv2.waitKey(0)
#             crop_characters.append(curr_num)


# cv2.imshow('1', img)
# cv2.waitKey()


