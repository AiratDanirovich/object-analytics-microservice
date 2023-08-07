from file_reader import json_reader
from file_writer import excel_write, zero_qg_writer
from graph_creator import matplot_graph, plotly_graph
from config import Config
import logging

if __name__ == "__main__":
    # выполним чтение json файла и запишем данные в 3 списка -
    # список с именем и дебитом, id для объектов с 0 дебитом и список давлений
    table_list, qg0lst, p_fak_list = json_reader(
        Config.input_path,  # путь для входных данных
        Config.tipn,  # tipn параметр
        Config.sost_t,  # sost_t параметр
        Config.qg_min,  # параметр для min qg
        Config.qg_max,  # параметр для max qg
        Config.p_fak_write)  # записывать ли p_fak

    # запишем id объектов с нулевым qg в отдельный файл
    zero_qg_writer(qg0lst)

    # excel_write(Config.output_path,  # путь для выходных данных
    #         table_list,  # список с id, cnt и qg объектов
    #         p_fak_list)  # список с давлениями объектов

    # построение графика с объектами и их дебитами

    # matplot_graph(table_list) # matplot
    plotly_graph(table_list)  # plotly
