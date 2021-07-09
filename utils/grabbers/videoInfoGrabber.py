# -*-coding:utf-8-*-
from bilibili_api import video, exceptions
import asyncio


async def main_av(vid: int):
    v = video.Video(aid=vid)
    # 获取信息
    info = await v.get_info()
    return info


async def main_bv(vid: str):
    v = video.Video(bvid=vid)
    # 获取信息
    info = await v.get_info()
    return info


def get_video_info(vid: str) -> list:
    error_return = ['未找到该视频相关信息，请检查视频ID是否正确和网络连接是否正常', '未知', 0, 0, 0, 0, 0, vid]
    try:
        if vid.lower().startswith('av'):
            info = asyncio.get_event_loop().run_until_complete((main_av(int(vid.replace(vid[0:2], '')))))
            vid = vid.lower()
        else:
            vid = 'BV{}'.format(vid.replace(vid[0:2], ''))
            info = asyncio.get_event_loop().run_until_complete(main_bv(vid))

        # 返回信息
        return_list = [
            info['title'],
            info['owner']['name'],
            info['stat']['view'],
            info['stat']['like'],
            info['stat']['favorite'],
            info['stat']['danmaku'],
            info['stat']['reply'],
            vid
        ]
        return return_list

    except exceptions.ArgsException:
        return error_return
    except exceptions.ResponseCodeException:
        return error_return


if __name__ == '__main__':
    print(get_video_info('av10496'))
