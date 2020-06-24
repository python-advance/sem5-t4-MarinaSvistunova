'''
4.1. Используя свободные источники (bn.ru, avito.ru и т.д.), собрать данные о ценах на недвижимость,
     выставленную на продажу в разных районах города. Преобразовать данные в формат csv. Разработать
     скрипт для визуализации данных, используя библиотеку mathplotlib. Для визуализации использовать
     тип “точечная диаграмма” (scatterplot).

4.2. Разработать фрагмент программы с использованием библиотеки pyqrcode, позволяющей создавать
     изображение QR-кода на основе переданной в программу текстовой строки.

4.3.  Реализовать модификацию изображения генерируемого QR-кода: раскрасить фрагменты изображения
      в несколько случайно определяемых цветов.
'''

import csv
import matplotlib.pyplot as plt
import datetime
import random


def get_random_color():
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())


def diag(lable, args):
    print(args)
    k = len(args)
    for i in range(k):
        [x, y] = args[i]
        print(x, y)
        numbers = len(y)
        colors = (get_random_color())
        area = 70
        # Plot
        plt.scatter(x, y, s=area, c=colors, alpha=1.)
    # plt.title('Scatter plot pythonspot.com')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(lable, loc="best")
    plt.savefig("ISR-4-1.png")
    plt.show()



def csv_reader(file_csv):
    reader = csv.reader(file_csv, delimiter=';')
    datas = {'date': [], 'first': [], 'changesFirst': [], 'second': [], 'changesSecond': []}
    for line in reader:
        datas['date'] += [line[0]]
        datas['first'] += [float(line[1])]
        datas['changesFirst'] += [line[2]]
        datas['second'] += [float(line[3])]
        datas['changesSecond'] += [line[4]]
    data_1 = datas['date']
    time = []
    for i in range(len(data_1)):
        data_1[i] = data_1[i].split('.')
        data_1[i] = [int(k) for k in data_1[i]]
        data_1[i] = (data_1[i][::-1])
        k = datetime.date(data_1[i][0], data_1[i][1], data_1[i][2])
        time += [k]
    return time, datas['first']


if __name__ == "__main__":
    csv_path = "flats.csv"  # Приморский
    csv_path_1 = "flats_1.csv"  # Московский
    csv_path_2 = "flats_2.csv"  # Василеостровский
    datas_for_diag = []
    paths = [csv_path, csv_path_1, csv_path_2]
    labels = ['Приморский район', 'Московский район', 'Василеостровский район']
    for i in range(len(paths)):
        with open(paths[i], encoding='utf-8', newline='') as f_obj:
            datas_for_diag += [csv_reader(f_obj)]
    # print(datas_for_diag[0])
    diag(labels, datas_for_diag)
