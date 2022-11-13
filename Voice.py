import speech_recognition as sr

def record_volume(countChanged):

    r = sr.Recognizer()

    fout = open('BufferText.txt', 'w')
    print('It`s work')
    try:
        with sr.Microphone(device_index=14) as sourse:
            countChanged.emit('Listen')
            print('Listen...')
            audio = r.listen(sourse,phrase_time_limit=10)

        querty = r.recognize_google(audio, language='en-En')
        print(querty)
        return querty

    except:
        return 'Error'

    finally:
        fout.close()










