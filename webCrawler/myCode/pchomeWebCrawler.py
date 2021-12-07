import time
from urllib import parse as UP

import util

def removeUselessScript(script):
    #移除 JSON 資料前後無用的 JS程式碼
    return script.replace('try{jsonp_prod(', '').replace(');}catch(e){if(window.console){console.log(e);}}', '')

def getPChome24Product(pid):
    # define url and function name to get response
    url = f'https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/{pid}-000&fields=Id,Name,Nick,Store,PreOrdDate,SpeOrdDate,Price,Discount,Pic&_callback=jsonp_prod'

    response = util.getResponse(url, getPChome24Product.__name__)

    # clean the result we get from pchome
    script = removeUselessScript(response.text)
    
    # turn result into Object
    data = util.ConvJsonStr(script)
    data = data[f'{pid}-000']

    print(f'產品代碼：{pid}')
    print(f'產品名稱：{data.Name}')
    print(f'產品原價：{data.Price.M}')
    print(f'產品售價：{data.Price.P}')
    print(r'----------------')

    time.sleep(2)

def searchPChome24Product(keyword):
    page = 1
    maxPage = 1

    while True:
        # define url and function name to get response
        url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=' + UP.quote(keyword) + f'&page={page}&sort=sale/dc'
        print(url)
        response = util.getResponse(url, searchPChome24Product.__name__)

        # turn response into an Object
        data = util.ConvJsonStr(response.content)

        # get information from each product
        for prod in data.prods:
            getPChome24Product(prod.Id)
        
        # limit the searching pages
        page += 1
        if page > data.totalPage or page > maxPage:
            break

if __name__ == '__main__':

    keyword = 'dyson' 
    searchPChome24Product(keyword)