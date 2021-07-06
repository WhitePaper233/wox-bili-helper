# -*-coding:utf-8-*-
def generate_normal_result(title, subtitle, prefix, suffix='') -> dict:
    dictionary = {
        "Title": title,
        "SubTitle": subtitle,
        "IcoPath": "icons/bili.ico",
        "ContextData": "ctxData",
        "JsonRPCAction": {
            'method': 'open_page',
            'parameters': ['https://{}.bilibili.com/{}'.format(prefix, suffix)],
            'dontHideAfterAction': False
        }
    }
    return dictionary


def generate_search_result(key) -> dict:
    dictionary = {
        "Title": "搜索:{}".format(key),
        "SubTitle": '''在bilibili.com上搜索"{}"的结果'''.format(key),
        "IcoPath": "icons/search.ico",
        "ContextData": "ctxData",
        "JsonRPCAction": {
            'method': 'open_page',
            'parameters': ['https://search.bilibili.com/all?keyword={}'.format(key)],
            'dontHideAfterAction': False
        }
    }
    return dictionary


def generate_video_result(*args) -> dict:
    """
    :param args:{
                [0]: title
                [1]: up's name
                [2]: view
                [3]: like
                [4]: favorite
                [5]: danmaku
                [6]: reply
                [7]: aid or bvid
    :return: search result
    """
    args = args[0]
    dictionary = {
        "Title": args[0],
        "SubTitle": '''UP主:{}  播放:{}  点赞:{}  收藏:{}  弹幕:{}  评论:{}'''.format
        (args[1], args[2], args[3], args[4], args[5], args[6]),
        "IcoPath": "icons/bili.ico",
        "ContextData": "ctxData",
        "JsonRPCAction": {
            'method': 'open_page',
            'parameters': ['https://www.bilibili.com/video/{}'.format(args[7])],
            'dontHideAfterAction': False
        }
    }
    return dictionary


def generate_article_result(*args) -> dict:
    """
    :param args:{
                [0]: title
                [1]: up's name
                [2]: view
                [3]: favorite
                [4]: like
                [5]: reply
                [6]: share
                [7]: coin
                [8]: aid or bvid
    :return: search result
    """
    args = args[0]
    dictionary = {
        "Title": args[0],
        "SubTitle": '''UP主:{}  浏览:{}  收藏:{}  点赞:{}  回复:{}  分享:{}  投币'''.format
        (args[1], args[2], args[3], args[4], args[5], args[6], args[7]),
        "IcoPath": "icons/bili.ico",
        "ContextData": "ctxData",
        "JsonRPCAction": {
            'method': 'open_page',
            'parameters': ['https://www.bilibili.com/read/{}'.format(args[8])],
            'dontHideAfterAction': False
        }
    }
    return dictionary


def generate_audio_result(*args) -> dict:
    """
    :param args:{
                [0]: title
                [1]: up's name
                [2]: author
                [3]: view
                [4]: favorite
                [5]: comment
                [6]: share
                [7]: aid or bvid
    :return: search result
    """
    args = args[0]
    dictionary = {
        "Title": args[0],
        "SubTitle": '''UP主:{}  歌手:{}  播放:{}  收藏:{}  评论:{}  分享:{}'''.format
        (args[1], args[2], args[3], args[4], args[5], args[6]),
        "IcoPath": "icons/bili.ico",
        "ContextData": "ctxData",
        "JsonRPCAction": {
            'method': 'open_page',
            'parameters': ['https://www.bilibili.com/audio/{}'.format(args[7])],
            'dontHideAfterAction': False
        }
    }
    return dictionary


if __name__ == '__main__':
    print(generate_search_result(key='av10492'))
