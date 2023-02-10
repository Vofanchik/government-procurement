#https://online-json.com/json-editor
from pprint import pprint

import requests

def api_request(customerregion=66, perpage=1, productsearch=None):
    payloads_ = {f'customerregion': customerregion, 'perpage': perpage,
                 'currentstage': 'EC', 'sort': '-signDate', 'fz': 44}
    response = requests.get(f"http://openapi.clearspending.ru/restapi/v3/contracts/search/?productsearch={productsearch}",
                            params=payloads_)
    l = list(response.json()['contracts']['data'])

    return l

if __name__ == '__main__':
    print(api_request(productsearch='перчатки'))
