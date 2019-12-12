# This is a voice-output interface for CleverBot, a chatbot.
# Needs python3, cleverwrap and flite chattyto run
# python should be present in a unix terminal
#
# pip install cleverwrap
# sudo apt-get install flite
#
# Usage:
# python chatBot.py
# then just type after the > prompt
# to leave, type > I'm leaving
##

from cleverwrap import CleverWrap
chatBot = CleverWrap("CC6zkRgO9TPlPcz6AO_zLCunNBg")
import subprocess
import sys
import os
from googletrans import Translator
shell = True
#chatBot.reset()

def speak(this):
    print('- '+str(this))
    #subprocess.run(['flite', '-voice', 'file://cmu_us_aew.flitevox', '-t', str(this)])
    gg = "say %s"%(str(this))
    os.system(gg)

#speak("I\\'m listening")
tmp = 'Hi'
translator = Translator()
var = translator.translate(tmp, src='zh-tw', dest='en').text

chatting = True
while chatting == True:
        if(var == 'I\'m leaving'):
            chatting = False
            break
        reply = chatBot.say(str(var))
        reply = translator.translate(reply, src='en', dest='zh-tw').text
        speak(reply)
        #tmp = input('> ')
        tmp = reply
        var = translator.translate(tmp, src='zh-tw', dest='en').text

speak("Fine, leave. See if I care.")
