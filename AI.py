#Importing required packages. 

import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import wikipedia
from englisttohindi.englisttohindi import EngtoHindi

#Setting up the engine. 

engine=pyttsx3.init('sapi5')
engine.setProperty('rate', 190)
engine.setProperty('volume', 1.0)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#The Speak Function.

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print("Sophie: Please enter your name")
speak("Please enter your name")
nm = input("You: ")

#The TakeCommand Function.

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening.....")
        r.pause_threshold = 10
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
       
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f'You: {query}\n')

    except Exception as e:
        #print(e)
        print("Say that again please.....")
        return "None"
    return query

#The WishMe Function.

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Sophie: Good Morning {}!!!".format(nm))
        speak("Good Morning {}".format(nm))
    elif hour>=12 and hour<18:
        print("Sophie: Good Afternoon {}!!!".format(nm))
        speak("Good Afternoon {}".format(nm))
    else:
        print("Sophie: Good Evening {}!!!".format(nm))
        speak("Good Evening {}".format(nm))
     
    print("Sophie: I am Sophie, Please tell me how can I help you?")
    speak("I am Sophie,Please tell me how can I help you")

#The Main Body of the Project.

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        print("You: " + query)
        if 'hello' in query:
            print("Sophie: Hello {}".format(nm))
            speak("Hello {}".format(nm))
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")       
        
        elif 'tell me about' in query:
            speak("Searching Wikipedia.....")
            query = query.replace("wikipedia"," ")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open project' in query:
            project_dir='F:\Deepak\B.Tech_Work\FUTURE_PROJECT\Python'
            folder = os.listdir(project_dir)
            print("Sophie: You have different files to open in it,So I am opening the most preferable one...")
            speak("You have different files to open in it,So I am opening the most preferable one...")
            print(folder)
            os.startfile(os.path.join(project_dir,folder[7]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sophie: Sir,the time is {strTime}")
            speak(f"Sir,the time is {strTime}")

        elif 'open code' in query:
            print("Sophie: Opening Visual Studio Code...")
            speak("Opening Visual Studio Code...")
            code_Path = "F:\Deepak\B.Tech_Work\Software\Visual Studio Code.lnk"
            os.startfile(code_Path)
        
        elif 'open file' in query:
            print("Sophie: Opening Project PPT...")
            speak("Opening Project PPT...")
            file_Path = "F:\Deepak\B.Tech_Work\FUTURE_PROJECT\Project Analysis.pptx"
            os.startfile(file_Path)
        
        elif 'open teams' in query:
            print("Sophie: Opening Microsoft Teams...")
            speak("Opening Microsoft Teams...")
            class_Path = "C:\\Users\\hp\\Downloads\\Teams_windows_x64.exe"
            os.startfile(class_Path)
        
        elif 'crypt' in query:
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            speak("Please enter the code")
            code = input("Enter the code:")                      
            print("Enter the key value:")
            speak("Please enter the key value")
            key = takeCommand().lower()
            Encrypt = ''
            Decrypt = ''
            print("Sophie: What to do you want to do from the options given below:")
            speak("What to do you want to do from the options given below:")
            print("1.Encrypt")
            speak("Encrypt")
            print("2.Decrypt")
            speak("Decrypt")
            print("Please enter your choice:")
            speak("Please enter your choice.")
            ch = takeCommand().lower()
            if ch==1:
                for i in code:
                    p = alphabet.find(i)
                    np = (p+int(key))%26
                    Encrypt = Encrypt+alphabet[np]
                print(f'Your encrypted code is {Encrypt}')
                speak(f'Your encrypted code is {Encrypt}')
            else:
                for j in code:
                    r = alphabet.find(j)
                    nr = (r-int(key))%26
                    Decrypt = Decrypt+alphabet[nr]
                print(f'Your decrypted code is {Decrypt}')
                speak(f'Your decrypted code is {Decrypt}')
        
        elif 'translate' in query:
            print("Sophie: Please enter the message to be translate")
            speak("Please enter the message to be translate")
            message = takeCommand().lower()
            res_conv = ''
            res = EngtoHindi(message)
            res_conv = res_conv+res.convert
            print(f'Sophie: Your translated message is {res_conv}')
        
        elif 'sleep' in query:
            print("Sophie: Ok Sir")
            speak("Ok Sir")
            exit()
        
        else:
            print("Sophie: I think you don't have any other work from me,so I am going to sleep.")
            speak("I think you don't have any other work from me,so I am going to sleep.")
            exit()