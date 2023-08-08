import json
import os
import logging
from log_config import log_conf
logger = logging.getLogger(__name__)

def json_reader(input_path, conf_tipn, conf_sostt, conf_minqg, conf_maxqg, conf_pfak=0):
    


    # считывание json-файла

    # проверка на наличие файла
    if os.path.isfile(input_path):

        # проверка на пустой файл
        if os.stat(input_path).st_size > 0:

            logger.info('data file exists and not empty')

            with open(input_path, 'r', encoding='utf-8') as f:

                data = json.loads(f.read())

                # проверка наличия ключа data в файле
                if 'data' in data and data['data'] != []:

                    logger.info('file and data row were opened')

                    # инициализация списков
                    table_list = []
                    list_qg_0_ids = []
                    list_pfak = []

                    # получаем из data нужные нам поля:
                    for i in range(len(data['data'])):

                        # проверка наличия нужных нам полей в таблице
                        if 'tipn' not in data['data'][i]:
                            raise Exception('no tipn for object with id %s' % (data['data'][i]['id']))

                        if 'cnt' not in data['data'][i]:
                            raise Exception('no cnt for object with id  %s' % (data['data'][i]['id']))
                        if 'qg' not in data['data'][i]:
                            raise Exception('no qg for object with id  %s' % (data['data'][i]['id']))
                        if 'sost_t' not in data['data'][i]:
                            raise Exception('no sost_t for object with id  %s' % (data['data'][i]['id']))

                        # поля tipn, id, cnt и qg в таблице
                        table_tipn_field = data['data'][i]['tipn']
                        table_id_field = data['data'][i]['id']
                        table_cnt_field = data['data'][i]['cnt']
                        table_qg_field = data['data'][i]['qg']

                        table_sostt_field = data['data'][i]['sost_t']

                        # отдельная проверка для pfak - это поле не всегда нужно выводить
                        if 'p_fak' not in data['data'][i] and conf_pfak == 1:
                            raise Exception('no p_fak for object with id  %s' % (data['data'][i]['id']))
                        table_pfak_field = data['data'][i]['p_fak']

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

                    logger.info('successful file operation')

                    return table_list, list_qg_0_ids, list_pfak
                else:
                    logger.error('Incorrect file structure - incorrect data row')
                    raise Exception("Incorrect file structure - incorrect data row" )

        else:
            logger.error('Empty file')
            raise Exception("Empty file")

    else:
        logger.error('File does not exist')
        raise Exception("File does not exist")
