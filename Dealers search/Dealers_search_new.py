from pprint import pprint

import requests

def api_request(customerregion=66, perpage=10, productsearch=None):
    payloads_ = {f'customerregion': customerregion, 'perpage': perpage, 'currentstage': 'EC', 'sort': '-signDate'}
    response = requests.get(f"http://openapi.clearspending.ru/restapi/v3/contracts/search/?productsearch={productsearch}",
                            params=payloads_)
    l = list(response.json()['contracts']['data'])

    return l

if __name__ == '__main__':
    pprint(api_request(productsearch='перчатки'))
