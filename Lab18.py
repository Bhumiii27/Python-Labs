import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
def load_audio(fs=44100, duration=2.0):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    audio = (np.sin(2 * np.pi * 440 * t) + 0.5 * np.sin(2 * np.pi * 880 * t)) * np.exp(-t * 2)
    return fs, audio
def load_ir(fs=44100, duration=0.5):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    ir = np.exp(-t * 8) * np.sin(2 * np.pi * 1000 * t)
    ir /= np.sqrt(np.sum(ir**2))
    return fs, ir
if __name__ == "__main__":
    fs, x = load_audio()
    _, h = load_ir(fs=fs)
    y_linear = signal.convolve(x, h, mode='full')
    N = len(x)
    h_pad = np.pad(h, (0, N - len(h)))
    X = np.fft.fft(x)
    H = np.fft.fft(h_pad)
    y_circ = np.real(np.fft.ifft(X * H))
    y_circ_trunc = y_circ[:len(y_linear)]
    plot_len = min(1024, len(y_linear))
    time_axis = np.arange(plot_len) / fs
    fig, axes = plt.subplots(4, 1, figsize=(12, 10))    
    axes[0].plot(np.arange(plot_len) / fs, x[:plot_len])
    axes[0].set_title('Original Audio')
    axes[0].grid(True)
    axes[1].plot(np.arange(min(512, len(h))) / fs, h[:min(512, len(h))])
    axes[1].set_title('Impulse Response')
    axes[1].grid(True)
    axes[2].plot(time_axis, y_linear[:plot_len])
    axes[2].set_title('Linear Convolution')
    axes[2].grid(True)
    axes[3].plot(time_axis, y_circ_trunc[:plot_len])
    axes[3].set_title('Circular Convolution')
    axes[3].set_xlabel('Time (s)')
    axes[3].grid(True)
    plt.tight_layout()
    plt.show()
    diff = y_linear[:plot_len] - y_circ_trunc[:plot_len]
    plt.figure(figsize=(12, 4))
    plt.plot(time_axis, diff)
    plt.title('Difference: Linear - Circular')
    plt.xlabel('Time (s)')
    plt.grid(True)
    plt.show()    
    print("Linear convolution shows true effect; circular has wrap-around artifacts.")

#2.Use Python to implement both cross-correlation and autocorrelation on a set of audio files (clean_audio.wav, noisy_audio.wav, periodic_audio.wav). Visualize and compare the results.
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal
def load_audio(file_path, fs=44100, duration=2.0):
    try:
        fs_file, audio = wavfile.read(file_path)
        if len(audio.shape) > 1:
            audio = audio[:, 0]
        audio = audio.astype(np.float32) / np.max(np.abs(audio))
        return fs_file, audio
    except FileNotFoundError:
        print(f"File {file_path} not found. Generating synthetic audio.")
        t = np.linspace(0, duration, int(fs * duration), endpoint=False)
        if 'clean' in file_path:
            audio = np.sin(2 * np.pi * 440 * t)
        elif 'noisy' in file_path:
            audio = np.sin(2 * np.pi * 440 * t) + 0.5 * np.random.randn(len(t))
        else:  
            audio = np.sin(2 * np.pi * 440 * t) + 0.3 * np.sin(2 * np.pi * 220 * t)  
        return fs, audio / np.max(np.abs(audio))
fs_clean, clean = load_audio('clean_audio.wav')
fs_noisy, noisy = load_audio('noisy_audio.wav')
fs_periodic, periodic = load_audio('periodic_audio.wav')
fs = fs_clean  
min_len = min(len(clean), len(noisy), len(periodic))
clean, noisy, periodic = [sig[:min_len] for sig in [clean, noisy, periodic]]
def autocorrelation(sig):
    corr = signal.correlate(sig, sig, mode='full')
    center = len(corr) // 2
    corr /= corr[center] if corr[center] != 0 else 1
    return corr
auto_clean = autocorrelation(clean)
auto_noisy = autocorrelation(noisy)
auto_periodic = autocorrelation(periodic)
def cross_correlation(sig1, sig2):
    corr = signal.correlate(sig1, sig2, mode='full')
    denom = np.sqrt(np.sum(sig1**2) * np.sum(sig2**2))
    return corr / denom if denom != 0 else corr
cross_clean_noisy = cross_correlation(clean, noisy)
cross_clean_periodic = cross_correlation(clean, periodic)
cross_noisy_periodic = cross_correlation(noisy, periodic)
corr_len = len(auto_clean)
plot_len = min(1000, corr_len - 1)
center = corr_len // 2
plot_start = max(0, center - plot_len // 2)
plot_end = min(corr_len, center + plot_len // 2)
actual_plot_len = plot_end - plot_start
lags = np.arange(- (center - plot_start), actual_plot_len - (center - plot_start)) / fs
fig1, axes1 = plt.subplots(3, 1, figsize=(10, 6))
axes1[0].plot(lags, auto_clean[plot_start:plot_end])
axes1[0].set_title('Auto: Clean')
axes1[0].grid(True)
axes1[1].plot(lags, auto_noisy[plot_start:plot_end])
axes1[1].set_title('Auto: Noisy')
axes1[1].grid(True)
axes1[2].plot(lags, auto_periodic[plot_start:plot_end])
axes1[2].set_title('Auto: Periodic')
axes1[2].set_xlabel('Lag (s)')
axes1[2].grid(True)
plt.tight_layout()
plt.show()
fig2, axes2 = plt.subplots(3, 1, figsize=(10, 6))
axes2[0].plot(lags, cross_clean_noisy[plot_start:plot_end])
axes2[0].set_title('Cross: Clean-Noisy')
axes2[0].grid(True)
axes2[1].plot(lags, cross_clean_periodic[plot_start:plot_end])
axes2[1].set_title('Cross: Clean-Periodic')
axes2[1].grid(True)
axes2[2].plot(lags, cross_noisy_periodic[plot_start:plot_end])
axes2[2].set_title('Cross: Noisy-Periodic')
axes2[2].set_xlabel('Lag (s)')
axes2[2].grid(True)
plt.tight_layout()
plt.show()
center_val = auto_clean[center] if len(auto_clean) % 2 == 1 else auto_clean[center-1]  
print("Auto peaks (lag ~0):", auto_clean[center], auto_noisy[center], auto_periodic[center])
print("Cross max abs peaks:", np.max(np.abs(cross_clean_noisy)), np.max(np.abs(cross_clean_periodic)), np.max(np.abs(cross_noisy_periodic)))
