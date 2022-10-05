#import required all module
import wikipedia
import pyttsx3 #this module is convert text to speech
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am Jarvis. Please tell me how may I help you")
    
def takeCommand():
    #it takes microphones input and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language="en-In")
        print(f"user said:{query}\n")
    except Exception as e:

        print("Say that again please...")
        return "none"
    return query
  
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sender_email@gmail.com','password')
    server.sendmail('receiver_email@gmail.com',to,content)
    server.close()
    
if __name__ == "__main__":wishMe()
while True:
    query = takeCommand().lower()
#logic for executing tasks based on query
    if "wikipedia" in query:
        speak('Searching Wikipedia...please wait')
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query, sentences=2)
        speak("Acording to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("satckoverflow.com")

    elif 'open facebook' in query:
        webbrowser.open("facebook.com")

    elif 'open instagram' in query:
        webbrowser.open("instagram.com")

    elif 'open twitter' in query:
        webbrowser.open("twitter.com")

    elif 'play song' in query:
        music_dir= "C:\\Users\\91761\\Desktop\\Music"
        songs=os.listdir(music_dir)
        os.startfile(os.path.join(music_dir,songs[0]))

    elif 'tell me the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif 'open my photo' in query:
        codePath="C:\\Users\\91761\\Desktop\\myphoto"
        os.startfile(codePath)
            
    elif 'play video songs' in query:
        videosongs_dir="C:\\Users\\91761\\Desktop\\video songs"
        video_songs=os.listdir(videosongs_dir)
        os.startfile(os.path.join(videosongs_dir,video_songs[0]))

    elif 'open whatsapp' in query:
        codepath ="C:\\Users\\91761\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
        os.startfile(codepath)

    elif 'open chrome browser' in query:
        codepath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(codepath)
            
    elif 'open notepad' in query:
        codepath="C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
        os.startfile(codepath)

    elif 'E-mail to Shibu' in query:
        try:
            speak("What should I say?")
            content=takeCommand()
            to = "shibuji1430@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent!")

        except Exception as e:
            print(e)
            speak("sorry my friend Durjendra. i am not able to send this email")
                
    if 'stop' in query:
        speak('ok sir...bye sir...take care')
        break
