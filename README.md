## Signal reconstruction at sub-Nyquist Frequencies
Matt Bagnes, Lorenzo Joquino

1. To achieve accurate sampling of a signal, the sampling frequency must be at least twice as high as the highest relevant frequency in the signal - this is called the Nyquist Frequency. 
2. However, using a random sampling approach, we can **reduce sampling frequency** while still getting **accurate signal reconstruction**. This is very useful in **reducing cost for storing data**.
3. Our project tests the **limits** of this method of signal reconstruction. 

### General Approach

1. Random sampling - the Nyquist Frequency condition applies to uniformly-spaced sampling. Random-location sampling captures both short-term \(high frequency\) and long-term \(low frequency\) behavior of the signal. 
2. Basis Functions - Signals can be expressed as a weighted sum of cosine waves of varying frequencies. We solve for these weights through linear algebra with the *discrete cosine transform*. 
3. Code - we reference code by Steve Brunton from the book Data Driven Science and Engineering.

### Key Highlights 

<table>
  <tr>
    <td style="width:40%; vertical-align: top;">
      <p>
        1. For single-frequency waves, accurate reconstruction by random sampling can be performed at sampling frequencies 10 times fewer than the original signal's frequency.
      </p>
    </td>
    <td style="width:60%; text-align: right;">
      <img src="/readme_images_src_new/singleWaveStats.jpg" alt="drawing" width="500"/>
    </td>
  </tr>
</table>

2. When more waves are added, the accurate reconstruction can still be performed when 5 more waves are added. Significant errors are observed beyond this complexity. 


<img src="/readme_images_src_new/increasingNumberOfWavesPSD.jpg" alt="drawing" width="1000"/>

3. When the spacing of these added waves is larger or smaller, the accuracy changes 
- **x-axis is spacing between waves, y-axis is RMSE. Choose one p instead**.  

### Specific Approach (Talk all the equations)


### Possible Extenstions 
- Filtering Audio 


