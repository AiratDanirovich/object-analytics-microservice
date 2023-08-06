import json
import os


#  метод, отвечающий за открытие и обработку json:

def json_reader(input_path, conf_tipn, conf_sostt, conf_minqg, conf_maxqg, conf_pfak=0):
    # считывание json-файла

    # проверка на наличие файла
    if os.path.isfile(input_path):

        # проверка на пустой файл
        if os.stat(input_path).st_size > 0:
            with open(input_path, 'r', encoding='utf-8') as f:

                data = json.loads(f.read())

                # проверка наличия ключа data в файле
                if 'data' in data:
                    # инициализация списков
                    table_list = []
                    list_qg_0_ids = []
                    list_pfak = []

                    # получаем из data нужные нам поля:
                    for i in range(len(data['data'])):

                        # поля из таблицы - tipn, id, cnt, qg, p_fak и sost_t:

                        table_tipn_field = data['data'][i]['tipn']
                        table_id_field = data['data'][i]['id']
                        table_cnt_field = data['data'][i]['cnt']
                        table_qg_field = data['data'][i]['qg']
                        table_pfak_field = data['data'][i]['p_fak']
                        table_sostt_field = data['data'][i]['sost_t']

                        # проходим по json-файлу и ищем записи объектов с подходящими нам параметрами,
                        # они указаны в конфиге - sost_t, agent, tipn, min qg и max qg:

                        if table_tipn_field == conf_tipn and (
                                table_id_field not in table_list) and table_sostt_field == conf_sostt:
                            if conf_minqg <= table_qg_field <= conf_maxqg:
                                # запишем в список id, cnt и qg
                                # при дальнейшей записи в excel-файл, поле id предотвращает дублирование объектов, если
                                # в поле с именем будет ошибка:
                                table_list.append(table_id_field)
                                table_list.append(table_cnt_field)
                                table_list.append(table_qg_field)

                                # сохраняем id объектов с нулевым qg:
                                if table_qg_field == 0.0:
                                    list_qg_0_ids.append(table_id_field)
                                # сохраняем давления в список, если выбрана их запись:
                                if conf_pfak == 1:
                                    list_pfak.append(table_pfak_field)

                    # передаем 3 списка: имя + дебит, нулевые дебиты и список давлений
                    return table_list, list_qg_0_ids, list_pfak
                else:
                    raise Exception("Incorrect file structure - data row does not exist")
        else:
            raise Exception("Empty file")

    else:
        raise Exception("File does not exist")
