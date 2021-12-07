import time
import requests
import re
import urllib.parse as UP
import util

def getChinaTimesComments(url):
    # get response
    response = util.getResponse(url, getChinaTimesComments.__name__)

    with open('CTcomments.html', 'wb') as f:
        f.write(response.content)
    
    html = response.text
    lines = html.split('\n')
    script = lines[-1]

    parts = script.split('constructAndRenderComponentIntoComment_DO_NOT_USE')
    script = parts[1]
    parts = script.split('NavigationMetrics')
    script = parts[0]
    
    script = script[77:-4]

    print(script)

def getChinaTimesNews(url):
    # response = util.getResponse(url, getChinaTimesNews.__name__)

    # time.sleep(2)

    # with open('chinaTimesNews.html', 'wb') as f:
    #     f.write(response.content)

    with open('chinaTimesNews.html', 'r', encoding='utf-8') as f:
        html = f.read()

    m = re.search(r"appId: '(?P<appid>\d+)'", html)
    appid = m.group('appid')

    fb_url = (
        f'https://www.facebook.com/plugins/feedback.php?'
        f'app_id={appid}&'
        f'channel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df34068c4a96c774%26domain%3Dwww.chinatimes.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.chinatimes.com%252Ff396fd39f5bb6f%26relation%3Dparent.parent&'
        f'container_width=924&height=100&'
        f'href={UP.quote(url)}&'
        f'locale=zh_TW&numposts=5&order_by=reverse_time&sdk=joey&version=v3.2&width'
    )
    # print(fb_url)
    getChinaTimesComments(fb_url)

if __name__ == '__main__':
    url = 'https://www.chinatimes.com/realtimenews/20211205001412-260407?chdtv'
    getChinaTimesNews(url)