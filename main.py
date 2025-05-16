#!/usr/bin/env python3
import os
import speech_recognition as ear
import speech_recognition as ear2
import pyttsx3
import webbrowser as wb


engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-70)

# get audio from the microphone
r = ear.Recognizer()

def start():
    engine.say("I am on. Systems online. I am ready.")
    engine.runAndWait()

def end():
    engine.say("Turning off. See you")
    engine.runAndWait()
    exit()

def operation(text):
    myString = text
    if myString.find('x')!= -1:
        myString = myString.replace('x','*')
    if myString.find('*')!= -1 or myString.find('/')!=-1 or myString.find('+')!=-1 or myString.find('-')!=-1:
        try:
            a = eval(myString)
            print(a)
            engine.say(text+"gives"+ str(a) )
            engine.runAndWait()
        except SyntaxError:
            engine.say("oops!")
            print("oops!")
            engine.runAndWait()

def intro(text):
    if text == 'introduce yourself':
        engine.say("Hi everyone, i am Jarvis, I am currently in development stage, Thank you, have a good day")
        print("Hi everyone, i am Jarvis.I am currently in development stage.Thank you, have a good day")
        engine.runAndWait()

def greet(text):
    if text == 'hello':
        engine.say("Hi Sir")
        print("Hi Sir")
        engine.runAndWait()

def prompt(text):
    if text == "jarvis" or text == "Jarvis":
        engine.say("yes, sir")
        print("Yes, sir")
        engine.runAndWait()

def shutdown(text):
    if text == "shut down" or text == "shutdown":
        with ear2.Microphone() as s:
            engine.say("really shutdown system?")
            print("really shutdown system?")
            engine.runAndWait()
            a = r.listen(s)
        con = r.recognize_google(a)
        if con == "yes" or con =="Yes":
            engine.say("Shutting down")
            print("Shutting down")
            os.system('shutdown -s')
            engine.runAndWait()

def standby(text):
    if text == "standby" or text == "stand by" or text == "stop listening" or text == "stay on hold" or text =="hold":
        engine.say("staying on hold")
        print("staying on hold")
        engine.runAndWait()
        i = 0
        while i == 0:
            with ear2.Microphone() as s:
                a = r.listen(s)
            try:
                text = r.recognize_google(a)
                if text == "listen to me":
                    main()
                    i = 1
            except ear.UnknownValueError:
                i = 0
            except ear.RequestError as e:
                i = 0

def location(text):
     if "where is" in text:
        text = text.split(" ")
        location = text[2]
        print("Hold on, I will show you where " + location + " is.")
        engine.say("Hold on, I will show you where " + location + " is.")
        wb.open_new_tab("https://www.google.com.np/maps/place/" + location)
        engine.runAndWait()

def query(text):
     if "search for" in text:
        #text = text.split(" ")
        term = text[2]
        print("Hold on, I will show you the results of " + term)
        engine.say("Hold on, I will show you the results of" + term)
        wb.open_new_tab("https://www.google.com.np/search?q=" + term)
        engine.runAndWait()

def main():
    def listen():
        with ear.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Speak:")
            audio = r.listen(source)
            return audio

    engine.say("I am listening")
    engine.runAndWait()
    while True:
        audio = listen()
        try:
            text = r.recognize_google(audio)
            print("-->" + text)
            engine.say("You said" + text)
            engine.runAndWait()
            greet(text)
            operation(text)
            intro(text)
            prompt(text)
            standby(text)
            shutdown(text)
            location(text)
            query(text)

            if "power off" in text:
                break

        except ear.UnknownValueError:
            print("Could not understand audio")
            engine.say("Could not understand audio")
            engine.runAndWait()
        except ear.RequestError as e:
            print("Could not request results; {0}".format(e))
            engine.say("Could not request results; {0}".format(e))
            engine.runAndWait()

#calling main function
try:
    start()
    main()
    end()
except OSError:
    engine.say("I can't listen to you")
    print("I can't listen to you")
    engine.runAndWait()
