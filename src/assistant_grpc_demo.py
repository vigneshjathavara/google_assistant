#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google Assistant GRPC recognizer."""

import logging

import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)


def main():
    status_ui = aiy.voicehat.get_status_ui()
    status_ui.status('starting')
    assistant = aiy.assistant.grpc.get_assistant()
    button = aiy.voicehat.get_button()
    with aiy.audio.get_recorder() as recorder:
        while True:
            status_ui.status('ready')
            print('Press the button and speak')
            button.wait_for_press()
            status_ui.status('listening')
            print('Listening...')
            text, audio = assistant.recognize()
            if text is not None:
                if text == 'goodbye':
                    status_ui.status('stopping')
                    print('Bye!')
                    break
                
              
                
                if 'recognize the song' in text:
                    #print('entered')
                    #assistant.stop_conversation()
                    aiy.audio.record_to_wave('/home/pi/acrcloud_sdk_python-master/raspberrypi/python2.7/test1.wav',12)
                    recong_command = "python2 /home/pi/acrcloud_sdk_python-master/raspberrypi/python2.7/test.py /home/pi/acrcloud_sdk_python-master/raspberrypi/python2.7/test1.wav"
                    process = subprocess.Popen(recong_command.split(), stdout=subprocess.PIPE)
                    output = process.stdout.read()
                    output = output[0:-1]
                    #print ('test')
                    res = "".join(map(chr,output))
                    aiy.audio.say('The song is '+ res)
                
                
                print('You said "', text, '"')
            if audio is not None:
                aiy.audio.play_audio(audio)


if __name__ == '__main__':
    main()
