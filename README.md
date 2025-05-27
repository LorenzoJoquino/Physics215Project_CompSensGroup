# Compressing and storing data at sub-Nyquist Frequencies

## Motivation 
To achieve accurate sampling of a signal, the sampling frequency must be at least twice as high as the highest relevant frequency in the signal - this is called the Nyquist Frequency. However, using a random sampling approach, we can reduce this sampling frequency while still getting accurate signal reconstruction. This is very useful in reducing cost for storing data.

Our project tests the limits of this method of signal reconstruction. 

## General Approach
1. Random sampling - the Nyquist Frequency condition applied to sampling at uniform spacing. When sampling is randomized, we can capture both short-term \(high frequency\) and long-term \(low frequency\) behavior of the signal. 
2. Basis Functions - We can express a signal as a weighted sum of cosine waves of varying frequencies. We solve for these weights through linear algebra when we reconstruct our signal 
3. Sparse Approach - Signals normally have a few relevant signals \(while the rest are noise \). We introduce sparsity so that the weights can be dedicated to the most relevant frequencies in the signal 

## Key Highlights 

1. When this random sampling approach, accurate reconstruction can be performed at sampling frequencies \_ times fewer than the original frequency 
![single wave stats]<img src="/readme_images_src_new/singleWaveStats.jpg" alt="drawing" width="200"/>

- **I need a graph where the x-axis is the number of points used to sample, and the y-axis is the RMSE. Here you tried to reconstruct a single wave (preferably the 630 Hz wave only).**

2. When more waves are added, the accurate reconstruction can be performed at this sampling frequencies 
- **Graph where x-axis is the number of waves added, and the y-axis is the RMSE, and the several graphs where differing P is used**
- **Alternatively \(or even better\), x-axis is the number of waves added, y-axis is the p data points, and then color is the RMSE. Use color bar where it is white at small RMSE, and more shadier at larger RMSE.**

3. When the spacing of these added waves is larger or smaller, the accuracy changes 
- **x-axis is spacing between waves, y-axis is RMSE. Choose one p instead**.  

## Specific Approach (Talk all the equations)


## Possible Extenstions 
- Filtering Audio


