import xlsxwriter
from datetime import datetime


def excel_write(file_path, table_lst, pf_list=[]):
    # добавим дату в название файла для создания нескольких таблиц

    #output_path = file_path[:-5] + '_{}'.format(datetime.now().strftime("%d%m%Y_%H%M%S")) + file_path[-5:]

    output_path = file_path
    # создание excel книги
    workbook = xlsxwriter.Workbook(output_path)

    # название листа
    worksheet = workbook.add_worksheet("Object Worksheet")

    # запишем названия столбцов 1 и 2
    worksheet.write(0, 0, 'Название объекта')
    worksheet.write(0, 1, 'Дебит жидкости')

    row = 1
    col = 0

    # запишем данные для 2 столбцов - Название объекта и дебит
    # список содержит по 3 элемента для каждого объекта, нам нужны 2 и 3 из них ( 1 это id )
    for element in range(1, (len(table_lst) - 1), 3):  #
        worksheet.write(row, col, table_lst[element])
        worksheet.write(row, col + 1, table_lst[element + 1])

        row += 1

    # Если в параметрах есть запись давления, добавим столбец с его значениями
    if pf_list:
        worksheet.write(0, 2, 'Фактическое давление')
        row = 1
        col = 2
        for element in range(1, (len(pf_list))):
            worksheet.write(row, col, pf_list[element])
            row += 1

    workbook.close()


def zero_qg_writer(zero_qg_id_lst):
    lst = zero_qg_id_lst
    file = open('../output_data/zero_qg_id_list.txt', 'w')
    for element in lst:
        file.write(str(element))
        file.write('\n')
    file.close()
