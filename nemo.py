# -*- coding: utf-8 -*-


# Программа для поиска сегментов по заданому цветовому диапазону в BGR, на примере рыбки Немо
"""Основной код из статьи: https://pythonru.com/biblioteki/segmentacija-izobrazhenija-s-opencv-i-python"""


import cv2


# Функция для удобства
def view_image(name_of_window, image):
    """Функция вывода изображения"""
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Считываем картинку (точно такой же Немо, что из статьи)
img = cv2.imread('./images/nemo.png')

"""Нашел другого Немо, у которого слегка отличается оранжевый цвет"""
# img = cv2.imread('./images/nemo_real.jpg')
"""
Результат: неверно выбирает сегмент
Причина: оранжевый оттенок на картинке не подходит под заданный нами диапазон
"""

view_image("normal RGB image", img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
view_image("BGR image", img)

# Переводим в HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
view_image("hsv image", hsv_img)

# Диапазон оранжевого цвета в BGR, если хотим искать сегменты с оттенками оражевого
light_col = (1, 190, 200)
dark_col = (18, 255, 255)

# Когда необходимый цветовой диапазон выбран, можно использовать cv2.inRange(), чтобы разбить изображение
mask = cv2.inRange(hsv_img, light_col, dark_col)

# Чтобы наложить маску поверх оригинального изображения, используется cv2.bitwise_and()
result = cv2.bitwise_and(hsv_img, hsv_img, mask=mask)

# Выводим изображения
view_image("mask", mask)
view_image("result", result)
