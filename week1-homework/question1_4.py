#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

x = [0] * 1000000 # 1 million bp
np.random.seed(1)
place = np.random.randint(low = 0, high = 999900, size = 150000) # For a genome of length 1Mbp, and reads of length 100, the possible start positions are 0 through 999,900. # of reads is 1000000*15/100=150000
for i in range(len(place)): # 0 to 49999
    for j in range(100): # 0 to 99
        x[place[i]+j] +=1

# print (x)

fig1, ax1 = plt.subplots()
ax1.hist(x, bins = np.arange(0, max(x) + 1, 1)) # what is the best bin number??
ax1.set_xticks(np.arange(0, 31, 1))
plt.xlim(0, 30)
# what to label x axis?? k? Number of incidence? Number of events?
plt.savefig("histogram2.png") # savefig must go before show because show will free all memory
plt.show()
plt.close() # why do we use close?? to save memory?


fig2, ax2 = plt.subplots()
#PMF f(k;u)=P(X=k)= (e^-u *u^k)/ k!
#pmf(k, mu, loc=0)
# creating a numpy array for x-axis
k = np.arange(0, 31, 1)
# poisson distribution data for y-axis
# probability of observing each coverage * total = frequency count ??
y = poisson.pmf(k, mu=15)*1000000
# plotting the graph
ax2.hist(x, bins = np.arange(0, max(x) + 1, 1))
ax2.plot(k, y)
ax2.scatter(k, y, color = 'red')

ax2.set_xticks(np.arange(0, 31, 1))
ax2.set_xlabel("k") # is this same as coverage??
ax2.set_ylabel("Count")

plt.xlim(0, 30)

plt.savefig("with_poisson2.png")
plt.show()
plt.close()


array = np.array(x) # make list into array
zero = array[np.where(array == 0)]
print(zero.size) # gives 6

y = poisson.pmf(0, mu=15)*1000000
print (y) # 0.3059023205018258