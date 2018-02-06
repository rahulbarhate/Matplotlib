import matplotlib.pyplot as plt
import numpy as np


mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)

#print(s)

#Verifying the mean and the variance
#abs(mu - np.mean(s)) < 0.01
#abs(sigma - np.std(s, ddof=1)) < 0.01  // ddof=delta degrees of freedom
                                        #to know more about ddof : https://stackoverflow.com/questions/27600207/why-does-numpy-std-give-a-different-result-to-matlab-std


count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.show()
