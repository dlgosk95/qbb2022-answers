#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

# minor allele frequency

freq = np.genfromtxt("plink.frq", dtype = None, encoding = None, names = ["chr", "snp", "a1", "a2", "maf", "x", "y", "NCHROBS"])

# print(freq[1][4])

allele_freq = []
for i in range(1,len(freq)):
    allele_freq.append(float(freq[i][4]))

# print (allele_freq)

fig, ax = plt.subplots()
ax.hist(allele_freq)
ax.set_xlabel("Allele Frequency")
ax.set_ylabel("Count of Allele Frequency")
plt.savefig("allele_freq.png")
plt.xticks(rotation=30, ha='right') 
plt.show()
plt.close()

