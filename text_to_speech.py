from gtts import gTTS

import os

myText1 = "text to speech conversion using python and gTTS"
fh = open("sample.text","r")
myText = fh.read().replace("\n"," ")

language = 'en'

output = gTTS(text=myText,lang = language,slow=False)
output.save("output.mp3")
fh.close()
os.system("start output.mp3")