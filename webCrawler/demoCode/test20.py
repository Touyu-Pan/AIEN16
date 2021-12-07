import re
import time
import urllib.parse as UP

import requests

def getChinaTimesComments(url):
    pass

def getChinaTimesNews(url):
    # response = requests.get(url)
    # if response.status_code != 200:
    #     print(f'[getChinaTimesNews] response error ({response.status_code})')
    #     return
    # print(f'[getChinaTimesNews] response success')

    # time.sleep(2)

    # with open('chinatimesnews.html', 'wb') as f:
    #     f.write(response.content)

    with open('chinatimesnews.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # appId: '1379575469016080',
    m = re.search(r"appId: '(?P<appid>\d+)'", html)
    appid = m.group('appid')
    print(appid)

    fb_url = (
        f'https://www.facebook.com/plugins/feedback.php?'
        f'app_id={appid}&'
        f'channel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df34068c4a96c774%26domain%3Dwww.chinatimes.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.chinatimes.com%252Ff396fd39f5bb6f%26relation%3Dparent.parent&'
        f'container_width=924&height=100&'
        f'href={UP.quote(url)}&'
        f'locale=zh_TW&numposts=5&order_by=reverse_time&sdk=joey&version=v3.2&width'
    )
    print(fb_url)

    response = requests.get(fb_url)
    if response.status_code != 200:
        return

    time.sleep(2)

    html = response.text

    with open('chinatimescomments1.html', 'wb') as f:
        f.write(response.content)

    lines = html.split('\n')
    script = lines[-1]

    print(script)

    # with open('chinatimescomments.html', 'w', encoding='utf-8') as f:
    #     f.write(script)

    parts = script.split('constructAndRenderComponentIntoComment_DO_NOT_USE')
    script = parts[1]
    parts = script.split('NavigationMetrics')
    script = parts[0]
    
    script = script[77:-4]

    with open('chinatimescomments2.html', 'w', encoding='utf-8') as f:
        f.write(script)

    # <script>requireLazy(["TimeSliceImpl","ServerJS"]

if __name__ == '__main__':
    url = 'https://www.chinatimes.com/realtimenews/20211205001412-260407'
    getChinaTimesNews(url)