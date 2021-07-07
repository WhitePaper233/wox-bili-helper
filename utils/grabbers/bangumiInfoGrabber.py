# -*-coding:utf-8-*-
from bilibili_api import bangumi, sync, exceptions


def main(ssid: int):
    # 获取信息
    info = sync(bangumi.get_overview(season_id=ssid))
    return info


def get_bangumi_info(ssid: int):
    error_return = ['未找到该剧集的相关信息，请检查音频ID是否正确和网络连接是否正常', 0, 0, 0, 0, 0, 0, ssid]
    try:
        info = main(ssid)
        # 返回信息
        return_list = [
            info['title'],
            info['total'],
            info['stat']['views'],
            info['stat']['coins'],
            info['stat']['danmakus'],
            info['stat']['favorites'],
            info['stat']['reply'],
            info['stat']['share'],
            ssid
        ]
        return return_list

    except exceptions.ArgsException:
        return error_return
    except exceptions.ResponseCodeException:
        return error_return


if __name__ == '__main__':
    print(get_bangumi_info(5800))
