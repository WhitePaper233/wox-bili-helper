# -*-coding:utf-8-*-
import utils.grabbers.videoInfoGrabber as videoInfo
import utils.grabbers.articleInfoGrabber as articleInfo
import utils.grabbers.audioInfoGrabber as audioInfo
import utils.grabbers.bangumiInfoGrabber as bangumiInfo


class IDInterpreter:
    @staticmethod
    def id_interpreter(id_type: str, key: str):

        if id_type == 'aid':
            # Format aid
            vid = key.replace(key[0:2], '')
            return_list = videoInfo.get_video_info(vid)
            return_list.append(key.lower())
            return return_list

        elif id_type == 'bvid':
            # Format bvid
            vid = 'BV{}'.format(key.replace(key[0:2], ''))
            return_list = videoInfo.get_video_info(vid)
            return_list.append(vid)
            return return_list

        elif id_type == 'cvid':
            # Format cvid
            return_list = articleInfo.get_article_info(key)
            return_list.append(key)
            return return_list

        elif id_type == 'auid':
            # Format auid
            return_list = audioInfo.get_audio_info(key.replace(key[0:2], ''))
            return_list.append(key.lower())
            return return_list

        elif id_type == 'ssid':
            # Format ssid
            return bangumiInfo.get_bangumi_info(int(key.replace(key[0:2], '')))

        else:
            # Throw Error
            return TypeError('No such id_type "{}"'.format(id_type))


if __name__ == '__main__':
    print(IDInterpreter.id_interpreter('ssid', key='ss10'))
