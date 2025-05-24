import numpy as np
from scipy.fftpack import dct, idct
from scipy.optimize import minimize

#Cosamp functions and Others


def cosamp(phi, u, s, epsilon=1e-10, max_iter=1000):
    """
    Return an `s`-sparse approximation of the target signal
    Input:
        - phi, sampling matrix
        - u, noisy sample vector
        - s, sparsity
    """
    a = np.zeros(phi.shape[1])
    v = u
    it = 0 # count
    halt = False
    while not halt:
        it += 1
        print("Iteration {}\r".format(it), end="")
        
        y = np.dot(np.transpose(phi), v)
        omega = np.argsort(y)[-(2*s):] # large components
        omega = np.union1d(omega, a.nonzero()[0]) # use set instead?
        phiT = phi[:, omega]
        b = np.zeros(phi.shape[1])
        # Solve Least Square
        b[omega], _, _, _ = np.linalg.lstsq(phiT, u)
        
        # Get new estimate
        b[np.argsort(b)[:-s]] = 0
        a = b
        
        # Halt criterion
        v_old = v
        v = u - np.dot(phi, a)

        halt = (np.linalg.norm(v - v_old) < epsilon) or \
            np.linalg.norm(v) < epsilon or \
            it > max_iter
        
    return a

#Reconstruction Methods

def reconstructSignal_dct(x, p, sparsity=10, epsilon=1.e-10,max_iter=10):
    '''
    x - original signal
    p - number of points to sample from the original signal
    
    implements signal reconstruction by Steve Brunton (Data Driven Science and Engineering)
    uses discrete cosine transform as basis function 
    '''

    n = len(x)
    perm = np.random.choice(np.arange(n), p, False)
    y = x[perm]
    ## Solve compressed sensing problem
    Psi = dct(np.identity(n)) # Build Psi
    Theta = Psi[perm,:]       # Measure rows of Psi
    
    s = cosamp(Theta,y,sparsity,epsilon=1.e-10,max_iter=10) # CS via matching pursuit
    xrecon = idct(s) # reconstruct full signal


    xrecont = np.fft.fft(xrecon)
    PSD = xrecont * np.conj(xrecont) / n # Power spectral density

    return xrecon, PSD, perm


def reconstructSignal_UniformSpacedSamples_dct(x, p, sparsity=10, epsilon=1.e-10,max_iter=10):
    '''
    x - original signal
    p - number of points to sample from the original signal
    
    implements signal reconstruction by sampling points at uniform spacing 
    (in this case, for accurate reconstruction, the sampling frequency must be 2 times the signal frequency)
    uses discrete cosine transform as basis function 
    '''

    n = len(x)
    perm = np.linspace(0, n-1, p).astype(int)
    y = x[perm]
    ## Solve compressed sensing problem
    Psi = dct(np.identity(n)) # Build Psi
    Theta = Psi[perm,:]       # Measure rows of Psi
    
    s = cosamp(Theta,y,sparsity,epsilon=1.e-10,max_iter=10) # CS via matching pursuit
    xrecon = idct(s) # reconstruct full signal

    xrecont = np.fft.fft(xrecon)
    PSD = xrecont * np.conj(xrecont) / n # Power spectral density

    return xrecon, PSD, perm


