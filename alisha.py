import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')#to use inbilt voices

voices = engine.getProperty('voices')#getting details of current voice

engine.setProperty('voice', voices[1].id)#helps us to select different voices

#We use speak() function to convert our text to speech.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()#Without this command, speech will not be audible to us.

# Now, we will make a wishme() function that will make our Alisha. 
# Wish or greet the user according to the time of computer or pc. 
# To provide current or live time to A.I., we need to import a module called datetime

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Alisha Sir or Madam. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()#help us to recognize the voice
    with sr.Microphone() as source: # We will use this as source moicrophone
        print("Listening...") #seconds of non-speaking audio before a phrase is considered as complete  
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.


    except Exception as e:
        # print(e)    
        print("Say that again please...")  #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

#We have created a main() function, and inside this main() Function, we will call our speak function.

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Whatever we will write inside this speak() function will be converted into speech

        # Logic for executing tasks based on query
        if 'wikipedia' in query:    #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # Here, we are using an elif loop to check whether Youtube is in the user's query. 
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        #We first opened our music directory and then listed all the songs present in the directory with the os module's help. 
        
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Admin\\Desktop\\song'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0])) #Here with the help of os.startfile, you can play any song of your choice.

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") #we are using the datetime()function and storing the current or live system time into a variable called strTime.  
            speak(f"Sir, the time is {strTime}")#After storing the time in strTime, we are passing this variable as an argument in speak function 

        elif 'open code' in query:
            codePath = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

 