### Limits of signal reconstruction at sub-Nyquist Frequencies
Matt Bagnes, Lorenzo Joquino

To store and analyze signals accurately, we usually need to take samples very frequently, which can be costly. Steve Brunton\* discusses explores a method where points are sampled at random intervals instead of at uniform intervals. This approach can still capture both the long-term and short-term characteristics of the signal, even with fewer samples. The sampled points can then be fitted in order to recreate the full signal. Our project tests the limits the reconstruction method based on the signal's complexity.

#### Key Highlights 

<table style="height:40%">
  <tr>
    <td style="width:50%; vertical-align: top; padding-bottom: 20px;">
      <p>
        1. For single-frequency waves, reconstruction (ratio RMSE < 1) by random sampling is more accurate than uniform sampling - works for sampling frequencies 10 times fewer than the original signal's frequency.
      </p>
    </td>
    <td style="width:50%; text-align: right;">
      <img src="/readme_images_src_new/singleWaveStats.jpg" alt="drawing" width="500"/>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td style="width:10%; vertical-align: top;">
      <p>
        2. Accurate reconstruction occurs when the peaks coincide, which is observed when up to 5 more waves are added. Significant errors are observed beyond this complexity. The lowest frequency wave is 30 Hz. From there, we add frequencies at intervals of 60 Hz. The sampling frequency for reconstruction is 64 Hz. 
      </p>
    </td>
    <td style="width:90%; text-align: right;">
     <img src="/readme_images_src_new/PSD_sub_frequency.png" alt="drawing" width="2600"/>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td style="width:10%; vertical-align: top;">
      <p>
        3. Good reconstruction is achieved at various spacing, until the frequencies involved are much higher (x10) than the reconstruction sampling frequency. The sampling frequency for reconstruction 64 Hz. 
      </p>
    </td>
    <td style="width:90%; text-align: right;">
     <img src="/readme_images_src_new/PSD_sub_spacing.png" alt="drawing" width="1700"/>
    </td>
  </tr>
</table>
 
#### \*References
[Brunton, S. L., & Kutz, J. N. (2022). Data-Driven Science and Engineering: Machine Learning, Dynamical Systems, and Control (2nd ed.). Cambridge: Cambridge University Press.](https://databookuw.com/)



