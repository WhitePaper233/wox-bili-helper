# -*-coding:utf-8-*-
from bilibili_api import audio, exceptions
import asyncio


async def main(auid: int):
    au = audio.Audio(auid=auid, credential=None)
    # 获取信息
    info = await au.get_info()
    return info


def get_audio_info(auid: str) -> list:
    error_return = ['未找到该音频的相关信息，请检查音频ID是否正确和网络连接是否正常', '未知', '未知', 0, 0, 0, 0, auid]
    try:
        info = asyncio.get_event_loop().run_until_complete(main(int(auid.replace(auid[0:2], ''))))
        # 返回信息
        return_list = [
            info['title'],
            info['uname'],
            info['author'],
            info['statistic']['play'],
            info['statistic']['collect'],
            info['statistic']['comment'],
            info['statistic']['share'],
            auid
        ]
        return return_list

    except exceptions.ArgsException:
        return error_return
    except exceptions.ResponseCodeException:
        return error_return


if __name__ == '__main__':
    print(get_audio_info(2366706))
