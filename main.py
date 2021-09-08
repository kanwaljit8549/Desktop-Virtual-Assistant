import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import os
import random
import smtplib 
import webbrowser
import time
import requests

print("Initialising Virtual Assistent")

v= pyttsx3.init('sapi5')  # "v" variable is used to access sapi which is the default voices in the database
voices = v.getProperty('voices')   # accessing the voices 
v.setProperty('voice',voices[0].id)  # accessing voices[0] which is the male voice

# will speak whatever is passed in the function
def speak(text):
    v.say(text)
    v.runAndWait()

# basic greeting
def greeting():
    speak("hello there! how can i help you")

# speech recognition function, will take input as speech
def SI():
    a=sr.Recognizer()       # taken "a" variable as speech recogniser 
    with sr.Microphone() as source:   # "source" will take input of speech from microphone
        print("Listening...")
        audio=a.listen(source)  # here listening will take place
    try:
        print("Recognising...")
        q = a.recognize_google(audio)  # "q" -> query
        print(f">{q}\n")   # printing query given from user
    except Exception as e:   # Exception is handled if anything is wrong with speech or microphone
        print("say that again please")
        q=None  # query is going to automatically will be None to be passed ahead in the function
    return q

#  email function
def email(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email','password')
    server.sendmail('email_from',to,content)
    server.close()

def main():
    speak("Initialising Virtual Assistent")
    greeting()
    ex="start"     # "ex" variable is initialised here so that program does not return error
    while (ex!="exit"):   # loop will be continuous until the value of "ex" variable reaches exit to stop program
        speak("Listening for command")    # checkpoitn when it will listen for real command
        q=SI()
            
        #logic for hi/hello
        if "how are you" in q.lower():
            l = ["hi there. i feel good. thanks for asking","i'm fine. thanks for asking","good","excellent"]   # list of some strings
            random.shuffle(l)    # shuffling will take place here
            speak(l[0])    # first element after shuffling will be as output
        
        # logic for the wikipedia query
        if "wikipedia" in q.lower():    # lower() function is used to avoid any capitalisation in the string
            speak("searching wikipedia...")
            q=q.replace("wikipedia", "")    # query is replacing wikipedia, in order to not search again wikipedia inside wikipedia
            results=wikipedia.summary(q,sentences=2)  # "results" variable will store the result of the search
            print(results)
            speak(results)   # results varible is passed in speak function
        
        #logic for google search
        if "search on google" in q.lower():
            q=q.lower().replace("search on google", "")  # replacing "search on google" from the string while searching
            url='https://google.com/search?q=' + q     # creating a url og google search
            webbrowser.open(url)   # opening the google search url on web browser
            
        #logic to open youtube
        elif "open youtube" in q.lower():
            webbrowser.open("youtube.com")    # webbrowser package is accessed here directly to open link provided

        #logic to open google
        elif "open google" in q.lower():
            speak("what should i search")
            gs=SI().lower()
            webbrowser.open('https://google.com/search?q=' + gs )   # webbrowser package is accessed here directly to open link provided

        # logic to play music
        elif "play music" in q.lower():
            songs_dir='C:\\Users\\Acer\\Music\\tunes' # directory where songs are placed
            songs = os.listdir(songs_dir)  # "songs" variable access the songs name present in the directory
            print(songs)  # will print the names of songs like array format
            random.shuffle(songs)   # random songs will be played
            os.startfile(os.path.join(songs_dir,songs[0]))  # to play the first song in the directory

        # logic to tell time
        elif "time" in q.lower():
            t=datetime.datetime.now().strftime("%H:%M:%S")  # "t" variable is storing the time at the instance  
            # here strftime() function is used for the time format
            print(f"Time is {t}")   # to print and speak time as ouput
            speak(f"Time is {t}")

        # logic to open Visual Studio Code
        elif "open code" in q.lower():
            path='C:\\Users\\Acer\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe'  # "path" variable holds the location of VS Code application
            os.startfile(path)  # here the application is launched 

        # email logic
        elif "email" in q.lower():
            try:      # try catch is used if there will be an error because of internet or server
                speak("what should i say")   # asking to speak
                content=SI()  # "content" variable will store the content of email to be sent
                to='email'  # "to" variable stores the email
                email(to,content) # calling the eamil function and passing the information 
                speak("email sent successfully")
            except Exception as e:
                print(e)  # printing exception if occurs
        time.sleep(1)
        print("you wanna proceed or exit")    # print function
        speak("you wanna proceed or exit")    # speak function
        ex=SI()  # asking for the proceeding or exit from program

main()
