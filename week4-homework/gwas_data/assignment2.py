#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt

eigenvec = np.genfromtxt("plink.eigenvec", dtype = None, encoding = None, names = ["family_id", "sample_id", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

fig, ax = plt.subplots()


ax.scatter(eigenvec["1"], eigenvec["2"])
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
# ax.legend()
ax.title.set_text('PCA analysis')
plt.savefig("PC1vs2.png")
plt.show()