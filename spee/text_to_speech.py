import pyttsx3                       # pyttsx3 - library to convert text to speech
txt_sp=pyttsx3.init()               # initialising
text=input("Enter a text...")
voices=txt_sp.getProperty('voices')   # to get list of available voices on the system
for voice in voices:
    print('ID:',voice.id)
txt_sp.setProperty('voice',voices[0].id)   # to set voice 
txt_sp.say(text)                           
txt_sp.runAndWait()                        # runs the speech engine and waits until the speaking is finished.
