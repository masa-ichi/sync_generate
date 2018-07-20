import os
import sys

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

def main():
    sound_name1 = input_filename("Input sound file name. > ")
    sound_file1 = wav_import(sound_name1)
    sound_name2 = input_filename("Input sound file name. > ")
    sound_file2 = wav_import(sound_name2)

    corr,estimated_delay = cross_correlation(sound_file1,sound_file2)
    wav_prot(sound_file1,sound_file2,corr,estimated_delay)

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
    fs, data = read(filename)

    print ("Sampling rate :", fs)

    if (data.shape[1] == 2):
        left = data[:, 0]
        right = data[:, 1]

    return left



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
