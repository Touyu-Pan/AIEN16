import time
import urllib.parse as UP

import munch
import requests

import test19
import util

def searchPChome24Products(keyword):
    page = 1
    # 限制查詢頁數
    pageMax = 1
    while True:
        url = f'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={UP.quote(keyword)}&page={page}&sort=sale/dc'
        response = util.GET('searchPChome24Products', url)

        data = util.ConvJsonStr(response.text)
        
        for prod in data.prods:
            print(f'{prod.Id}\t{prod.name}')
            test19.getPChome24Product(prod.Id)

        page = page + 1
        # 不限制查詢頁數
        # if page > data.totalPage:
        #     break
        # 限制查詢頁數
        if page > data.totalPage or page > pageMax:
            break

if __name__ == '__main__':
    keyword = 'dyson'
    searchPChome24Products(keyword)