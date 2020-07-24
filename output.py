from pydub import AudioSegment
AudioSegment.converter = "ffmpeg/bin/ffmpeg.exe"
AudioSegment.ffmpeg = "ffmpeg/bin/ffmpeg.exe"
AudioSegment.ffprobe ="ffmpeg/bin/ffmpeg.exe"


def output(labelling):
    # Creating different audios based on the labelling/timeframes received.
    output = {}
    for x, y, z in labelling:
        if x in output:
            output[x].append((y, z))
        else:
            output[x] = [(y, z)]

    values = []
    items = output.items()
    for item in items:
        values.append(item[1])

    audio = AudioSegment.from_wav('Denoise/Denoise_commercial_mono.wav')
    voices = []
    for i in values:
        n = audio[0]
        for j in i:
            start_time, stop_time = j
            n += audio[(start_time * 1000):(stop_time * 1000)]
        voices.append(n)

    for i, j in enumerate(voices):
        j.export(f'Output/voice_{i}.wav')
    return