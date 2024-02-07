import struct


def test_bmp_file(filename):
    with open(filename, 'rb') as f:
        # Считываем заголовок файла BMP (14 байт)
        bmp_header = f.read(14)

        # Размер файла
        file_size = struct.unpack('<I', bmp_header[2:6])[0]
        print(f"Размер файла: {file_size} байт")

        # Считываем заголовок изображения BMP (40 байт)
        bmp_info_header = f.read(40)

        # Ширина и высота изображения
        width, height = struct.unpack('<ii', bmp_info_header[4:12])
        print(f"Ширина изображения: {width} пикселей")
        print(f"Высота изображения: {height} пикселей")

        # Число бит на пиксел
        bit_count = struct.unpack('<H', bmp_info_header[14:16])[0]
        print(f"Число бит на пиксел: {bit_count}")

        # Проверка на допустимое число бит на пиксел
        if bit_count not in [8, 24]:
            print("Ошибка: поддерживаются только изображения с 8 или 24 битами на пиксел.")
            return

        # Здесь можно добавить другие проверки или анализ заголовка файла
        # Например, проверку на наличие компрессии и др.


if __name__ == '__main__':
    test_bmp_file('images/input/Airplane.bmp')
