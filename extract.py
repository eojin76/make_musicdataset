import librosa
import numpy as np
import csv
import os

def get_file_paths(directory):
    file_paths = []

    # 디렉토리 내의 모든 파일과 하위 디렉토리를 검색합니다.
    for root, directories, files in os.walk(directory):
        # 파일 경로를 리스트에 추가합니다.
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)

    return file_paths

def extract_features_from_wav_files(wav_files, output_csv):
    # CSV 파일에 저장할 열 제목
    header = ['filename', 'chroma_stft_mean', 'chroma_stft_var', 'spectral_centroid_mean', 'spectral_centroid_var',
              'spectral_bandwidth_mean', 'spectral_bandwidth_var', 'rolloff_mean', 'rolloff_var','zero_crossing_rate_mean', 'zero_crossing_rate_var']

    # CSV 파일을 쓰기 모드로 엽니다.
    with open(output_csv, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)  # 열 제목을 CSV 파일에 씁니다.

        for file in wav_files:
            try:
                # WAV 파일을 로드합니다.
                y, sr = librosa.load(file, mono=True)

                # 특징을 추출합니다.
                chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
                spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
                spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
                rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
                zero_crossing_rate = librosa.feature.zero_crossing_rate(y)


                # 특징을 평균값으로 변환합니다.
                chroma_stft_mean = np.mean(chroma_stft)
                spectral_centroid_mean = np.mean(spectral_centroid)
                spectral_bandwidth_mean = np.mean(spectral_bandwidth)
                rolloff_mean = np.mean(rolloff)
                zero_crossing_rate_mean = np.mean(zero_crossing_rate)

                # 특징을 분산값으로 변환합니다.
                chroma_stft_var = np.var(chroma_stft)
                spectral_centroid_var = np.var(spectral_centroid)
                spectral_bandwidth_var = np.var(spectral_bandwidth)
                rolloff_var = np.var(rolloff)
                zero_crossing_rate_var = np.var(zero_crossing_rate)

                # 파일 이름과 특징 값을 CSV 파일에 씁니다.
                row = [file, chroma_stft_mean, chroma_stft_var, spectral_centroid_mean, spectral_centroid_var,
              spectral_bandwidth_mean, spectral_bandwidth_var, rolloff_mean, rolloff_var,zero_crossing_rate_mean, zero_crossing_rate_var]

                writer.writerow(row)

            except Exception as e:
                print(f'Error processing {file}: {str(e)}')

    print(f"Features extracted and saved to {output_csv}")


wav_files = get_file_paths('2010-2') # WAV 파일 리스트
output_csv = '2010-2.csv'  # 특징을 저장할 CSV 파일 이름

extract_features_from_wav_files(wav_files, output_csv)
