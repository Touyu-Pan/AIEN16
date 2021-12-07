import json
import time

import munch
import requests

def getResponse(url, funcName):
    # get response
    response = requests.get(url)

    # print response status
    if response.status_code != 200:
        print(f'[{funcName}] response error ({response.status_code})')
        return
    print(f'[{funcName}] response success')
    
    time.sleep(2)

    return response
    
def ConvJsonStr(text):
    return munch.munchify(json.loads(text))