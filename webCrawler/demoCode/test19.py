import time
import json

import munch
import requests

import util

def removeUselessScript(script):
    # 移除 JSON 資料前後無用的 JS 程式碼
    return script.replace('try{jsonp_prod(', '').replace(');}catch(e){if(window.console){console.log(e);}}', '')

def getPChome24Product(pid):
    url = f'https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/{pid}-000&fields=Id,Name,Nick,Store,PreOrdDate,SpeOrdDate,Price,Discount,Pic&_callback=jsonp_prod'
    response = util.GET('getPChome24Product', url)

    script = removeUselessScript(response.text)
    
    data = util.ConvJsonStr(script)
    data = data[f'{pid}-000']
    print(f'產品代碼：{pid}')
    print(f'產品名稱：{data.Name}')
    print(f'產品原價：{data.Price.M}')
    print(f'產品售價：{data.Price.P}')

if __name__ == '__main__':
    pid = 'DCANDJ-A90095X3S'
    getPChome24Product(pid)