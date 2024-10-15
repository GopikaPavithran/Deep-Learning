import speech_recognition as sr
def speech_recog():
    r=sr.Recognizer()                     # Recognizer - used to handle the speech recognition process.
    mic=sr.Microphone()                   # Microphone - representing the default system microphone.
    with mic as source:                   
        print("Speak..")
        r.energy_threshold=10            # energy_threshold is the minimum level of audio energy required to register as speech
        r.adjust_for_ambient_noise(source,duration=1)    # listens to the background noise for a given duration and adjusts the energy_threshold accordingly
        audio=r.listen(source)             # listens for speech from the microphone and records it as an audio object
        try:
            text=r.recognize_google_cloud(audio)         # recognize the recorded speech using Google's cloud-based speech recognition service
            print("You said:",text)
        except:
            print("Didn't hear anything! Please speak again..")
speech_recog()