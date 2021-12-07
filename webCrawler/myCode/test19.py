import json
import munch
import requests

def getResponse(url, funcName):
    response = requests.get(url)
    if response.status_code != 200:
        print(f'[{funcName}] response error ({response.status_code})')
        return
    print(f'[{funcName}] response success')
    return response

def getPChome24Product(pid):
    url = f'https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/{pid}-000&fields=Id,Name,Nick,Store,PreOrdDate,SpeOrdDate,Price,Discount,Pic&_callback=jsonp_prod'
    funcName = 'getPChome24Product'
    response = getResponse(url, funcName)

    script = response.text.replace('try{jsonp_prod(', '').replace(');}catch(e){if(window.console){console.log(e);}}', '')
    
    data = munch.munchify(json.loads(script))
    data = data[f'{pid}-000']
    print(f'產品代碼：{pid}')
    print(f'產品名稱：{data.Name}')
    print(f'產品原價：{data.Price.M}')
    print(f'產品售價：{data.Price.P}')

def searchProduct(keyword):
    url = 'https://ecshweb.pchome.com.tw/search/v3.3/?q=' + keyword
    funcName = 'searchProduct'
    response = getResponse(url, funcName)

    with open('pchomeSearch.html', 'wb') as f:
        f.write(response.content)

if __name__ == '__main__':
    keyword = 'dyson' 
    # searchProduct(keyword)

    pid = 'DCANDJ-A90095X3S'
    getPChome24Product(pid)