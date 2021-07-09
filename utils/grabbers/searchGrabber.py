import requests
from utils.grabbers.videoInfoGrabber import get_video_info
from utils.generators.resultGenerator import GetResult
import threading


class SearchGrabber:
    @staticmethod
    def get_search_result(keyword: str, search_scope: str = 'all', search_type: str = 'video',
                          page: str = '1', order: str = 'default', length: int = 5) -> list:
        """
        :param keyword: 搜索关键字
        :param search_scope: 搜索分区范围
        :param search_type: 搜索类型（未知参数）
        :param page: 搜索页面
        :param order: 搜索排序
        :param length: 所搜数量
        :return: 搜索结果
        """
        if search_scope == 'all':
            try:
                response = requests.get('https://api.bilibili.com/x/web-interface/search/type?&page={}'
                                        '&order={}&keyword={}&search_type={}'.format(page, order, keyword, search_type))
                response_ctx = response.json()
                if bool(response_ctx['code']) is False:
                    return_list = []

                    def format_result(response_result):
                        return_list.extend(GetResult.generate_video_result(get_video_info(
                            response_result['arcurl'].replace('http://www.bilibili.com/video/', ''))))

                    i = 0
                    try:
                        for result in response_ctx['data']['result']:
                            i += 1
                            if i <= length:
                                thread = threading.Thread(target=format_result(result))
                                thread.start()
                        return return_list
                    except KeyError:
                        return []

                else:
                    return []

            except requests.exceptions.Timeout:
                return []


if __name__ == '__main__':
    print(SearchGrabber.get_search_result(keyword='asdasdawedsafafa'))
