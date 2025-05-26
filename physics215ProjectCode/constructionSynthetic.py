import numpy as np

def constructSyntheticSignal(n, f_a_orig, t_end=1):
    '''
    constructs a sine wave signal 
    n = number of data points to construct original signal
    if f_a_orig is 'int':
        wave of frequency f_a_orig has amplitude 1 
    if f_a_orig is 'list':
        wave of frequencies in f_a_orig will all have amplitude 1
    if f_a_orig is 'dict':
        wave of frequencies in the keys with value being the corresponding amplitude
        Ex. constructSyntheticSignal(4096, {3:1, 15:2}, t_end=1) #constructs 4096 sample points of 
        wave of frequency 3 with amplitude 1 and freq 15 with amp 2

    set t_end to 1 so that n is the sampling frequency
    '''
    if type(f_a_orig).__name__ == "int":
        t = np.linspace(0,t_end,n)
        x = np.cos(2 * f_a_orig * np.pi * t)
        xt = np.fft.fft(x) # Fourier transformed signal
        PSD = xt * np.conj(xt) / n # Power spectral density

        return x, PSD, t

    elif type(f_a_orig).__name__ == "list":
        x = 0
        t = np.linspace(0,t_end,n)
        for f in f_a_orig:
            x += np.cos(2 * f * np.pi * t)
            xt = np.fft.fft(x) # Fourier transformed signal
            PSD = xt * np.conj(xt) / n # Power spectral density

        return x, PSD, t

    elif type(f_a_orig).__name__ == "dict":
        x = 0
        t = np.linspace(0,t_end,n)
        for f in f_a_orig:
            x += f_a_orig[f]*np.cos(2 * f * np.pi * t)
            xt = np.fft.fft(x) # Fourier transformed signal
            PSD = xt * np.conj(xt) / n # Power spectral density

        return x, PSD, t

def getPSD(x):
    xt = np.fft.fft(x) # Fourier transformed signal
    PSD = xt * np.conj(xt) / len(x)
    return PSD