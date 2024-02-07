import struct


def convert_bmp(input_file, output_file, new_bit_count):
    if new_bit_count not in [1, 4, 8, 16, 24]:
        raise IndexError("Ошибка: Неподдерживаемое число бит на пиксел для нового формата.")

    with open(input_file, 'rb') as f_in:
        bmp_header = f_in.read(14)  # Читаем заголовок файла
        with open(output_file, 'wb') as f_out:
            f_out.write(bmp_header)  # Пишем его в выходной файл

            bmp_info_header = f_in.read(40)  # Читаем заголовок изображения
            f_out.write(bmp_info_header)  # Пишем его в выходной файл

            # Читаем цветовую палитру (если есть) для 8- и 4-битных изображений
            if new_bit_count <= 8:
                palette_size = 4 * 2**new_bit_count
                palette = f_in.read(palette_size)
                f_out.write(palette)

            # Читаем данные пикселей
            width, height = struct.unpack('<ii', bmp_info_header[4:12])
            padding = (4 - (width * (new_bit_count // 8)) % 4) % 4

            for _ in range(height):
                for _ in range(width):
                    pixel_data = f_in.read(3)  # Читаем данные пикселя в формате RGB (24 бита)
                    # Здесь можно добавить код для преобразования формата пикселя
                    # в новый формат, в зависимости от требований

                # Пропускаем ненужные байты, если есть отступы в конце строки
                f_in.read(padding)

                # Записываем отступы в конец строки нового изображения
                f_out.write(b'\x00' * padding)


if __name__ == '__main__':
    convert_bmp('images/input/Airplane.bmp', 'output.bmp', 8)  # Пример преобразования в 8-битное изображение
