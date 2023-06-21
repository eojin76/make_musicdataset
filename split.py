import wave
from split2 import get_milliseconds_array


def cut_wav_segments(input_file, milliseconds_array):
    with wave.open(input_file, 'rb') as wav_file:
        params = wav_file.getparams()
        sample_width = params.sampwidth
        frame_rate = params.framerate
        n_frames = params.nframes
        channels = params.nchannels

        for i in range(len(milliseconds_array) - 1):
            start_time = milliseconds_array[i]
            end_time = milliseconds_array[i + 1]

            start_frame = int(start_time / 1000 * frame_rate)
            end_frame = int(end_time / 1000 * frame_rate)
            num_frames = end_frame - start_frame

            new_wav_file = wave.open(f"segment_{i + 1}.wav", 'wb')
            new_wav_file.setparams(params)

            wav_file.setpos(start_frame)
            frames = wav_file.readframes(num_frames)
            new_wav_file.writeframes(frames)

            new_wav_file.close()

    wav_file.close()


cut_wav_segments('10-2.wav', get_milliseconds_array())
