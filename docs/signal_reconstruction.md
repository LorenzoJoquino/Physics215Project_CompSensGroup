## How does signal compression work with random sampling?

1. In the context of our work, a signal can be thought of as a 1-D column vector of length $n$. 
2. A signal $a$ can be decomposed into a weighted sum of a single-frequency cosine/sine functions. To be able to bypass the trigonometry, we work with fourier transforms. In the linear algebra sense, we are multiplying the weights $v$ of the cosine functions to the discrete cosine transform of an identity matrix $C$. 
   
$$ a = Cv $$

- we note that $a$ in our study is a $n=4096$ long array. Thus $C$ is of shape $4096$ by $4096$, and $v$ is also 1-D with length $4096$ as well.

4. Now, when we perform random sampling from $a$, we are effectively "removing" rows from $a$. Let us call this random sampled signal $b$ a 1-D column vector of $p$ rows. This means $n-p$ rows were "removed". 

- In the book, [Steve Brunton discusses](https://databookuw.com/page-2/page-13/) this random sampling through a screening matrix. However, code for this is depicted as (where variable y is $a$):

        #in reconstruct_signal.py, sub_nyquist_reconstruction function
        perm = np.random.choice(np.arange(n), p, False)

      ...
        y = x[perm]

- The advantage of random sampling vs uniform sampling is in the fact that random sampling is able to capture characteristics of the signal at different time scales because the distance between two sample points varies. In uniform sampling, the space between two sampled data points is the same; hence, behavior at time scales smaller than the time distance between sampled points may not be observed. 

5. Consequently, when we perform the equation in 3, we are also removing rows from $C$. However, $v$ is still a 4096 long array. $C$ is a $p$ row by $n$ column rectangular matrix.

$$ b_{p\ rows} = C_{p\ by\ n} \times v_{n\ rows} $$

6. The goal of the algorithm is to find $v_{best}$ such that $Cv$ minimizes $b$. This algorithm will repeat, by finding a different $v$. The algorithm ends when the difference in the calculated $b$ in the previous iteration. In solving the matrix equation, we use the least squares algorithm

        #in cosamp_fn.py, cosamp function
         b[omega], _, _, _ = np.linalg.lstsq(phiT, u)

7. Throughout the algorithm, sparsity is introduced. We assert that most signals can carry a few relevant frequencies with the rest being noise. To manifest this assumption of sparsity, we focus on the top 10-20 largest coefficients (per new iteration).

        #in cosamp_fn.py, cosamp function
        omega = np.argsort(y)[-(2*s):] # large components
        omega = np.union1d(omega, a.nonzero()[0])


9. However, ones the algorithm finds this $v_{best}$, we know compare $Cv_{best}$ with $a$. We use methods such as calculating their root-mean-square errors, or by comparing their power spectrums.

References: [Brunton, S. L., & Kutz, J. N. (2022). Data-Driven Science and Engineering: Machine Learning, Dynamical Systems, and Control (2nd ed.). Cambridge: Cambridge University Press.](https://databookuw.com/)