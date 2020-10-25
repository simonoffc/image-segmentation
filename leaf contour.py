# -*- coding: utf-8 -*-

# Программа, которая оконтуривает зеленый листочек
"""
Статья:
https://towardsdatascience.com/object-detection-via-color-based-image-segmentation-using-python-e9b7c72f0e11
"""

import cv2
import numpy as np


def view_image(image):
    """Функция вывода изображения"""
    cv2.namedWindow('test', cv2.WINDOW_NORMAL)
    cv2.imshow('test', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def find_greatest_contour(contours):
    the_largest_area = 0
    the_largest_contour_index = -1
    i = 0
    total_contours = len(contours)
    while i < total_contours:
        area = cv2.contourArea(contours[i])
        if area > the_largest_area:
            the_largest_area = area
            the_largest_contour_index = i
        i += 1

    return the_largest_area, the_largest_contour_index


# 1. Конвертация изображения в HSV (Hue - тон, Saturation - насыщенность, Value - значение)
image = cv2.imread('./images/toliatty.png')
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
view_image(hsv_img)     # Вывод


# 2. Наложение маски для унификации цвета
green_low = np.array([45, 100, 50])
green_high = np.array([75, 255, 255])
# green_low = np.array([0, 102, 51])
# green_high = np.array([153, 255, 153])


curr_mask = cv2.inRange(hsv_img, green_low, green_high)
hsv_img[curr_mask > 0] = ([75, 255, 200])
view_image(hsv_img)     # Вывод


# 3. Преобразование HSV-изображения к оттенкам серого
RGB_again = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)
gray = cv2.cvtColor(RGB_again, cv2.COLOR_RGB2GRAY)
view_image(gray)     # Вывод


# 4. Пороговое изображение, последний этап
ret, threshold = cv2.threshold(gray, 90, 255, 0)
view_image(threshold)   # Вывод


# 5. Конечное оконтуривание
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
view_image(image)

"""
# Чтобы получить центр контура
cnt = contours[5]
M = cv2.moments(cnt)
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])
largest_area, largest_contour_index = find_greatest_contour(contours)

print(largest_area)
print(largest_contour_index)
print(len(contours))
print(cX)
print(cY)
"""
