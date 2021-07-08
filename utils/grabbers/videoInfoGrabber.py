# -*-coding:utf-8-*-
from bilibili_api import video, exceptions
import asyncio


async def main(vid: str):
    if vid.startswith('BV'):
        v = video.Video(bvid=vid)
    else:
        v = video.Video(aid=int(vid))
    # 获取信息
    info = await v.get_info()
    return info


def get_video_info(vid: str):
    error_return = ['未找到该视频相关信息，请检查视频ID是否正确和网络连接是否正常', '未知', 0, 0, 0, 0, 0]
    try:
        info = asyncio.get_event_loop().run_until_complete(main(vid))
        # 返回信息
        return_list = [
            info['title'],
            info['owner']['name'],
            info['stat']['view'],
            info['stat']['like'],
            info['stat']['favorite'],
            info['stat']['danmaku'],
            info['stat']['reply']
        ]
        return return_list

    except exceptions.ArgsException:
        return error_return
    except exceptions.ResponseCodeException:
        return error_return


if __name__ == '__main__':
    print(get_video_info('10496'))
