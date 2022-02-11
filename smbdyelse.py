import requests
from bs4 import BeautifulSoup
from pprint import pprint
# data = {'id': '6231',
#         'table_name': 'med_products',
#         'fancybox': 'true'}
#
# headers = {'Accept': '*/*',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
# 'Connection': 'keep-alive',
# 'Cookie': '_ym_uid=163205177663442347; _ym_d=1632051776; uid=3230190944360843000; _ym_isad=2; _ym_visorc=w; sputnik_session=1644580559537|1',
# 'DNT': '1',
# 'Host': 'roszdravnadzor.gov.ru',
# 'If-Modified-Since': 'Fri, 11 Feb 2022 12:27:17 GMT',
# 'Referer': 'https://roszdravnadzor.gov.ru/',
# 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
# 'sec-ch-ua-mobile': '?0',
# 'sec-ch-ua-platform': "Windows",
# 'Sec-Fetch-Dest': 'empty',
# 'Sec-Fetch-Mode': 'cors',
# 'Sec-Fetch-Site': 'same-origin',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
# 'X-Requested-With': 'XMLHttpRequest'}
#
# res = requests.post('https://roszdravnadzor.gov.ru/services/misearch', headers=headers, data=data)
# print(res.text)

# data = {
# 'draw': '4',
# 'columns[0][data]': 'col1.label',
# 'columns[0][name]': '',
# 'columns[0][searchable]': 'true',
# 'columns[0][orderable]': 'true',
# 'columns[0][search][value]': '',
# 'columns[0][search][regex]': 'false',
# 'columns[1][data]': 'col2.label',
# 'columns[1][name]': '',
# 'columns[1][searchable]': 'true',
# 'columns[1][orderable]': 'true',
# 'columns[1][search][value]': '',
# 'columns[1][search][regex]': 'false',
# 'columns[2][data]': 'col3.label',
# 'columns[2][name]': '',
# 'columns[2][searchable]': 'true',
# 'columns[2][orderable]': 'true',
# 'columns[2][search][value]': '',
# 'columns[2][search][regex]': 'false',
# 'columns[3][data]': 'col4.label',
# 'columns[3][name]': '',
# 'columns[3][searchable]': 'true',
# 'columns[3][orderable]': 'true',
# 'columns[3][search][value]':'',
# 'columns[3][search][regex]': 'false',
# 'columns[4][data]': 'col5.label',
# 'columns[4][name]':'',
# 'columns[4][searchable]': 'true',
# 'columns[4][orderable]': 'true',
# 'columns[4][search][value]':'',
# 'columns[4][search][regex]': 'false',
# 'columns[5][data]': 'col6.label',
# 'columns[5][name]':'',
# 'columns[5][searchable]': 'true',
# 'columns[5][orderable]': 'true',
# 'columns[5][search][value]':'',
# 'columns[5][search][regex]': 'false',
# 'columns[6][data]': 'col7.label',
# 'columns[6][name]':'',
# 'columns[6][searchable]': 'true',
# 'columns[6][orderable]': 'true',
# 'columns[6][search][value]':'',
# 'columns[6][search][regex]': 'false',
# 'columns[7][data]': 'col8.label',
# 'columns[7][name]':'',
# 'columns[7][searchable]': 'true',
# 'columns[7][orderable]': 'true',
# 'columns[7][search][value]':'',
# 'columns[7][search][regex]': 'false',
# 'columns[8][data]': 'col9.label',
# 'columns[8][name]':'',
# 'columns[8][searchable]': 'true',
# 'columns[8][orderable]': 'true',
# 'columns[8][search][value]':'',
# 'columns[8][search][regex]': 'false',
# 'columns[9][data]': 'col10.label',
# 'columns[9][name]':'',
# 'columns[9][searchable]': 'true',
# 'columns[9][orderable]': 'true',
# 'columns[9][search][value]':'',
# 'columns[9][search][regex]': 'false',
# 'columns[10][data]':'col11.label',
# 'columns[10][name]':'',
# 'columns[10][searchable]': 'true',
# 'columns[10][orderable]': 'true',
# 'columns[10][search][value]':'',
# 'columns[10][search][regex]': 'false',
# 'columns[11][data]': 'col12.label',
# 'columns[11][name]':'',
# 'columns[11][searchable]': 'true',
# 'columns[11][orderable]': 'true',
# 'columns[11][search][value]':'',
# 'columns[11][search][regex]': 'false',
# 'columns[12][data]': 'col13.label',
# 'columns[12][name]':'',
# 'columns[12][searchable]': 'true',
# 'columns[12][orderable]': 'true',
# 'columns[12][search][value]':'',
# 'columns[12][search][regex]': 'false',
# 'columns[13][data]': 'col14.label',
# 'columns[13][name]':'',
# 'columns[13][searchable]': 'true',
# 'columns[13][orderable]': 'true',
# 'columns[13][search][value]':'',
# 'columns[13][search][regex]': 'false',
# 'columns[14][data]': 'col15.label',
# 'columns[14][name]':'',
# 'columns[14][searchable]': 'true',
# 'columns[14][orderable]': 'true',
# 'columns[14][search][value]':'',
# 'columns[14][search][regex]': 'false',
# 'columns[15][data]': 'col16.label',
# 'columns[15][name]':'',
# 'columns[15][searchable]': 'true',
# 'columns[15][orderable]': 'true',
# 'columns[15][search][value]':'',
# 'columns[15][search][regex]': 'false',
# 'columns[16][data]': 'col17.label',
# 'columns[16][name]':'',
# 'columns[16][searchable]': 'true',
# 'columns[16][orderable]': 'true',
# 'columns[16][search][value]':'',
# 'columns[16][search][regex]': 'false',
# 'order[0][column]': '0',
# 'order[0][dir]': 'asc',
# 'start': '0',
# 'length': '25',
# 'search[value]':'',
# 'search[regex]': 'false',
# 'prev_total': '5',
# 'q_mi_label_application': 'isis c2',
# 'q_prod_address_post':'',
# 'q_appl_label':'',
# 'q_okp':'',
# 'q_no_uniq':'',
# 'id_sclass':'',
# 'q_no':'',
# 'q_appl_address':'',
# 'q_prod_label':'',
# 'q_prod_address':'',
# 'q_in_accordance_nomen':'',
# 'q_prescription':'',
# 'q_address_production':'',
# 'q_appl_address_post':'',
# 'dt_ru_end_from':'',
# 'dt_ru_end_to':'',
# 'dt_ru_from':'',
# 'dt_ru_to':'',
# 'q_interchangeability_med_products':'',
# }
#
# headers = {
# 'Accept': 'application/json, text/javascript, */*; q=0.01',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
# 'Connection': 'keep-alive',
# 'Content-Length': '4171',
# 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
# 'DNT': '1',
# 'Host': 'roszdravnadzor.gov.ru',
# 'Origin': 'https://roszdravnadzor.gov.ru',
# 'Referer': 'https://roszdravnadzor.gov.ru/',
# 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
# 'sec-ch-ua-mobile': '?0',
# 'sec-ch-ua-platform': "Windows",
# 'Sec-Fetch-Dest': 'empty',
# 'Sec-Fetch-Mode': 'cors',
# 'Sec-Fetch-Site': 'same-origin',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
# 'X-Requested-With': 'XMLHttpRequest'
# }

