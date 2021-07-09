# -*-coding:utf-8-*-
import asyncio
from bilibili_api import video, exceptions


def format_result(aid: str) -> list:

    async def get_video_detail(avid: int) -> dict:
        v = video.Video(aid=avid)
        return_info = await v.get_info()
        return return_info

    try:
        info = asyncio.get_event_loop().run_until_complete(get_video_detail(avid=int(aid)))
        return [{
            "Title": info['title'],
            "SubTitle": '''UP主:{}  播放:{}  点赞:{}  收藏:{}  弹幕:{}  评论:{}'''.format
            (info['owner']['name'], info['stat']['view'], info['stat']['like'],
             info['stat']['favorite'], info['stat']['danmaku'], info['stat']['reply']),
            "IcoPath": "icons/bili.ico",
            "ContextData": "ctxData",
            "JsonRPCAction": {
                'method': 'open_page',
                'parameters': ['https://www.bilibili.com/video/av{}'.format(aid)],
                'dontHideAfterAction': False
            }
        }]

    except exceptions.ArgsException:
        return []
    except exceptions.ResponseCodeException:
        return []
