import cv2
import os
import pandas

from blur_detection import estimate_blur
from blur_detection import fix_image_size
from blur_detection import pretty_blur_map
from process import find_images

image_dir = 'rgb_data/fuckingShits/'
for i, image_path in enumerate(os.listdir(image_dir, )):
    image_path = 'rgb_data/fuckingShits/' + image_path
    # print(image_path)
    image = cv2.imread(str(image_path))

    image = fix_image_size(image)
    blur_map, score, blurry = estimate_blur(image, threshold=45)

    if(blurry is False and blur_map[50:330,399:402].sum() > 8000):
        print('Blurry')
    else:
        print(score, blurry)

# cv2.namedWindow('input', 0)
# cv2.resizeWindow('input', 500, 500)
# cv2.namedWindow('result', 0)
# cv2.resizeWindow('result', 200, 200)
# cv2.imshow('input', image)
# #            cv2.imshow('result', pretty_blur_map(blur_map))
# cv2.imshow('result', pretty_blur_map(blur_map[50:330,399:402]))

# cv2.waitKey(0) == ord('q'):
#    exit()
