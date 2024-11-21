import pywhatkit as kit
import time
import random
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import requests
import gui 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Maya. How may I assist you?")




def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def take_email():
    try:
        speak("Please enter the recipient's email address:")
        print("Please enter the recipient's email address:")
        email_address = input()
        speak(f"Recipient's email address is: {email_address}\n")
        print(f"Recipient's email address is: {email_address}\n")
    except Exception as e:
        speak("Error while taking the email address. Please try again.")
        print("Error while taking the email address. Please try again.")
        return "None"
    return email_address


def sendEmail(content):
    email_address = take_email()
    
    if email_address != "None":
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('jarvis787834@gmail.com', 'ooim pawb pfqw cyfw')
        server.sendmail('jarvis787834@gmail.com', email_address, content)
        server.close()
        speak("Email has been sent to the specified recipient!")

def open_news():
    webbrowser.open("https://news.google.com")

def tell_joke():
    jokes = [
        "What do you call a fish with no eyes? Fsh!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call a lazy kangaroo? Pouch potato!"
        "What do you call an ant who fights crime? A vigilANTe!"
        "What did the policeman say to his hungry stomach? “Freeze. You are under a vest.”"
    ]
    speak(random.choice(jokes))

def convert_to_12_hour(time_in_24h):
    """Converts a time in 24-hour format (HH:MM) to 12-hour format with AM/PM."""
    try:
        hour, minute = map(int, time_in_24h.split(":"))
        if hour == 0:
            hour = 12
            am_pm = "AM"
        elif hour == 12:
            am_pm = "PM"
        elif hour > 12:
            hour -= 12
            am_pm = "PM"
        else:
            am_pm = "AM"
        return f"{hour}:{minute:02} {am_pm}"
    except ValueError:
        return "Invalid time format."
    

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
         speak("what you will like to watch ?")
         qrry = take_command().lower()
         kit.playonyt(f"{qrry}")
         speak("Opening Youtube")
        
        if  'send message' in query :
           speak("Your Message is Going Sir Please wait")
           kit.sendwhatmsg_instantly("+919509269410","Hello,BIRO")
           
         
           
        
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")

        elif 'the time' in query:
          current_time_24h = datetime.datetime.now().strftime("%H:%M")
          converted_time = convert_to_12_hour(current_time_24h)
          speak(f"Sir, the time is {converted_time}")

        elif 'open vs code' in query:
            vs_code_path = "C:/Users/puroh/AppData/Local/Microsoft/WindowsApps/python3.12.exe"
            os.startfile(vs_code_path)
            speak("Your App is Launching Sir")
       
       
        elif 'open chrome' in query:
                open_chrome_path ='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
                os.startfile(open_chrome_path)
                speak("Google Chrome Is opening")


        
        elif 'maximize this window' in query:
         pyautogui.hotkey('alt', 'space')
         time.sleep(1)
         pyautogui.press('x')
        
        
        elif 'google search' in query:
         query = query.replace("google search", "")
         pyautogui.hotkey('alt', 'd')
         pyautogui.write(f"{query}", 0.1)
         pyautogui.press('enter')
        
        elif ' search' in query:
         query = query.replace(" search", "")
         pyautogui.hotkey('alt', 'd')
         time.sleep(1)
         pyautogui.press('tab')
         pyautogui.press('tab')
         pyautogui.press('tab')
         pyautogui.press('tab')
         time.sleep(1)
         pyautogui.write(f"{query}", 0.1)
         pyautogui.press('enter')
        
        
        elif 'open new window' in query:
         pyautogui.hotkey('ctrl', 'n')
        
        
        elif 'open incognito window' in query:
         pyautogui.hotkey('ctrl', 'shift', 'n')
        
        
        elif 'minimise this window' in query:
         pyautogui.hotkey('alt', 'space')
         time.sleep(1)
         pyautogui.press('n')

        elif "what is my ip address" in query:
         speak("Checking")
         try:
           ipAdd = requests.get('https://api.ipify.org').text
           print(ipAdd)
           speak("your ip adress is")
           speak(ipAdd)
         except Exception as e:
          speak("network is weak, please try again some time later")
        
        
        elif 'open history' in query:
         pyautogui.hotkey('ctrl', 'h')
        
        
        elif 'open downloads' in query:
         pyautogui.hotkey('ctrl', 'j')
        
        
        elif 'previous tab' in query:
         pyautogui.hotkey('ctrl', 'shift', 'tab')
        
        
        elif 'next tab' in query:
         pyautogui.hotkey('ctrl', 'tab')

        elif "shut down the system" in query:
          os.system("shutdown /s /t 5")
        
        
        elif "restart the system" in query:
          os.system("shutdown /r /t 5") 
         
        elif 'close tab' in query:
         pyautogui.hotkey('ctrl', 'w')
        
        
        elif 'close window' in query:
         pyautogui.hotkey('ctrl', 'shift', 'w')
        
        
        elif 'clear browsing history' in query:
         pyautogui.hotkey('ctrl', 'shift', 'delete')
        
        
        elif 'close chrome' in query:
         os.system("taskkill /f /im chrome.exe")

        elif "open command prompt" in query:
          os.system("start cmd")
          speak("Opening Command Prompt")
        
        elif "close command prompt" in query:
         os.system("taskkill /f /im cmd.exe")
         speak("Closing Command Prompt")

        
        
        elif 'open lab code'in query:
            open_lab_code = "C:\\Users\\DELL\\Desktop\\Lab record code"
            os.startfile(open_lab_code)
            speak("Sir Your Command is completed")
        
        
        elif "volume up" in query:
         speak("Your Speaker volume has raised Sir")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")

   
        elif 'email to me' in query:
         try:
          speak("What Should I say")
          print("What should I say?")
          content = take_command()
          sendEmail(content)
         except Exception as e:
          print(e)
          print("Sorry sir. I am not able to send this email")


         

        elif "volume down" in query:
          pyautogui.press("volumedown")
          pyautogui.press("volumedown")
          pyautogui.press("volumedown")
          pyautogui.press("volumedown")
          pyautogui.press("volumedown")
          pyautogui.press("volumedown")
          pyautogui.press("volumedown")
          pyautogui.press("volumedown")
          pyautogui.press("volumedown")
          pyautogui.press("volumedown")
          pyautogui.press("volumedown")
          pyautogui.press("volumedown")
          pyautogui.press("volumedown")
          pyautogui.press("volumedown")
          pyautogui.press("volumedown")
          speak("Your Speaker volume has decreased Sir")
        elif "who are you" in query:
          print('My Name Is Jarvis An Virtual AI Assistant To This Machine')
          speak('My Name Is Jarvis An Virtual AI Assistant To This Machine')
          print('I can Do Everything that my creator programmed me to do')
          speak('I can Do Everything that my creator programmed me to do')

        elif "who created you" in query:
         print('I am Created By Sir aryan,  dev,  avdesh, varun and aman I created with Python Language, in Visual Studio Code.')
         speak('I am Created By Sir aryan,  dev,  avdesh, varun and aman I created with Python Language, in Visual Studio Code.')


        elif 'open news' in query:
            open_news()


        elif 'tell me a joke' in query:
            tell_joke()
        
       

        elif 'open whatsapp' in query:
           webbrowser.open("https://web.whatsapp.com/")

        elif 'open meeting' in query:
           webbrowser.open("https://meet.google.com/ekp-csbs-are")
       
        elif 'exit' in query:
            speak("Goodbye Sir! Have a great day!")
            break