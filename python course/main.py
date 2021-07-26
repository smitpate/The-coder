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

engine.say("SIR TUMNE SUBH SAVAR")
engine.say("KIVA HAL CHAL")
engine.say("         SIR TAMARA MATE AAK CUP COFEE BNAVU")
engine.say('            SIR TUMNE PIVE HOI THO BNAVU')
engine.say('             SIR COLD COFEE BNAVU KE HOT')
engine.say('                SIR TMARI COFEE TYAIR CHE')
engine.runAndWait()
engine.stop()
engine.runAndWait()