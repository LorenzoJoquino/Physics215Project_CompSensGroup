## How does signal compression work with random sampling?

1. In the context of our work, a signal can be thought of as a 1-D column vector of length $n$. 
2. A signal $a$ can be decomposed into a weighted sum of a single-frequency cosine/sine functions. To be able to bypass the trigonometry, we work with fourier transforms. In the linear algebra sense, we are multiplying the weights $v$ of the cosine functions to the discrete cosine transform of an identity matrix $C$.
   
$$ a = Cv $$

- we note that $a$ in our study is a $n=4096$ long array. Thus $C$ is of shape $4096$ by $4096$, and $v$ is also 1-D with length $4096$ as well.

4. Now, when we perform random sampling from $a$, we are effectively "removing" rows from $a$. Let us call this random sampled signal $b$ a 1-D column vector of $p$ rows. This means $n-p$ rows were "removed". 

5. Consequently, when we perform the equation in 3, we are also removing rows from $C$. However, $v$ is still a 4096 long array. $C$ is a $p$ row by $n$ column rectangular matrix.

$$ b_{p\ rows} = C_{p\ by\ n} \times v_{n\ rows} $$

6. The goal of the algorithm is to find $v_{best}$ such that $Cv$ minimizes $b$. This algorithm will repeat, by finding a different $v$. The algorithm ends when the difference in the calculated $b$ in the previous iteration.  

7. However, ones the algorithm finds this $v_{best}$, we know compare $Cv_{best}$ with $a$. We use methods such as calculating their root-mean-square errors, or by comparing their power spectrums. 

