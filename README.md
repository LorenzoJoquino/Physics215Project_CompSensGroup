# Signal reconstruction at sub-Nyquist Frequencies
members: Matt Bagnes, Lorenzo Joquino

1. To achieve accurate sampling of a signal, the sampling frequency must be at least twice as high as the highest relevant frequency in the signal - this is called the Nyquist Frequency. 
2. However, using a random sampling approach, we can **reduce sampling frequency** while still getting **accurate signal reconstruction**. This is very useful in **reducing cost for storing data**.
3. Our project tests the **limits** of this method of signal reconstruction. 

## General Approach
1. Random sampling - the Nyquist Frequency condition applied to sampling at uniform spacing. When sampling is randomized, we can capture both short-term \(high frequency\) and long-term \(low frequency\) behavior of the signal. 
2. Basis Functions - We can express a signal as a weighted sum of cosine waves of varying frequencies. We solve for these weights through linear algebra when we reconstruct our signal 
3. Code - we use code by Steve Brunton from the book Data Driven Science and Engineering .
## Key Highlights 

1. For single-frequency waves accurate reconstruction by random sampling can be performed at sampling frequencies 10 times fewer than the original signal's frequency. 

<img src="/readme_images_src_new/singleWaveStats.jpg" alt="drawing" width="400"/>

2. When more waves are added, the accurate reconstruction can still be performed when 5 more waves are added. Significant errors are observed beyond this complexity. 


<img src="/readme_images_src_new/increasingNumberOfWavesPSD.jpg" alt="drawing" width="1000"/>

3. When the spacing of these added waves is larger or smaller, the accuracy changes 
- **x-axis is spacing between waves, y-axis is RMSE. Choose one p instead**.  

## Specific Approach (Talk all the equations)


## Possible Extenstions 
- Filtering Audio 


