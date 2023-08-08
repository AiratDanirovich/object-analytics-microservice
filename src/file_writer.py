import xlsxwriter
from datetime import datetime
import logging
from log_config import log_conf

logger = logging.getLogger(__name__)

def excel_write(file_path, table_lst, pf_list=[]):
    # добавим дату в название файла для создания нескольких таблиц

    # output_path = file_path[:-5] + '_{}'.format(datetime.now().strftime("%d%m%Y_%H%M%S")) + file_path[-5:]

    output_path = file_path

    # создание excel книги
    workbook = xlsxwriter.Workbook(output_path)

    # название листа
    worksheet = workbook.add_worksheet("Object Worksheet")

    logger.info("excel book was created")

    # формат ячеек для настройки параметров текста
    # в нашем случае жирный текст
    cell_format_1 = workbook.add_format()
    cell_format_1.set_bold()
    cell_format_1.set_align('center')

    # запишем названия столбцов 1 и 2
    worksheet.write(0, 0, 'Название объекта', cell_format_1)
    worksheet.write(0, 1, 'Дебит жидкости', cell_format_1)

    row = 1
    col = 0

    # запишем данные для 2 столбцов - Название объекта и дебит
    # список содержит по 3 элемента для каждого объекта, нам нужны 2 и 3 из них ( 1 это id )
    for element in range(1, (len(table_lst) - 1), 3):  #
        worksheet.write(row, col, table_lst[element])
        worksheet.write(row, col + 1, table_lst[element + 1])

        row += 1
    logger.info("write 2 first columns")
    # Если в параметрах есть запись давления, добавим столбец с его значениями
    if pf_list:
        worksheet.write(0, 2, 'Фактическое давление', cell_format_1)
        row = 1
        col = 2
        for element in range(1, (len(pf_list))):
            worksheet.write(row, col, pf_list[element])
            row += 1
        logger.info("write column with p_fak")

    # автоматический размер ячеек

    worksheet.autofit()
    workbook.close()
    logger.info("excel file final version")

def zero_qg_writer(zero_qg_id_lst):
    logger.info('----------- zero qg list below ---------------------')
    logger.info(zero_qg_id_lst)
    logger.info('Wrote list with zero qg')
