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
            result = []
            if key[0:2] in ['av', 'AV', 'bv', 'BV', 'cv', 'CV', 'au', 'AU', 'ss', 'SS'] and len(key.replace(' ', '')) > 2:
                if key[0:2] in ['av', 'AV', 'bv', 'BV']:
                    result.append(
                    {
                        "Title": "直接打开视频",
                        "SubTitle": f'''直接打开视频 {key}''',
                        "IcoPath": "bili.ico",
                        "ContextData": "ctxData",
                        "JsonRPCAction":{
                            'method': 'OpenPage',
                            'parameters': [f'https://www.bilibili.com/video/{key}'],
                            'dontHideAfterAction': False
                        }
                    }
                    )
                elif key[0:2] in ['cv', 'CV']:
                    result.append(
                    {
                        "Title": "直接打开专栏",
                        "SubTitle": f'''直接打开专栏 {key}''',
                        "IcoPath": "bili.ico",
                        "ContextData": "ctxData",
                        "JsonRPCAction":{
                            'method': 'OpenPage',
                            'parameters': [f'https://www.bilibili.com/read/{key}'],
                            'dontHideAfterAction': False
                        }
                    }
                    )
                elif key[0:2] in ['au', 'AU']:
                    result.append(
                    {
                        "Title": "直接打开音频",
                        "SubTitle": f'''直接打开音频 {key}''',
                        "IcoPath": "bili.ico",
                        "ContextData": "ctxData",
                        "JsonRPCAction":{
                            'method': 'OpenPage',
                            'parameters': [f'https://www.bilibili.com/audio/{key}'],
                            'dontHideAfterAction': False
                        }
                    }
                    )
                elif key[0:2] in ['ss', 'SS']:
                    result.append(
                    {
                        "Title": "直接打开剧集",
                        "SubTitle": f'''直接打开剧集 {key}''',
                        "IcoPath": "bili.ico",
                        "ContextData": "ctxData",
                        "JsonRPCAction":{
                            'method': 'OpenPage',
                            'parameters': [f'https://www.bilibili.com/bangumi/play/{key}'],
                            'dontHideAfterAction': False
                        }
                    }
                    )
            result.append(
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
            )
        return result

    def OpenPage(self, url):
        webbrowser.open(url)
        WoxAPI.change_query(url)

if __name__ == '__main__':
    Main()