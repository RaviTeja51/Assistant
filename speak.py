import pyttsx3 as ttp

def speak(inp):
    speaker = ttp.init()

    rate = speaker.getProperty("rate")
    speaker.setProperty("rate",rate-60)
    voices = speaker.setProperty("voices","english")
    speaker.say(inp)
    speaker.runAndWait()
    return
