# -*-coding:utf-8-*-
from utils.interpreters import idInterpreter, commandInterpreter
from utils.grabbers.searchGrabber import SearchGrabber
from utils.generators.resultGenerator import *


class BasicInterpreter:
    @staticmethod
    def interpret(key: str):
        if key == '':
            # The default frequently-used pages
            # TODO: Customize pages
            return_list = GetResult.generate_normal_result('首页', '打开Bilibili首页', 'www')
            return_list.extend(GetResult.generate_normal_result('动态', '打开Bilibili动态页', 't'))
            return_list.extend(GetResult.generate_normal_result('个人主页', '打开Bilibili个人主页', 'space'))
            return_list.extend(GetResult.generate_normal_result('直播', '打开Bilibili直播页', 'live'))
            return_list.extend(GetResult.generate_normal_result('漫画', '打开Bilibili漫画', 'manga'))
            return return_list

        elif key.startswith('-'):
            return_list = GetResult.generate_search_result(key)
            return_list.extend(SearchGrabber.get_search_result(keyword=key))
            return return_list
            # TODO: Command interpret

        elif key[0:2].lower() not in ['av', 'bv', 'cv', 'au', 'ss'] or key.lower() in ['av', 'bv', 'cv', 'au', 'ss']:
            # Regular Search
            return_list = GetResult.generate_search_result(key)
            return_list.extend(SearchGrabber.get_search_result(keyword=key))
            return return_list

        else:
            return_list = idInterpreter.IDInterpreter.id_interpreter(key)
            return_list.extend(GetResult.generate_search_result(key))
            return_list.extend(SearchGrabber.get_search_result(keyword=key))
            return return_list


if __name__ == '__main__':
    print(BasicInterpreter.interpret('av1'))
