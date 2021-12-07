import json
import time

import munch
import requests

def GET(func, url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f'[{func}] response error ({response.status_code})')
        return
    print(f'[{func}] response success')

    time.sleep(2)

    return response

def ConvJsonStr(text):
    return munch.munchify(json.loads(text))