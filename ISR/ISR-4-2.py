'''
4.2. Разработать фрагмент программы с использованием библиотеки pyqrcode, позволяющей создавать
     изображение QR-кода на основе переданной в программу текстовой строки.

4.3.  Реализовать модификацию изображения генерируемого QR-кода: раскрасить фрагменты изображения
      в несколько случайно определяемых цветов.
'''


import pyqrcode
import png
import random


def get_random_color():
    r = lambda: random.randint(0, 255)
    return (r(), r(), r())


def qr_simple(str_input):
    QR = pyqrcode.create(str_input)
    QR.png('ISR-4-2.png', scale=13)


def qr_color(str_input):
    QR = pyqrcode.create(str_input)
    QR = QR.text().split('\n')[0:-1]

    pallet = []
    for row in QR:
        pallet_line = ()
        for c in row:
            if int(c) == 1:
                pallet_line += get_random_color()
            else:
                pallet_line += (255, 255, 255)
        pallet += [pallet_line]

    file = open('ISR-4-3.png', 'wb')
    w = png.Writer(len(QR[0]), len(QR), greyscale=False)
    w.write(file, pallet)
    file.close()


if __name__ == '__main__':
    input_str = input()
    qr_simple(input_str)
    qr_color(input_str)