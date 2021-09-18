from gtts import gTTS
import os, pyglet, time

def playAudio(audioText):
    print(audioText)
    try:
        tts = gTTS(audioText, lang='en')
        filename = 'temp.mp3'
        tts.save(filename)

        audio = pyglet.media.load(filename, streaming=False)
        audio.play()

        time.sleep(audio.duration)
        os.remove(filename)
    
    except Exception:
        print("text to speech audio failure, bcoz of " + Exception)