# res = requests.post('https://roszdravnadzor.gov.ru/ajax/services/misearch', headers=headers, data=data)
# print(res)
#
# # pprint(res.json()['data'])
#
# for all in res.json()['data']:
#     # print(all)
#     print(all['col1']['label'].replace('o', ''))






# headers = {'Accept': '*/*',
#              'Accept-Encoding': 'gzip, deflate, br',
#              'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#              'Connection': 'keep-alive',
#              'DNT': '1',
#              'Host': 'zakupki.gov.ru',
#              'Referer': 'https://zakupki.gov.ru/epz/ktru/search/results.html',
#              'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
#              'sec-ch-ua-mobile': '?0',
#              'sec-ch-ua-platform': "Windows",
#              'Sec-Fetch-Dest': 'empty',
#              'Sec-Fetch-Mode': 'cors',
#              'Sec-Fetch-Site': 'same-origin',
#              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
#              'X-Requested-With': 'XMLHttpRequest'}
#
# data = {'searchString': '122570',
#          'ktruClassifierId': '296',
#          'source': 'M',
#          'recordsPerPage': '_500',
#          'search': 'true',
#          'medicalProduct': 'false'}
#
# res = requests.post('https://zakupki.gov.ru/epz/ktru/ktruClassifiers/items.html', headers=headers, data=data)
#
# soup = BeautifulSoup(res.text, 'html.parser')
#
# name = soup.find(class_="ktruClassifiersItems")
#
# print(name.get_text().replace('\n', '')[7:])


headers = {   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Cookie': '_ym_uid=1630900769777928721; _ym_d=1630900769; contractCsvSettingsId=9feab4cb-ade1-4b6f-84ba-19b7b87faacd; _ym_isad=2; contentFilter=; _ym_visorc=b',
    'DNT': '1',
    'Host': 'zakupki.gov.ru',
    'Referer': 'https://zakupki.gov.ru/epz/ktru/search/results.html',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Windows',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}

data = {'searchString': 'перчатки',
 'morphology': 'on',
 'search-filter': 'Наименованию позиции',
 'active': 'on',
 'ktruCharselectedTemplateItem': '0',
 'sortBy': 'ITEM_NAME',
 'pageNumber': '1',
 'sortDirection': 'false',
 'recordsPerPage': '_10',
 'showLotsInfoHidden': 'false',
 'rubricatorIdSelected': '369'}

res = requests.post('https://zakupki.gov.ru/epz/ktru/ktruClassifiers/items.html', headers=headers, data=data)
# soup = BeautifulSoup(res.text, 'html.parser')
pprint(res.text)
# print(soup.find_all(class_ = 'ktruClassifiersItems'))

# for all in soup.find_all(class_ = 'ktruClassifiersItems'):
#     print(all.text)