#coding=utf-8
'''
教程：
先安装无违规包,在终端执行：pip install --index-url https://test.pypi.org/simple/ --no-deps wwg
安装发送请求包，在终端执行：pip install requests
'''
from wwg.setting import *
import requests
import time

s = requests.session()
wwgxiahao()

pingtai = {
    "QQ": "QQ",
    "wx": "微信",
}

while True:
    user_input = input("请输入要举报账号的平台(QQ/wx)：")
    if user_input in pingtai:
        # 2  ==> weekdays["2"]
        hao = input(f"请输入要举报的{user_input}号：")
        print("请核实账号:", hao)
        print("举报中")
        '''
        res2 = s.post(
            
            url="http://jubao.qq.com/index.php",
            headers={
                'Host': 'jubao.qq.com:80',
                'Content-Length': '1384',
                'Cache-Control': 'max-age=0',
                'sec-ch-ua': '"Chromium";v="103", ".Not/A)Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Upgrade-Insecure-Requests': '1',
                'Origin': 'http://jubao.qq.com:80',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Referer': 'http://jubao.qq.com:80',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
            },
        )
'''
        time.sleep(1)
        print("已提交")
        break
    elif user_input == "0":
        break
    else:
        print("输入错误,只能输入QQ/wx")
