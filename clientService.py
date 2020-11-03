from com_in_ineuron_ai_service.brandMeasureservice import BrandMeasureService
from com_in_ineuron_ai_speech_to_text.speechToText import speech2Text

brndMsreObj = BrandMeasureService()


audio_file_path = 'InputFiles/Maya.wav'
brndMsreObj.performSpeakerDiarization(audio_file_path)
speech2Text("SeparatedOutputFiles")
