
from pathlib import Path
from process import *
from labels import *
from labelling import *
from output import *

audio_file_path = 'Input/commercial_mono.wav'
wav_fpath = Path(audio_file_path)
cont_embeds, wav_splits =process(wav_fpath)
labels=labels(cont_embeds)
labelling = create_labelling(labels,wav_splits)
output=output(labelling)