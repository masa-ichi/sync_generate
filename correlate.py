import numpy as np
import matplotlib.pyplot as plt

# 正規分布のノイズ作成
target_sig = np.random.normal(size=1000) * 1.0
delay = 573 # 遅延
sig1 = np.random.normal(size=2000) * 0.2
sig1[delay:delay+1000] += target_sig
sig2 = np.random.normal(size=2000) * 0.2
sig2[:1000] += target_sig

#相互相関をとって遅延時間を算出
corr = np.correlate(sig1, sig2, "full")
estimated_delay = corr.argmax() - (len(sig2) - 1)
print("estimated delay is " + str(estimated_delay))

#描画
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
