### Signal reconstruction at sub-Nyquist Frequencies
Matt Bagnes, Lorenzo Joquino

To store and analyze signals accurately, we usually need to take samples very frequently, which can be costly. Steve Brunton\* discusses explores a smarter method where points are sampled at random intervals instead of at uniform intervals. This random sampling approach can still capture both the long-term and short-term characteristics of the signal, even with fewer samples. The sampled points can then be fitted in order to recreate the full signal. Our project tests the limits the reconstruction method based on the signal's complexity.

\*we reference code by Steve Brunton from the book Data Driven Science and Engineering.

#### Key Highlights 

<table>
  <tr>
    <td style="width:50%; vertical-align: top;">
      <p>
        1. For single-frequency waves, accurate reconstruction by random sampling can be performed at sampling frequencies 10 times fewer than the original signal's frequency.
      </p>
    </td>
    <td style="width:70%; text-align: right;">
      <img src="/readme_images_src_new/singleWaveStats.jpg" alt="drawing" width="600"/>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td style="width:10%; vertical-align: top;">
      <p>
        2. When more waves are added, the accurate reconstruction can still be performed when 5 more waves are added. Significant errors are observed beyond this complexity. The frequencies between each wave added are spaced by 60 Hz apart. The sampling frequency for reconstruction is \_ Hz. 
      </p>
    </td>
    <td style="width:90%; text-align: right;">
     <img src="/readme_images_src_new/increasingNumberOfWavesPSD.jpg" alt="drawing" width="1700"/>
    </td>
  </tr>
</table>


3. When the spacing of these added waves is larger or smaller, the accuracy changes 
 

### Possible Extenstions 
- Filtering Audio 


