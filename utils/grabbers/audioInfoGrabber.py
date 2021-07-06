# -*-coding:utf-8-*-
from bilibili_api import audio, sync, exceptions


def main(auid: int):
    au = audio.Audio(auid=auid, credential=None)
    # 获取信息
    info = sync(au.get_info())
    return info


def get_audio_info(auid):
    error_return = ['未找到该专栏相关信息，请检查音频ID是否正确和网络连接是否正常', '未知', '未知', 0, 0, 0, 0]
    try:
        info = main(auid)
        # 返回信息
        return_list = [
            info['title'],
            info['uname'],
            info['author'],
            info['statistic']['play'],
            info['statistic']['collect'],
            info['statistic']['comment'],
            info['statistic']['share']
        ]
        return return_list

    except exceptions.ArgsException:
        return error_return
    except exceptions.ResponseCodeException:
        return error_return


if __name__ == '__main__':
    print(get_audio_info(2366706))
