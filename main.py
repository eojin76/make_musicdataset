
from pydub import AudioSegment
import os

#파일 분할 함수
def split_wav_into_segments(wav_file, output_directory, segment_length=30):
    # 출력 디렉토리가 없다면 생성합니다.
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # WAV 파일을 로드합니다.
    audio = AudioSegment.from_wav(wav_file)

    # 분할할 시간(밀리초)을 계산합니다.
    segment_length_ms = segment_length * 1000

    # WAV 파일을 30초 단위로 분할합니다.
    for i, start_time in enumerate(range(0, len(audio), segment_length_ms)):
        # 분할된 WAV 파일의 이름을 생성합니다.
        segment_filename = f"{i+1}.wav"
        segment_path = os.path.join(output_directory, segment_filename)

        # WAV 파일을 분할합니다.
        segment = audio[start_time:start_time+segment_length_ms]

        # 분할된 WAV 파일을 저장합니다.
        segment.export(segment_path, format='wav')

        print(f"Segment {i+1} saved: {segment_path}")

# 예제 사용법
wav_file = '60.wav'  # 분할할 WAV 파일의 경로
output_directory = 'segment'  # 분할된 WAV 파일을 저장할 디렉토리 경로

split_wav_into_segments(wav_file, output_directory, segment_length=30)

