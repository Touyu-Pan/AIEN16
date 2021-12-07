import requests

# device fingerprint: 4yHGjRm2HvU5SML5937Srw==|GrMd2PEQHZPBVBJo6L88o4qv3L9e1NMTxawhQuO572RTP+Mp9M2pxPm3j4AgS0L9l5K+HTrCku6x4fVAXg==|P2YhbwTC7LPeubTX|03|3
# password: dfd65117f5a90cf87c1664e5f6db4d68b2d1e70e6bc2e96f9a5e40e995b0c066

# support_ivs: true
# support_whats_app: true
# username: "erinus"

response = requests.post(
    'https://shopee.tw/api/v2/authentication/login',
    headers={
        'cookie': '_gcl_au=1.1.609654435.1638757694; _med=refer; csrftoken=IhgDaOUTvdLfSuBZZhDG57y4TPnGZdZV; SPC_IA=-1; SPC_EC=-; SPC_U=-; SPC_F=fYO9vYzNpBBB0dzNUYEgeN8w3IBLNDMK; REC_T_ID=29ac4cee-563c-11ec-b08d-fe8def7c1c54; SPC_SI=mall.vr7UqXBhA85lkzE3vRTaNWbaLwZVta32; _fbp=fb.1.1638757694327.903406801; __BWfp=c1638757694899xea9765ad5; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.991139033.1638757695; _gid=GA1.2.40699313.1638757695; cto_bundle=du9Yw18xUkxmYXJMbCUyQk1vUXlHdHYlMkZicUpHcTN3ZmhCSkV3amtjNUJSMlhXZmpxbVlFJTJCWGVqdGxqVWg0RW16UTU0M3olMkJYaVRWWEJvMk5BeDhoSWN2VWJNOFlUaUV4UlQ5S0tRZmFBTEUxM2I3UlJNYmVhdVZUQTU3TVpFcmR6cUhtaXJaYWFrNEhFSmUzSUNPWXZ4eGNsNyUyRkFBJTNEJTNE; _QPWSDCXHZQA=fe5c9cea-c19d-402b-8aff-48482aa51529; G_ENABLED_IDPS=google; shopee_webUnique_ccd=4yHGjRm2HvU5SML5937Srw%3D%3D%7CGrMd2PEQHZPBVBJo6L88o4qv3L9e1NMTxawhQuO572RTP%2BMp9M2pxPm3j4AgS0L9l5K%2BHTrCku6x4fVAXg%3D%3D%7CP2YhbwTC7LPeubTX%7C03%7C3; SPC_CLIENTID=ZllPOXZZek5wQkJCmuxrslwksfvnvgsz; SPC_T_ID=omwki56y1/IinsVzql7jp7OrbhNyIOxF0qsbqQvNT5EB7MqOhgdzVQIsT/zMzbEW+EesuSHEnDu+m+/1VaaxYIy88UJDdzKuA5hinbsIFUw=; SPC_T_IV=M6rTprJEysdCTMTTBHD6Zw==; _ga_RPSBE3TQZZ=GS1.1.1638760335.2.1.1638760336.59; SPC_R_T_ID="z+b7OoKIq7UOz3oavjHOTRZAdkihd+RRWlpaoOjVfFq74+ZC6uNqBrQzP4UWPCc/oZ0HaEoivGT3pJ7UxOS4R2cOns/EA36kEUIM/5U4IuA="; SPC_T_IV="mFS/LqGieVdz88S9lnnxFg=="; SPC_R_T_IV="mFS/LqGieVdz88S9lnnxFg=="; SPC_T_ID="z+b7OoKIq7UOz3oavjHOTRZAdkihd+RRWlpaoOjVfFq74+ZC6uNqBrQzP4UWPCc/oZ0HaEoivGT3pJ7UxOS4R2cOns/EA36kEUIM/5U4IuA="',
        'referer': 'https://shopee.tw/buyer/login?next=https%3A%2F%2Fshopee.tw%2F',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'x-api-source': 'pc',
        'x-csrftoken': 'IhgDaOUTvdLfSuBZZhDG57y4TPnGZdZV',
        'x-requested-with': 'XMLHttpRequest',
        'x-shopee-language': 'zh-Hant',
    },
    json={
        'device_sz_fingerprint': '9//wf5q3dC4dBvUD2PR/QQ==|7xvCCD2RoU08dy7JQJqVDh+e38gk+gMwfyq516MwUFPhg4+c8ac8GLl3fnVek5DFs2/zr2coolasL7fBVJux|6gohcsnI9zSoTsKt|03|3',
        'password': 'dfd65117f5a90cf87c1664e5f6db4d68b2d1e70e6bc2e96f9a5e40e995b0c066',
        'support_ivs': 'true',
        'support_whats_app': 'true',
        'username': 'thumbe49555'
    }
)
if response.status_code != 200:
    print(f'response error ({response.status_code})')
    exit()

print(response.text)