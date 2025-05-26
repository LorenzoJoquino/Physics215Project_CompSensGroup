import numpy as np
from scipy.fftpack import dct, idct
import os
import sys
sys.path.append(os.path.join('..'))
# from cosamp_fn import cosamp
# from rmse import rmse
from physics215ProjectCode import error_fn
from physics215ProjectCode import cosamp_fn

def recon(n, p, freq_start, freq_end, increments):
    ## Generate signal, DCT of signal
    t = np.linspace(0,1,n)
    perm = np.floor(np.random.rand(p) * n).astype(int)

    # params
    # reg is for uniformly spaced above nyquist frequency
    # sub is sub nyquist
    orig_signal = []
    recon_reg = []
    recon_sub = []
    PSD_orig = []
    PSD_reg = []
    PSD_sub = []
    errors_reg = []
    errors_sub = []

    x = np.cos(2 * freq_start * np.pi * t) # signal

    # for regular nyquist sampling
    p_uniform = freq_end * 2 # double the highest signal frequency
    indices = np.linspace(0, n - 1, p_uniform, dtype=int)
    
    for addfreq in range(freq_start + increments, freq_end + increments + 1, increments):
        signal = x.copy()
        orig_signal.append(signal)
        # PSD of original signal
        xt = np.fft.fft(x) # Fourier transformed signal
        PSD = xt * np.conj(xt) / n # Power spectral density
        PSD_orig.append(PSD)

        # regular nyquist
        # Simulate normal sampling by selecting p DCT coefficients directly
        x_nyquist_samples = x[indices]
        x_dct = dct(x_nyquist_samples, norm='ortho')
        x_recon_reg = idct(x_dct, norm='ortho')
        recon_reg.append(x_recon_reg)

        xt_recon_reg = np.fft.fft(x_recon_reg,n) # computes the (fast) discrete fourier transform
        PSD_recon_reg = xt_recon_reg * np.conj(xt_recon_reg)/n # Power spectrum (how much power in each freq)
        PSD_reg.append(PSD_recon_reg)

        # sub-nyquist
        y = x[perm]
        
        Psi = dct(np.identity(n)) 
        Theta = Psi[perm,:]
        
        s = cosamp_fn.cosamp(Theta,y,10,epsilon=1.e-10,max_iter=10) 
        x_recon_sub = idct(s)
        recon_sub.append(x_recon_sub)

        xt_recon_sub = np.fft.fft(x_recon_sub,n) # computes the (fast) discrete fourier transform
        PSD_recon_sub = xt_recon_sub * np.conj(xt_recon_sub)/n # Power spectrum (how much power in each freq)
        PSD_sub.append(PSD_recon_sub)
        
        #calculating rmse of reconstructed signal
        # L = int(np.floor(n/2))

        indices = np.linspace(0, len(signal) - 1, len(x_recon_reg), dtype=int)
        downsampled_signal = signal[indices]

        error_reg = error_fn.normalized_rmse(downsampled_signal,x_recon_reg)
        error_sub = error_fn.normalized_rmse(signal,x_recon_sub)
        # error_reg = rmse(PSD[:L], PSD_recon_reg[:L])
        # error_sub = rmse(PSD[:L], PSD_recon_sub[:L])
        errors_reg.append(f"{error_reg.real:.5g}")
        errors_sub.append(f"{error_sub.real:.5g}")
        
        x += np.cos(2 * addfreq * np.pi * t)

    return orig_signal, recon_reg, recon_sub, PSD_orig, PSD_reg, PSD_sub, errors_reg, errors_sub

def make_signal(resolution, freq_start, freq_end, increments):
    t = np.linspace(0,1,resolution)
    signal = np.cos(2 * freq_start * np.pi * t)

    if increments == 0:
        return signal
    else:
        for addfreq in range(freq_start + increments, freq_end + increments + 1, increments):
            iter_signal = signal.copy()
            signal += np.cos(2 * addfreq * np.pi * t)
        return iter_signal

def nyquist_reconstruction(samples, signal):
    # for regular nyquist sampling
    indices = np.linspace(0, len(signal) - 1, samples, dtype=int)
    signal_samples = signal[indices]
    signal_dct = dct(signal_samples, norm='ortho')
    reconstruction = idct(signal_dct, norm='ortho')
    return reconstruction

def sub_nyquist_reconstruction(p, signal):
    perm = np.floor(np.random.rand(p) * len(signal)).astype(int)
    signal_samples = signal[perm]
    Psi = dct(np.identity(len(signal))) 
    Theta = Psi[perm,:]
    s = cosamp_fn.cosamp(Theta,signal_samples,10,epsilon=1.e-10,max_iter=10) 
    reconstruction = idct(s)
    return reconstruction

def PSD(signal):
    signal_t = np.fft.fft(signal)
    PSD = signal_t * np.conj(signal_t)/len(signal)
    return PSD