import cv2
import numpy as np


# Функции для удобства
def view_image(name_of_window, image):
    """Функция вывода изображения"""
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def change_size(image, percent: int):
    """Функция изменения размера изображения, чтобы оно выводилось корректно"""
    width = int(img.shape[1] * percent / 100)
    height = int(img.shape[0] * percent / 100)
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resized


# Считывакм и переводим в
img = cv2.imread('images/Nil.jpg')

# dark_green = (0, 30, 0)     # Вполне различимый зелёный
# light_green = (0, 255, 0)   # Супер-мега ярко зелёный
#
# mask = cv2.inRange(hsv_nemo, light_orange, dark_orange)

view_image("test", img)
