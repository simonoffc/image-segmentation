# -*- coding: utf-8 -*-

import cv2


def view_image(image, name_of_window):
    """Функция вывода изображения"""
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


"""
image = cv2.imread("test_images/vik_nik.jpg")
# Выводим обычного ВикНика
view_image(image, 'Viktor Nikolaevich regular')

# Делаем ВикНика чб, потом цветным
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, threshold_image = cv2.threshold(image, 127, 255, 0)
view_image(gray_image, "Vik-Nik bw")
view_image(threshold_image, "Vik-Nik gray")
"""

# """
# Распознавание лиц
image_path = "test_images/hard_test4.jpg"
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(10, 10)
)
faces_detected = "Face detected: " + format(len(faces))
print(faces_detected)
# Рисуем квадраты вокруг лиц
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
view_image(image, faces_detected)
# """

"""
image = cv2.imread("test_images/vik_nik.jpg")

blue, green, red = cv2.split(image)    # Split the image into its channels
img_gs = cv2.imread('test_images/vik_nik.jpg', cv2.IMREAD_GRAYSCALE)    # Convert image to grayscale

view_image(red, 'red')    # Display the red channel in the image
view_image(blue, 'blue')    # Display the red channel in the image
view_image(green, 'green')    # Display the red channel in the image
view_image(img_gs, 'img_gs')    # Display the grayscale version of image

# Вывод некторой информации о изображении
print("Image Properties")
print("- Number of Pixels: " + str(image.size))
print("- Shape/Dimensions: " + str(image.shape))
"""

# cv2.imwrite("test_images/ava_o_problem_res.jpg", image)   # Сохранение результата
