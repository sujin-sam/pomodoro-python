from gtts import gTTS
import os, pyglet, time

def playAudio(audioText):
    print(audioText)
    tts = gTTS(audioText, lang='en')
    filename = 'temp.mp3'
    tts.save(filename)

    audio = pyglet.media.load(filename, streaming=False)
    audio.play()

    time.sleep(audio.duration)
    os.remove(filename)