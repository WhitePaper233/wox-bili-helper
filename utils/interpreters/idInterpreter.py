# -*-coding:utf-8-*-
from utils.generators.resultGenerator import *
import utils.grabbers.videoInfoGrabber as videoInfo
import utils.grabbers.articleInfoGrabber as articleInfo
import utils.grabbers.audioInfoGrabber as audioInfo
import utils.grabbers.bangumiInfoGrabber as bangumiInfo


class IDInterpreter:
    @staticmethod
    def id_interpreter(key: str) -> list:
        prefix = key[0:2].lower()

        if prefix == 'av' and key.replace(key[0:2], '').isdecimal() \
                or prefix == 'bv' and ' ' not in key.replace(key[0:2], '', 1) and len(key) >= 3:
            # Advanced searching by using aid
            return GetResult.generate_video_result(videoInfo.get_video_info(key))

        elif prefix == 'cv' and key.replace(key[0:2], '').isdecimal():
            # Advanced searching by using cid
            return GetResult.generate_article_result(articleInfo.get_article_info(key))

        elif prefix == 'au' and key.replace(key[0:2], '').isdecimal():
            # Advanced searching by using cid
            return GetResult.generate_audio_result(audioInfo.get_audio_info(key))

        elif prefix == 'ss' and key.replace(key[0:2], '').isdecimal():
            # Advanced searching by using ssid
            return GetResult.generate_bangumi_result(bangumiInfo.get_bangumi_info(key))

        else:
            return []


if __name__ == '__main__':
    print(IDInterpreter.id_interpreter('cv'))
