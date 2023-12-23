import speech_recognition as sr
import os

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

if __name__ == '__main__':
    print('Pycharm')
    say("Hello I am jarvis A.I")



# ============== The below code is windows only ============

# import win32.client
# speaker = win32com.client.Dispatch("SAPI.SpVoice")

# while 1:
#     print("Enter the word you want to speak it out by coomputer")
#     s = input()
#     speaker.Speak(s)

# ================ Code is end Here =================