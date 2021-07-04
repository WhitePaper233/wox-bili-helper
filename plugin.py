# encoding=utf8
import webbrowser
from wox import Wox,WoxAPI

class Main(Wox):
    def query(self,key):
        result = [
            {
                "Title": "首页",
                "SubTitle": "打开Bilibili首页",
                "IcoPath": "bili.ico",
                "ContextData": "ctxData",
                "JsonRPCAction":{
                    'method': 'OpenPage',
                    'parameters': ['https://www.bilibili.com/'],
                    'dontHideAfterAction': False
                }
            },
            {
                "Title": "动态",
                "SubTitle": "打开Bilibili动态页",
                "IcoPath": "bili.ico",
                "ContextData": "ctxData",
                "JsonRPCAction":{
                    'method': 'OpenPage',
                    'parameters': ['https://t.bilibili.com/'],
                    'dontHideAfterAction': False
                }
            },
            {
                "Title": "主页",
                "SubTitle": "打开Bilibili个人主页",
                "IcoPath": "bili.ico",
                "ContextData": "ctxData",
                "JsonRPCAction":{
                    'method': 'OpenPage',
                    'parameters': ['https://space.bilibili.com/'],
                    'dontHideAfterAction': False
                }, 
            },
            {
                "Title": "直播",
                "SubTitle": "打开Bilibili直播页",
                "IcoPath": "bili.ico",
                "ContextData": "ctxData",
                "JsonRPCAction":{
                    'method': 'OpenPage',
                    'parameters': ['https://live.bilibili.com/'],
                    'dontHideAfterAction': False
                }
            },
            {
                "Title": "漫画",
                "SubTitle": "打开Bilibili漫画",
                "IcoPath": "bili.ico",
                "ContextData": "ctxData",
                "JsonRPCAction":{
                    'method': 'OpenPage',
                    'parameters': ['https://manga.bilibili.com/'],
                    'dontHideAfterAction': False
                }
            }
        ]
        if key != '':
            result = [
            {
                "Title": "搜索",
                "SubTitle": f'''Bilibili搜索"{key}"的结果''',
                "IcoPath": "search.ico",
                "ContextData": "ctxData",
                "JsonRPCAction":{
                    'method': 'OpenPage',
                    'parameters': [f'https://search.bilibili.com/all?keyword={key}'],
                    'dontHideAfterAction': False
                }
            }
            ]
        return result

    def OpenPage(self, url):
        webbrowser.open(url)
        WoxAPI.change_query(url)

if __name__ == '__main__':
    Main()