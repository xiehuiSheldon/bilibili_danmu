# -*- coding:utf-8 -*-
import requests #网络请求
import time
import random
import configparser

#定义类
class SendDanMu:
    #构造函数
    def __init__(self):    #self相当于this？
        self.url = 'https://api.bilibili.com/x/v2/dm/post'
        self.cookies = {
            'Cookie':'finger=cabe3269; buvid3=CD00DA07-30C7-46E2-AE32-0A059EF44797557infoc; LIVE_BUVID=AUTO2315303505577418; sid=8wk970na; DedeUserID=300053329; DedeUserID__ckMd5=0ff338466b750653; SESSDATA=8855607d%2C1532942578%2Cd8153f52; bili_jct=178fdc2fbdec26f18b74b3216258c9b0; rpdid=mwmqqikmodoskwksooiw; fts=1530351436; _dfcaptcha=4f9a336fc995266c893b6204b40a7d02'
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        }
    #发送弹幕
    def sendDM(self,datax): #所有函数的第一个参数都是self,要写
        self.html = requests.post(
            self.url,
            data = datax,
            cookies = self.cookies,
            headers = self.headers
        )
        print(self.html)

senddanmu = SendDanMu()
target = configparser.ConfigParser()
target.read('myconfig.ini')
while(True):
    message = target['my_danmu'][str(random.randint(1,10))]
    data = {
        'aid':'25874220',
        'color':'16777215',
        'csrf':'178fdc2fbdec26f18b74b3216258c9b0',
        'fontsize':'25',
        'mode':'1',
        'msg':message,
        'oid':'44232234',
        'plat':'1',
        'pool':'0',
        'progress':str(random.randint(1000,120000)),
        'rnd':str(int(time.time()*1000000)),
        'type':'1'
    }
    senddanmu.sendDM(data) #<Response [200]> 200是状态码 表示pass
    time.sleep(5.5)