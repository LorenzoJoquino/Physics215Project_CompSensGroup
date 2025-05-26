import numpy as np 
import pandas as pd 
import matplotlib.pyplot 

def saveNumpyArray(filepath, arrayToSave):
    np.savetext(filepath, arrayToSave, delimiter=',')
    return

def readNumpyArray(filepath):
    return np.loadtext(filepath, delimiter=',', dtype=float)