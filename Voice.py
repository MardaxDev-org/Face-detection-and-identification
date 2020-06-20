# imports
from gtts import gTTS
import playsound


def speak(text, language):
    tts = gTTS(text=text, lang=language)
    ps = playsound.playsound
    filename = 'speak.mp3'
    # save speech
    tts.save(filename)
    # play speech
    ps(filename)
