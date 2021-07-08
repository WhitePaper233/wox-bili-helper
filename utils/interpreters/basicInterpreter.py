# -*-coding:utf-8-*-
from utils.interpreters import idInterpreter, commandInterpreter
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
            return GetResult.generate_search_result(key)
            # TODO: Command interpret

        elif key[0:2].lower() not in ['av', 'bv', 'cv', 'au', 'ss']:
            # Regular Search
            return GetResult.generate_search_result(key)

        else:
            result = idInterpreter.IDInterpreter.id_interpreter(key)
            result.extend(GetResult.generate_search_result(key))
            return result


if __name__ == '__main__':
    print(BasicInterpreter.interpret('cv4890667'))
