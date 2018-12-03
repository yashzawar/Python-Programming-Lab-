import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
 
 

mu = 100 # mean of distribution
sigma = 15 # standard deviation of distribution
x = mu + sigma * np.random.randn(10000)
 
num_bins = 20

n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='blue', alpha=0.5)
 

y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')
 

plt.subplots_adjust(left=0.15)
plt.show()
