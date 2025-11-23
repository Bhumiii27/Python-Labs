post lab:
#1.
import numpy as np
import matplotlib.pyplot as plt
# Parameters
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)
f1 = 5
f2 10
sine1 = np.sin(2* np.pi* f1*t)
sine2 = np.sin(2* np.pi* f2*t)
# Add the two signals
combined_signal = sine1 + sine2
#result
plt.figure(figsize=(10,4))
plt.plot(t, combined_signal)
plt.title('Sum of of 5 Hz and 10 Hz Sine Waves')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

#2.
 import numpy as np
import matplotlib.pyplot as plt
fs = 500
duration = 2
#Duration in seconds
t = np.linspace(0, duration, int(fs * duration), endpoint=False)
sine_wave = np.sin(2* np.pi * 5 *t) #5 Hz sine wave
cosine_wave = np.cos(2* np.pi * 10 *t) #10 Hz cosine wave
#Element-wise multiplication
product_signal = sine_wave * cosine_wave
plt.figure(figsize=(10, 4))
plt.plot(t, product_signal)
plt.title('Product of 5 Hz Sine and 10 Hz Cosine Waves')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude")
plt.grid(True)
plt.show()

#3
import numpy as np
import matplotlib.pyplot as plt

fs = 1000                # Duration in seconds
duration = 1
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

freq = 5
original = np.sin(2 * np.pi * freq * t)
shift = 0.1
shifted = np.sin(2 * np.pi * freq * (t - shift))

#result
plt.figure(figsize=(10, 4))
plt.plot(t, original, label="Original 5 Hz Sine")
plt.plot(t, shifted, label="Shifted by 0.1s", linestyle='--')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Original and Shifted 5 Hz Sine Wave')
plt.legend()
plt.grid(True)
plt.show()


#4
import numpy as np
import matplotlib.pyplot as plt

fs = 1000
duration = 1
t = np.linspace(0, duration, int(fs * duration), endpoint=False)
req = 5
original = np.sin(2 * np.pi * freq * t)
reversed_signal = original[::-1]
#result
plt.figure(figsize=(10, 4))
plt.plot(t, original, label='Original 5 Hz Sine')
plt.plot(t, reversed_signal, label='Time-reversed', linestyle='--')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Original and Time-Reversed 5 Hz Sine Wave')
plt.legend()
plt.grid(True)
plt.show()

#5.
import numpy as np
import matplotlib.pyplot as plt

fs = 1000
duration = 1
t = np.linspace(0, duration, int(fs * duration), endpoint=False)
freq = 5
original = np.sin(2 * np.pi * freq * t)
reversed_signal = original[::-1]
#result
plt.figure(figsize=(10, 4))
plt.plot(t, original, label='Original 5 Hz Sine')
plt.plot(t, reversed_signal, label='Time-reversed', linestyle='--')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Original and Time-Reversed 5 Hz Sine Wave')
plt.legend()
plt.grid(True)
plt.show()
