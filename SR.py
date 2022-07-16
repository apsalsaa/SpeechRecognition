import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
  print("You may speak")
  audio = r.listen(source)

  try:
    text = r.recognize_google(audio)
    print("Here what i hear:{}" .format(text))
  except:
    print("Pardon?")