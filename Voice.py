# imports
from gtts import gTTS
import playsound
import os

def speak(text, language, filename):
    tts = gTTS(text=text, lang=language)
    ps = playsound.playsound
    # save speech
    tts.save(filename)
    # play speech
    ps(filename)
    # remove mp3 file to avoid errors
    os.remove("filename")
