from file_reader import json_reader
from file_writer import excel_write, zero_qg_writer
from graph_creator import matplot_graph, plotly_graph
from config import Config
import logging
import datetime

from log_config import log_conf

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    # выполним чтение json файла и запишем данные в 3 списка -
    # список с именем и дебитом, id для объектов с 0 дебитом и список давлений

    '''
    import time
    t1=time.time()
    test=[]
    for i in range(1,int(1e6)):
        if not i%2:
            test.append(i/2)
        else:
            test.append(10)
    print(time.time()-t1)
    t1 = time.time()
    test2 = []
    test2 = [i/2 if not i%2 else 10 for i in range(1,int(1e6))]
    print(time.time() - t1)
    '''

    table_list, qg0lst, p_fak_list = json_reader(
        Config.input_path,  # путь для входных данных
        Config.tipn,  # tipn параметр
        Config.sost_t,  # sost_t параметр
        Config.qg_min,  # параметр для min qg
        Config.qg_max,  # параметр для max qg
        Config.p_fak_write)  # записывать ли p_fak

    logger.info("File with data was opened")

    # запишем id объектов с нулевым qg в отдельный файл
    zero_qg_writer(qg0lst)

    logging.info("Zero qg's were checked")

    excel_write(Config.output_path,  # путь для выходных данных
            table_list,  # список с id, cnt и qg объектов
            p_fak_list)  # список с давлениями объектов
    logger.info('Excel file was created')
    # построение графика с объектами и их дебитами

    # matplot_graph(table_list) # matplot
    logger.info('Matplot graph was created')

    plotly_graph(table_list, is_scatter=Config.is_scatter)  # plotly
    logger.info('Plotly graph was created')
