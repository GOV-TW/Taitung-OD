# http://www.taitung.gov.tw/opendata/OD_OpenData_DealData.aspx?s=E5AA72D4F35F91D0
# get node content (metadata)
# and make .json file

import requests
from bs4 import BeautifulSoup as BS4
import json


def get_num(node_numb):
    node_numb_text = str(node_numb)
    zero_numb = 4 - len(node_numb_text)
    for i in range(zero_numb):
        node_numb_text = '0' + node_numb_text
    return node_numb_text


node_file = 'node_list.lst'

node_list = []
with open(node_file, 'r') as nf:
    for i in nf.readlines():
        node_list.append(i.strip())

# node_list = ['484A8E99E0E9CF5B']
node_numb = 0

for i_node in node_list:
    node_numb += 1
    node_matrix = {}
    node_url = 'http://www.taitung.gov.tw/opendata/OD_OpenData_DealData.aspx?s=' + i_node
    node_r = requests.get(node_url)
    node_content = BS4(node_r.content.decode('utf-8'), 'lxml')
    node_content = node_content.find('div','page_directory')
    node_matrix['title'] = node_content.h3.text.strip()
    node_matrix['node'] = i_node

    node_content = node_content.find_all('tr')
    for i in node_content:

        th = i.find_all('th')
        td = i.find_all('td')
        for j,k in enumerate(th):
            node_matrix[k.text.strip().replace('*', '').replace('：', '')] = td[j].text.strip()

    node_save = get_num(node_numb) + '. ' + node_matrix['資料集名稱'].replace('.csv', '') + '.json'
    with open('.\\datasets\\' + node_save, 'w', encoding='utf-8') as nw:
        json.dump(node_matrix, nw, ensure_ascii=False, indent=4)
    print(node_save)


