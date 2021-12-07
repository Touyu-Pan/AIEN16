import time
import requests

def getBookData():
    url = 'https://www.books.com.tw/products/0010905287'
    response = requests.get(url)
    if response.status_code != 200:
        print(f'response failed ({response.status_code})')
        return
    print(f'response success')
    time.sleep(1)
    
    with open('books.html', 'wb') as f:
        f.write(response.content)

if __name__ == '__main__':
    getBookData()