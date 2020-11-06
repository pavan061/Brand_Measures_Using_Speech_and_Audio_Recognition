import speech_recognition as sr
import os

outputText = {}
def speech2Text(FolderPath):
    fileList = os.listdir(FolderPath)
    for val in fileList:
        r = sr.Recognizer()
        with sr.AudioFile(os.path.join(FolderPath,"eng.wav")) as source:
            audio = r.record(source)
        try:
            textdata = r.recognize_google(audio)
            print("Text data: " + textdata)
            # return textdata
        except sr.UnknownValueError:
            print(" Audio Error")



#Write results to a txt file
#file = open("result.txt","w")
#file.write(textdata)
#file.writelines(L) 
#file.close()
