'''
4.1. На основе кода, позволяющего визуализировать данные о ценах на недвижимость (точечная диаграмма), отобразить с
     помощью библиотеки mathplotlib линейные графики изменений цен на недвижимость, разбив всё множество данных
     на 3 подмножества.
'''

import numpy
import matplotlib.pyplot as plt
import scipy as sp
import csv
import datetime
import random

def draw_graph(x, y, plt, colors):
    """
    Рисование графика функции.
    """
    print(x)
    # polyfit подбирает коэффициенты модели
    f2p, residuals, rank, sv, rcond = numpy.polyfit(x, y, 2, full=True)
    f2 = sp.poly1d(f2p)

    fx = numpy.linspace(0, x[-1], 500)

    plt.plot(fx, f2(fx), linewidth=2.0, color=colors)
    plt.scatter(x, y, s=40, c=colors)
    plt.autoscale(tight=True)

    return plt.grid(True, linestyle='-', color='0.75')



def get_random_color():
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())


def diag(lable, args):
    k = len(args)
    x_rank =[i for i in range(0, len(args[0][-1]))]
    for i in range(k):
        [x, y] = args[i]
        colors = (get_random_color())
        draw_graph(x_rank, y[::-1], plt, colors)
    # plt.title('Scatter plot pythonspot.com')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(lable, loc="best")
    plt.savefig("VSR.png")
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
    diag(labels, datas_for_diag)
