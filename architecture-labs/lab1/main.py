"""Точка входа для демонстрации результата выполнения лабораторной работы."""
import os

from get_file_names import get_file_names
from file_test import test_bmp_file


def main():
    images_list: list = get_file_names(os.getcwd() + '\\images')
    for image_name in images_list:
        print(f'Image: {image_name}')
        test_bmp_file(f'images\\{image_name}')
        print()


if __name__ == '__main__':
    main()
