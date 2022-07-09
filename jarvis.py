import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setproperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour=int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir.Please tell me how may i help you")

def takecommand():
    #it takes microphone input from the user and return output

    r=sr.Recognizer()
    with sr.Microphne() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said:,{query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,comment):
    server=smtplib('smtp gmail.com', 587)
    server.ehlo()
    server.startttls()
    server.login('yourmail@gmail.com', 'your-password')
    server.sendmail('yourmail@gmail.com',to,content)
    server.close()

if __name__ =="__main__":
    wishme()
    #while True:
    if 1:
        query = takecommand().lower()

       #logic for executing task based on query
        if wikipedia in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentence=2)
            speak("Accoding to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
    
        elif 'stackoverflow' in query:
            webbrowser.open("stackoveflow.com")


        elif 'playmusic' in query:
            music_dir ='D:\\Non Critical\\songs\\Favourite Songs2'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"SIR THE TIME IS {str}")

        elif 'open code' in query:
             codepath="C:\\Users\\Anil Sharma\\AppData\\Roaming\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
             os.startfile(codepath)

        elif 'Email to Akshit' in query:
            try:
                speak("What should i say?")
                content = takecommand()
                to="anilsharma.as117@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Akshit bhai.I am not able to send the email")