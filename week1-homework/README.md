Question 1. Coverage simulator

Question 1.1. How many 100bp reads are needed to sequence a 1Mbp genome to 5x coverage? How many are needed for 15x coverage?
1000000*5/100=50000
1000000*15/100=150000


Question 1.2. Write a program (in Python) to simulate sequencing 5x coverage of a 1Mbp genome with 100bp reads. The output of this simulation should be an array of length 1 million, where each element in the array is the coverage at that base (i.e. a count of the number of reads that overlapped that base’s position). You do not actually need to consider the sequence of the genome or the strand of the reads. Using this array, plot a histogram of the coverage. Then, overlay the histogram with a Poisson distribution with lambda=5.

```
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
ax1.hist(x, bins = 17) # what is the best bin number?? 20 has empty bin in the middle
ax1.set_xticks(np.arange(0, 21, 1))
plt.xlim(0, 20)
# what to label x axis?? k? Number of incidence? Number of events?
plt.savefig("histogram.png") # savefig must go before show because show will free all memory
plt.show()
plt.close() # why do we use close?? to save memory?


fig2, ax2 = plt.subplots()
#PMF f(k;u)=P(X=k)= (e^-u *u^k)/ k!
#pmf(k, mu, loc=0)
# creating a numpy array for x-axis
k = np.arange(0, 21, 1)
# poisson distribution data for y-axis
# probability of observing each coverage * total = frequency count ??
y = poisson.pmf(k, mu=5)*1000000
# plotting the graph
ax2.hist(x, bins = 17)
ax2.plot(k, y)
ax2.scatter(k, y, color = 'red')

ax2.set_xticks(np.arange(0, 21, 1))
ax2.set_xlabel("k") # is this same as coverage??
ax2.set_ylabel("Count")

plt.xlim(0, 20)

plt.savefig("with poisson.png")
plt.show()
plt.close()
```


Question 1.3. Using your output array of coverages from Q1.2, how much of the genome (e.g., how many base pairs) has not been sequenced (has 0x coverage)? How well does this match Poisson expectations?

```
#!/usr/bin/env python3

import sys
import numpy as np
from scipy.stats import poisson

x = [0] * 1000000 # 1 million bp
np.random.seed(1)
place = np.random.randint(low = 0, high = 999900, size = 50000) # For a genome of length 1Mbp, and reads of length 100, the possible start positions are 0 through 999,900. # of reads is 1000000*5/100=50000
for i in range(len(place)): # 0 to 49999
    for j in range(100): # 0 to 99
        x[place[i]+j] +=1
# print(type(x)) # list
array = np.array(x) # make list into array
zero = array[np.where(array == 0)]
print(zero.size) # array.size function gives 6992

y = poisson.pmf(0, mu=5)*1000000
print (y) # gives 6737.946999085467
```
It matches pretty well. off by about 255.


Question 1.4. Now repeat the analysis with 15x coverage: 
simulate the appropriate number of reads and compute coverage,
make a histogram, 
overlay a Poisson distribution with lambda=15,
compute the number of bases with 0x coverage, and
evaluate how well it matches the Poisson expectation.

```
Very close. off by about 6.


Question 2. De novo assembly

Question 2.1. How many contigs were produced? [Hint: try grep -c '>' contigs.fasta]















