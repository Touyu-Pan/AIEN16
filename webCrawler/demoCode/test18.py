import json
import os.path
import time

import chardet
import munch
import pyquery
import requests

def getAppleDailyNews(url):
    response = requests.get(url, headers={
        'referer': 'https://tw.appledaily.com/home/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    })
    if response.status_code != 200:
        print(f'[getAppleDailyNews] response error ({response.status_code})')
        return
    print(f'[getAppleDailyNews] response success')

    time.sleep(2)

    with open('appledailynews.html', 'wb') as f:
        f.write(response.content)

    encoding = 'utf-8'
    res = munch.munchify(chardet.detect(response.content))
    if res.confidence >= 0.7:
        encoding = res.encoding
    if encoding.lower() == 'big-5':
        encoding = 'big5'

    html = response.content.decode(encoding)

    # 取出 script 標籤裡的資料，因為內文放在這裡面的 JS 程式碼
    doc = pyquery.PyQuery(html)
    script = doc('script#fusion-metadata')
    # 使用 .html() 的原因是因為 .text() 會忽略 <!-- ... --> 這種 HTML 註解的內容
    script = script.html()
    
    with open('appledailynews.js', 'w', encoding='utf-8') as f:
        f.write(script)

    # 我們發現資料所在的程式碼區段被 Fusion.globalContent 包夾
    # Fusion.globalContent = {
    #     ...  // 我們要的文章內容在此處
    # };
    # Fusion.globalContentConfig = { 
    # 所以我們用 Fusion.globalContent 作為 split 的目標
    parts = script.split('Fusion.globalContent')
    # 切完之後，我們的資料在中間這一段，然後用 slice 去掉頭尾的 = 和 ;
    script = parts[1][1:-1]
    
    with open('appledailynews1.js', 'w', encoding='utf-8') as f:
        f.write(script)

    # 剩下的 JS 程式碼就是 JSON 格式，因此將其用 json.loads 進行解析
    data = munch.munchify(json.loads(script))
    for content_element in data.content_elements:
        # 廣告內容都不會是 type: "text"
        if content_element.type == 'text':
            print(content_element.content)
        if content_element.type == 'image':
            # 取出圖檔 URL
            img_url = content_element.additional_properties.originalUrl
            print(img_url)
            # 下載圖檔
            img_response = requests.get(img_url)
            if img_response.status_code != 200:
                print(f'[getAppleDailyNews.Image] response error ({img_response.status_code})')
                # 這裡用 continue，因為圖檔無法抓可能只是單檔問題，不代表其他圖檔或內文有誤，所以用 continue 繼續處理其他區塊
                continue
            print(f'[getAppleDailyNews.Image] response success')

            time.sleep(2)

            # 取出圖檔 URL 末端的檔名
            filename = os.path.basename(img_url)
            # 保存圖檔，記得圖檔是二進位資料，所以要用 b(inary) 模式寫檔
            with open(filename, 'wb') as f:
                f.write(img_response.content)

def getAppleDailyNewsList():
    url = 'https://tw.appledaily.com/realtime/new/'
    response = requests.get(url, headers={
        'referer': 'https://tw.appledaily.com/home/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    })
    if response.status_code != 200:
        print(f'[getAppleDailyNewsList] response error ({response.status_code})')
        return
    print(f'[getAppleDailyNewsList] response success')

    time.sleep(2)

    with open('appledailynewslist.html', 'wb') as f:
        f.write(response.content)

    encoding = 'utf-8'
    res = munch.munchify(chardet.detect(response.content))
    if res.confidence >= 0.7:
        encoding = res.encoding
    if encoding.lower() == 'big-5':
        encoding = 'big5'

    html = response.content.decode(encoding)

    doc = pyquery.PyQuery(html)
    cards = list(doc('div.stories-container a.story-card').items())
    for card in cards:
        title = card('span.headline').text()
        link = card.attr('href')
        link = f'https://tw.appledaily.com{link}'
        print(f'標題：{title}')
        print(f'連結：{link}')
        getAppleDailyNews(link)

if __name__ == '__main__':
    getAppleDailyNewsList()