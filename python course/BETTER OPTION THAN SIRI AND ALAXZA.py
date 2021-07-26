0
import pyttsx3
engine = pyttsx3.init()


rate = engine.getProperty('rate')
print (rate)
engine.setProperty('rate', 125)

volume = engine.getProperty('volume')
print (volume)
engine.setProperty('volume',1.0)


voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

engine.say("good morning sir")
engine.say("sir i was thinking")
engine.say("           i am better than siri and alaxza")
engine.say('            YOU fool HOW DID YOU SAY THAT')
engine.say('              THAN TAKE HELP OF THEm YOU DONT NEED ME OK BY FOOL')
engine.say('                   i will never answer you by by tata NEVER MEET YOU LATER')
engine.runAndWait()
engine.stop()
engine.runAndWait()