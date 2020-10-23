# -*- coding: utf-8 -*-

"""
Статья: https://www.freecodecamp.org/news/sketchify-turn-any-image-into-a-pencil-sketch-with-10-lines-of-code-cf67fa4f68ce/
"""

import os
import cv2
import numpy as np
import imageio
import scipy.ndimage
import matplotlib.pyplot as plt


def view_image(image, title):
    """Функция вывода изображения"""
    cv2.namedWindow(title, cv2.WINDOW_NORMAL)
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def grayscale(rgb):
    """Функция применение оттенков серого"""
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])


def dodge(front, back):
    """Функция уклонения и слияния"""
    result = front * 255 / (255 - back)
    result[result > 255] = 255
    result[back == 255] = 255
    return result.astype('uint8')


# Для быстроты проведения тестов сделаем цилк, который будет прогонять все изображения по алгоритму
dir_name = "/images"
test = os.listdir(dir_name)

s = 0
for img in test:
    if img.endswith(".jpg"):
        start_img = imageio.imread(f"images/{img}")
        # start_img.shape(196, 160, 30)

        # Применение оттенков серого
        gray_img = grayscale(start_img)

        # Инвертирование изображения
        inverted_img = 255 - gray_img

        # Размытие изображения
        blur_img = scipy.ndimage.filters.gaussian_filter(inverted_img, sigma=5)

        # Уклонение и слияние
        final_img = dodge(blur_img, gray_img)

        # view_image(final_img, img)
        # from time import sleep
        # sleep(4)

        s += 1
        plt.imshow(final_img, cmap="gray")
        plt.imsave(f'final_images/img{s}.png', final_img, cmap='gray', vmin=0, vmax=255)  # Сохранение

print(s)
