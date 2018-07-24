import os
import sys

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import matplotlib.pyplot as plt

import moviepy.editor as mp

def main():
    sound_name = input_filename("Input sound file name. > ")
    sound_file = wav_import(sound_name)
    movie_name = input_filename("Input movie file name. > ")
    mp4towav(movie_name)
    movie_file = wav_import("audio.wav")

    corr,estimated_delay = cross_correlation(sound_file,movie_file)
    wav_prot(sound_file,movie_file,corr,estimated_delay)

# ファイル名を取得，存在するファイル名を入力するまで聞き返す
def input_filename(sentence_to_display):
    while True:
        filename = input(sentence_to_display)
        if os.path.exists(filename):
            break
        else:
            print("入力した名前のファイルは存在しません。")
            print("もう一度入力してください。")

    return filename

#wavファイル読み込み
def wav_import(filename):
    data,fs = sf.read(filename)

    print ("Sampling rate :", fs)

    if (data.shape[1] == 2):
        left = data[:, 0]
        right = data[:, 1]
        return left
    else:
        return data

#mp4動画ファイルをwavファイルに変換する
def mp4towav(filename):
    clip_input = mp.VideoFileClip(filename).subclip()
    clip_input.audio.write_audiofile('audio.wav')


#相互相関をとって遅延時間を算出
def cross_correlation(sig1,sig2):
    corr = np.correlate(sig1, sig2, "full")
    estimated_delay = corr.argmax() - (len(sig2) - 1)
    print("estimated delay is " + str(estimated_delay))
    return corr,estimated_delay

def wav_prot(sig1,sig2,corr,estimated_delay):
    plt.subplot(4, 1, 1)
    plt.ylabel("sig1")
    plt.plot(sig1)

    plt.subplot(4, 1, 2)
    plt.ylabel("sig2")
    plt.plot(sig2, color="g")

    plt.subplot(4, 1, 3)
    plt.ylabel("fit")
    plt.plot(np.arange(len(sig1)), sig1)
    plt.plot(np.arange(len(sig2)) + estimated_delay, sig2 )
    plt.xlim([0, len(sig1)])

    plt.subplot(4, 1, 4)
    plt.ylabel("corr")
    plt.plot(np.arange(len(corr)) - len(sig2) + 1, corr, color="r")
    plt.xlim([0, len(sig1)])

    plt.show()


if __name__ == '__main__':
    main()
