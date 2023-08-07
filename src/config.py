import json


class Config:
    conf_path = "../input_data/config.json"
    with open(conf_path, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())

    if 'tipn' not in data['params']:
        raise Exception('no config tipn provided')

    if 'agent' not in data['params']:
        raise Exception('no config agent provided')

    if 'qg_max' not in data['params']:
        raise Exception('no config qg_max provided')
    if 'qg_min' not in data['params']:
        raise Exception('no config qg_min provided')

    if 'config_p_fak_write' not in data['params']:
        raise Exception('no config p_fak_write provided')

    if 'input_path' not in data['params']:
        raise Exception('no config input_path provided')
    if 'output_path' not in data['params']:
        raise Exception('no config output_path provided')

    agent = data['params']['agent']
    sost_t = data['params']['sost_t']
    qg_max = data['params']['qg_max']
    qg_min = data['params']['qg_min']
    tipn = data['params']['tipn']
    p_fak_write = data['params']['p_fak_write']
    input_path = data['params']['input_path']
    output_path = data['params']['output_path']
