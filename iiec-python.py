import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import subprocess
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# change voice (voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hii, How may I help you")     
  

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(whom, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('18erecs013.ashish@rietjaipur.ac.in', 'Ashrad99!')
    server.sendmail('18erecs013.ashish@rietjaipur.ac.in', whom, content)
    server.close()

def remove(string): 
    return string.replace(" ", "")

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play tv series' in query:
            music_dir = 'F:/entertainment/tv series/12 Monkeys/s1'# put you music dir here
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"the time is {strTime}")

        elif 'run command' in query:
            speak("what you want to run")
            app = remove(takeCommand())
            x = subprocess.getoutput("start"+" "+"/MIN"+" "+app)

        elif 'run docker' in query:
            webbrowser.open("commands.html")

        elif 'linux command' in query:
            webbrowser.open("commands.html")
            

        elif 'send mail' in query:
            try:
                speak("Email Please")
                whom = remove(takeCommand())
                speak("What should I say?")
                content = takeCommand()   
                sendEmail(whom, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("There is some issue Try manually")   



