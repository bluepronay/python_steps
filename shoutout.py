#shoutout to everyone!!!
#pip install pywin32   to run this do this in terminal


import win32com.client

def text_to_speech(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

text_to_speech("Korbo Lorbo Jeetbo re...."); 

