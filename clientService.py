import os

from com_in_ineuron_ai_service.brandMeasureservice import BrandMeasureService
from com_in_ineuron_ai_speech_to_text.speechToText import speech2Text
from com_in_ineuron_ai_speech_to_text.spetotxt import get_large_audio_transcription

# brndMsreObj = BrandMeasureService()
#
#
# audio_file_path = 'InputFiles/commercial_mono.wav'
# brndMsreObj.performSpeakerDiarization(audio_file_path)
from com_in_ineuron_ai_spellingcorrector.spellcorrector import spell_corrector

FolderPath = "InputFiles"
fileList = os.listdir(FolderPath)
for val in fileList:
    outputText = get_large_audio_transcription(os.path.join(FolderPath,val))
    print(outputText)

    for val in outputText.keys():
        spellcorrectedOp = spell_corrector(outputText[val])
        print("Input Text : ", outputText[val])
        print("Corrected Text : ", spellcorrectedOp)
        outputText[val] = spellcorrectedOp

# speech2Text("InputFiles")
