"""Точка входа для демонстрации результата выполнения лабораторной работы."""
import os

from get_file_names import get_file_names
from file_test import test_bmp_file


def test_bmp_files():
    # todo: сделать поменьше фотографий
    images_list: list = get_file_names(os.getcwd() + '\\images')
    for image_name in images_list:
        print(f'Image: {image_name}')
        test_bmp_file(f'images\\{image_name}')
        print()


def convert_bmp_files():
    ...


if __name__ == '__main__':
    test_bmp_files()
    convert_bmp_files()
