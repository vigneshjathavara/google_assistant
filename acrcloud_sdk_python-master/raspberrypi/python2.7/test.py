#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
    >>> python test.py test.mp3
'''

import os, sys
from acrcloud.recognizer import ACRCloudRecognizer
from acrcloud.recognizer import ACRCloudRecognizeType

if __name__ == '__main__':
    config = {
        'host':'identify-us-west-2.acrcloud.com',
        'access_key':'1f92b35a1fb65c62561e5b6ee758d52a',
        'access_secret':'YmHq3qezDJMHWZ6ZvRMAVQWQa48sKcXWR20svVF1',
        'recognize_type': ACRCloudRecognizeType.ACR_OPT_REC_AUDIO, # you can replace it with [ACR_OPT_REC_AUDIO,ACR_OPT_REC_HUMMING,ACR_OPT_REC_BOTH], The SDK decide which type fingerprint to create accordings to "recognize_type".
        'debug':False,
        'timeout':10 # seconds
    }
    
    '''This module can recognize ACRCloud by most of audio/video file. 
        Audio: mp3, wav, m4a, flac, aac, amr, ape, ogg ...
        Video: mp4, mkv, wmv, flv, ts, avi ...'''
    re = ACRCloudRecognizer(config)
    #print 'test1'
    #recognize by file path, and skip 0 seconds from from the beginning of sys.argv[1].
    res = re.recognize_by_file(sys.argv[1], 0, 10)
    pos_start = res.find("title")
    pos_end = res.find("release_date")
    title = res[pos_start+8:pos_end-3]
    print title
    #print 'test2'
    #buf = open(sys.argv[1], 'rb').read()
    #recognize by file_audio_buffer that read from file path, and skip 0 seconds from from the beginning of sys.argv[1].
    #print re.recognize_by_filebuffer(buf, 0, 10)

