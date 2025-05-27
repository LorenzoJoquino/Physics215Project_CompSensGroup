### Signal reconstruction at sub-Nyquist Frequencies
Matt Bagnes, Lorenzo Joquino

1. To achieve accurate sampling of a signal, the sampling frequency must be at least twice as high as the highest relevant frequency in the signal - this is called the Nyquist Frequency. 
2. However, using a random sampling approach, we can **reduce sampling frequency** while still getting **accurate signal reconstruction**. This is very useful in **reducing cost for storing data**.
3. Our project tests the **limits** of this method of signal reconstruction. 

#### General Approach

1. Random-location sampling captures both short-term \(high frequency\) and long-term \(low frequency\) behavior of the signal. 
2. Signals can be expressed as a weighted sum of cosine waves of varying frequencies. We solve for these weights through linear algebra, fitting the sampled points in the *discrete cosine transform*. 
3. Code - we reference code by Steve Brunton from the book Data Driven Science and Engineering.

#### Key Highlights 

<table>
  <tr>
    <td style="width:30%; vertical-align: top;">
      <p>
        1. For single-frequency waves, accurate reconstruction by random sampling can be performed at sampling frequencies 10 times fewer than the original signal's frequency.
      </p>
    </td>
    <td style="width:70%; text-align: right;">
      <img src="/readme_images_src_new/singleWaveStats.jpg" alt="drawing" width="600"/>
    </td>
  </tr>
</table>

2. When more waves are added, the accurate reconstruction can still be performed when 5 more waves are added. Significant errors are observed beyond this complexity. 

<img src="/readme_images_src_new/increasingNumberOfWavesPSD.jpg" alt="drawing" width="800"/>


<table>
  <tr>
    <td style="width:10%; vertical-align: top;">
      <p>
        2. When more waves are added, the accurate reconstruction can still be performed when 5 more waves are added. Significant errors are observed beyond this complexity.
      </p>
    </td>
    <td style="width:90%; text-align: right;">
     <img src="/readme_images_src_new/increasingNumberOfWavesPSD.jpg" alt="drawing" width="1800"/>
    </td>
  </tr>
</table>


3. When the spacing of these added waves is larger or smaller, the accuracy changes 
 

### Possible Extenstions 
- Filtering Audio 


