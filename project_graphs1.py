import easier_case as ez
from matplotlib import pyplot as plt
import numpy as np
X = [i for i in range(1,201)]
Y = [ez.c_val(i,i,i) for i in range(1,201)]
plt.subplot(1,2,1)
plt.plot(X,Y)
plt.title("convergence of c(n,n,n)")
#plt.legend()
plt.xlabel("value of n")
plt.ylabel("the ratio between expectation of preferential and binomial")

W=40
R=80
X = [i for i in range(1, 41)]
Y1 = [ez.variance(i,R,W) for i in range(1, 41)]
Y2 = [ez.var_of_bin(i,R,W) for i in range(1, 41)]
Y3 = [ez.var_of_hypergeo(i,R,W) for i in range(1, 41)]
plt.subplot(1,2,2)
plt.plot(X, Y1, label='var of bin')
plt.plot(X, Y2, label='var of pref')
plt.plot(X, Y3, label='var of hypergeo')
plt.xlabel('n - number of draws')
plt.ylabel('y - variance')
plt.title('variance of 3 distributions, W=40,R=40')
plt.legend()
plt.show()