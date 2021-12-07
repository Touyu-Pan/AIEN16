import datetime
import requests
import munch

def getStockData():
    # date = datetime.datetime.today().strftime('%Y%m%d')
    date = ''
    # date=YYYYMMDD
    # type=MS 大盤統計資訊
    url = f'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date={date}&type=MS'
    print(url)

    response = requests.get(url)
    if response.status_code != 200:
        print(f'response error ({response.status_code})')
        return
    print(f'response success')

    with open('MI_INDEX.json', 'wb') as f:
        f.write(response.content)

    body = munch.munchify(response.json())
    # print(body)

    print(body.data7[0][1])

if __name__ == '__main__':
    getStockData()