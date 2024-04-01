import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

def generate_and_save_spectrogram_and_npy(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
    log_S = librosa.power_to_db(S, ref=np.max)

    plt.figure(figsize=(10, 4))
    librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel')
    plt.title('Mel spectrogram')
    plt.colorbar(format='%+02.0f dB')
    plt.tight_layout()
    plt.savefig(os.path.splitext(audio_path)[0] + '.png')
    plt.close()
    
    np.save(os.path.splitext(audio_path)[0] + '.npy', S)

def traverse_and_generate_spectrograms_and_npy(root_dir):
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.wav'):
                audio_path = os.path.join(subdir, file)
                generate_and_save_spectrogram_and_npy(audio_path)
                print(f'Processed {audio_path}')

def main():
    root_dir = '/Users/shreevardhanshah/dl/RECS'
    traverse_and_generate_spectrograms_and_npy(root_dir)

if __name__ == "__main__":
    main()
