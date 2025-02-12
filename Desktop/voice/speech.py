
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
from datetime import date
def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
def speak(audio):
  engine.say(audio)
  engine.runAndWait()
def wishme(datetime):
  hour=int(datetime.datetime.now().hour)
  if hour>=0 and hour <=12:
    speak("Good Morning")
  elif hour>12 and hour <=18:
    speak("Good Afternoon") 
  else:
    speak("Good Evening")  
def takecommand():
  r=sr.Recognizer()
  speak('Hello.....How Can I Help You ? Speak now')
  with sr.Microphone() as source:
    print("Listening.....")
    r.pause_threshold = 1
    audio = r.listen(source)
  try:
    print("Recognizing.......")  
    query=r.recognize_google(audio,language="en-in")
    print("user said: ",query)
  except Exception as e:
    print(e)
    speak("say that again please......")
    return "none"
  return query

wishme(datetime)
query=takecommand().lower()
if 'wikipedia' in query:
  speak("searching wikipedia....please wait")
  query=query.replace("wikipedia","")
  results=wikipedia.summary(query)
  speak("According to wikipedia")
  print(results)
elif 'open youtube' in query:
  webbrowser.open("youtube.com")
elif 'open wikipedia' in query:
  webbrowser.open("wikipedia.com")
elif 'command' in query:
  os.open('start cmd',flags=10)
elif 'age' in query:
  print('Enter year : ')
  y=int(input())
  print('enter month : ')
  m=int(input())
  print('Enter date  : ')
  d=int(input())

  ag=age(date(y,m,d))
  print('Your age : ')
  print(ag)