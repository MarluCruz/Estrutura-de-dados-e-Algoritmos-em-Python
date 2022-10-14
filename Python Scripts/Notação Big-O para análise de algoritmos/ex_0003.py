from math import log
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace (1,10,100)
len(n)
n
np.ones(n.shape) # Constant
np.log(n) # Logarithmic
n # Linear
n*np.log(n) # #Log Linear
n**2 # Quadratic
n**3 # Cubic
2**n # Exponential
labels = ['Constant', 'Logarithmic', 'Linear', 'Log linear', 'Quadratic', 'Cubic', 'Exponential']
big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n**2, n**3, 2**n]
plt.figure(figsize=(10,8))
plt.ylim(0,100)
for i in range(len(big_o)):
    plt.plot(n, big_o[i], label =labels[i])
plt.legend
plt.ylabel('Runtime')
plt.xlabel('n')