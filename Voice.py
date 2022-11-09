import speech_recognition as sr

def record_volume(countChanged):

    r = sr.Recognizer()
    fout = open('BufferText.txt', 'w')
    print('It`s work')
    try:
        with sr.Microphone(device_index=1) as sourse:
            countChanged.emit('Listen')
            print('Listen...')
            audio = r.listen(sourse)
        querty = r.recognize_google(audio, language='en-En')
        return querty

    except:
        return 'Error'

    finally:
        fout.close()










