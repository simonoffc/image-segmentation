"""Точка входа для демонстрации результата выполнения лабораторной работы."""
import os

from get_file_names import get_file_names
from file_test import test_bmp_file
from converter import convert_bmp


def test_bmp_files():
    # todo: сделать поменьше фотографий
    images_list: list = get_file_names(os.getcwd() + '\\images\\input')
    for image_name in images_list:
        print(f'Image: {image_name}')
        test_bmp_file(f'images\\input\\{image_name}')
        print()


def convert_bmp_files():
    images_list: list = get_file_names(os.getcwd() + '\\images\\input')
    for image_name in images_list:
        print(f'Image: {image_name}')
        convert_bmp(f'images\\input\\{image_name}', f'images\\output\\output_{image_name}', 8)
        print('Convertation completed.')


if __name__ == '__main__':
    test_bmp_files()
    print('+---------------------------------+')
    convert_bmp_files()
