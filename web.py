from googlesearch import search 
from webbot import Browser
import speech_recognition as sr
from gtts import gTTS

USER_NAME = 'Abhishek'

def my_query():
    query = 'please open amazon website'
    speech = gTTS(text = query, lang = 'en', slow = False)
    speech.save("my_query.wav")

def speech_recognition(source = 'my_query.wav'):
    rec = sr.Recognizer()
    audio = sr.AudioFile(source)
    print('Listening your query...')
    with audio as source:
        audio = rec.record(source)
        try:   
            text = rec.recognize_google(audio, language = 'en-US', show_all = True)
            print(text[0]['transcript'])
            return text['alternative'][0]['transcript']
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None

def text_to_speech(text, lang = 'en', slow = False):
    speech = gTTS(text = text, lang = lang, slow = slow)
    return speech

def open_web_page(url):
    web = Browser()
    web.go_to(url)
    web.press(web.Key.ENTER)
    return web

def google_search(query , results = 1):
    urls = [url for url in search(query, tld="co.in", num=results, stop=results, pause=2)]
    return urls
