import numpy as np

def rmse(signal_orig, signal_recon):
    error = np.sqrt(np.mean((signal_orig - signal_recon) ** 2))
    return error

def normalized_rmse(signal_orig, signal_recon):
    rmseOrigRecon = rmse(signal_orig, signal_recon)

    zeroArray = np.zeros_like(signal_orig)
    rmseNormFactor = rmse(signal_orig, zeroArray)

    return rmseOrigRecon/rmseNormFactor