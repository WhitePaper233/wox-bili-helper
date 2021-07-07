# -*-coding:utf-8-*-
from utils.interpreters import idInterpreter, commandInterpreter
from utils.generators.resultGenerator import *


class BasicInterpreter:
    @staticmethod
    def interpret(key: str):
        if key == '':
            return [
                # The default frequently-used pages
                # TODO: Customize pages
                generate_normal_result('首页', '打开Bilibili首页', 'www'),
                generate_normal_result('动态', '打开Bilibili动态页', 't'),
                generate_normal_result('个人主页', '打开Bilibili个人主页', 'space'),
                generate_normal_result('直播', '打开Bilibili直播页', 'live'),
                generate_normal_result('漫画', '打开Bilibili漫画', 'manga')
            ]

        elif key.startswith('-'):
            return [
                generate_search_result(key)
            ]
            # TODO: Command interpret

        elif key[0:2].lower() not in ['av', 'bv', 'cv', 'au', 'ss']:
            # Regular Search
            return [generate_search_result(key)]

        else:
            prefix = key[0:2].lower()
            result = []
            if prefix == 'av' and key.replace(key[0:2], '').isdecimal():
                # Advanced searching by using aid
                result.append(generate_video_result(idInterpreter.IDInterpreter.id_interpreter(id_type='aid', key=key)))

            elif prefix == 'bv' and ' ' not in key.replace(key[0:2], '') and len(key) >= 3:
                # Advanced searching by using bvid
                result.append(generate_video_result(idInterpreter.IDInterpreter.id_interpreter(id_type='bvid', key=key)))

            elif prefix == 'cv' and key.replace(key[0:2], '').isdecimal():
                # Advanced searching by using cid
                result.append(generate_article_result(idInterpreter.IDInterpreter.id_interpreter(id_type='cvid', key=key)))

            elif prefix == 'au' and key.replace(key[0:2], '').isdecimal():
                # Advanced searching by using auid
                result.append(generate_audio_result(idInterpreter.IDInterpreter.id_interpreter(id_type='auid', key=key)))

            elif prefix == 'ss' and key.replace(key[0:2], '').isdecimal():
                # Advanced searching by using ssid
                result.append(generate_bangumi_result(idInterpreter.IDInterpreter.id_interpreter(id_type='ssid',key=key)))

            result.append(generate_search_result(key))
            return result


if __name__ == '__main__':
    print(BasicInterpreter.interpret('Cv4890667'))
