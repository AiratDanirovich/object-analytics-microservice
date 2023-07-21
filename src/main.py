from file_reader import jsonreader
from file_writer import excel_write, zero_qg_writer
from graph_creator import matplot_graph
import config

input_file_path = config.input_path
output_file_path = config.output_path

if __name__ == "__main__":
    # выполним чтение json файла и запишем данные в 3 списка -
    # список с именем и дебитом, id для объектов с 0 дебитом и список давлений
    table_list, qg0lst, p_fak_list = jsonreader(
        input_file_path,  # путь для входных данных
        config.tipn,  # tipn параметр
        config.sost_t,  # sost_t параметр
        config.qg_min,  # параметр для min qg
        config.qg_max,  # параметр для max qg
        config.p_fak_write)  # записывать ли p_fak

    # запишем id объектов с нулевым qg в отдельный файл
    zero_qg_writer(qg0lst)

    excel_write(output_file_path,  # путь для выходных данных
                table_list,  # список с id, cnt и qg объектов
                p_fak_list)  # список с давлениями объектов

    # построение графика с объектами и их дебитами
    matplot_graph(table_list)
