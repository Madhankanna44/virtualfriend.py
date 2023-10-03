import pyttsx3
vtf = pyttsx3.init()


#rate
rate = vtf.getProperty('rate')
vtf.setProperty('rate' ,140)


def vtf_speak(txt):
    print("speaking....")
    vtf.say(txt)
    vtf.runAndWait()

txt = "Hello my friend I am  your virtual friend"
vtf_speak(txt)

txt = input("what should I say: ")
vtf_speak(txt)


while txt != 'bye':
    txt = input("what should I say: ")
    txt = txt.lower()
    if txt != 'bye':
       vtf_speak(txt)
    hyelse:
       vtf_speak('see u again my friend, that was nice to meet you')

