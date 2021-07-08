# -*-coding:utf-8-*-
from bilibili_api import article, exceptions
import asyncio


async def main(aid: int):
    a = article.Article(cvid=aid)
    # 获取信息
    info = await a.get_info()
    return info


def get_article_info(aid: str):
    error_return = ['未找到该专栏相关信息，请检查专栏ID是否正确和网络连接是否正常', '未知', 0, 0, 0, 0, 0, 0, aid.lower()]
    try:
        info = asyncio.get_event_loop().run_until_complete(main(int(aid.replace(aid[0:2], ''))))
        # 返回信息
        return_list = [
            info['title'],
            info['author_name'],
            info['stats']['view'],
            info['stats']['favorite'],
            info['stats']['like'],
            info['stats']['reply'],
            info['stats']['share'],
            info['stats']['coin'],
            aid.lower()
        ]
        return return_list

    except exceptions.ArgsException:
        return error_return
    except exceptions.ResponseCodeException:
        return error_return


if __name__ == '__main__':
    print(main(12032529))
