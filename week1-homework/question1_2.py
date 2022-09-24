#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

x = [0] * 1000000 # 1 million bp
np.random.seed(1)
place = np.random.randint(low = 0, high = 999900, size = 50000) # For a genome of length 1Mbp, and reads of length 100, the possible start positions are 0 through 999,900. # of reads is 1000000*5/100=50000
for i in range(len(place)): # 0 to 49999
    for j in range(100): # 0 to 99
        x[place[i]+j] +=1

# print (x)

fig1, ax1 = plt.subplots()
<<<<<<< Updated upstream
ax1.hist(x, bins = np.arange(0, max(x) + 1, 1)) 
# bins=np.arange(min(data), max(data) + binwidth, binwidth
=======
ax1.hist(x, bins = range(min(x), max(x) + 1, 1)) # ideal bin number
>>>>>>> Stashed changes
ax1.set_xticks(np.arange(0, 21, 1))
plt.xlim(0, 20)
ax1.set_xlabel("Coverage") # a count of number of reads that overlaps the base's position. number of time reads overlap that position. k
ax1.set_ylabel("Count")


plt.show() # to show and then reset plt
fig1.savefig("histogram.png") # plt.savefig must go before show because show will free all memory. plt is whatever the matplot is working with most recently.
plt.close(fig1) # to clear memory?

fig2, ax2 = plt.subplots()
#PMF f(k;u)=P(X=k)= (e^-u *u^k)/ k!
#pmf(k, mu, loc=0)
# creating a numpy array for x-axis
k = np.arange(0, 21, 1)
# poisson distribution data for y-axis
# probability of observing each coverage * total = frequency count ??
y = poisson.pmf(k, mu=5)*1000000
# plotting the graph
ax2.hist(x, bins = np.arange(0, max(x) + 1, 1))
ax2.plot(k, y)
ax2.scatter(k, y, color = 'red')

ax2.set_xticks(np.arange(0, 21, 1))
ax2.set_xlabel("k") # is this same as coverage??
ax2.set_ylabel("Count")

plt.xlim(0, 20)

plt.savefig("with_poisson.png")
plt.show()
plt.close()







# x = [0] * 100
# place = np.random.randint(low = 0, high = 99, size = 5)
# for i in range (5): # 0, 1, 2, 3, 4
#     for j in range (3): # 0, 1, 2
#         x[place[i]+j] +=1
# print (x)