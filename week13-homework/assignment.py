#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt

def simulation(p, pop):
    n = 2*pop
    freq_list = [p]
    while (p > 0) & (p < 1):
        p_next = np.random.binomial(n,p)/n
        freq_list.append(p_next)
        p = p_next
    return freq_list

def plot(p, pop, fname):
    y = simulation(p,pop)
    fig, ax = plt.subplots()
    x = range(len(y))
    plt.plot(x,y)
    ax.set_title("Wright Fisher simulation with population size of " + str(pop))
    ax.set_ylim(0,1)
    ax.set_ylabel("Allele Frequency")
    ax.set_xlabel("Number of Generations")
    plt.savefig(fname)
    plt.show()

def multiple(p, pop, sim_size):
    length = []
    for i in range(sim_size):
        freq_list = simulation(p, pop)
        length.append(len(freq_list))
    return length

## initial state of the population.
## We will suppose that the single site has two alleles labeled 0 and 1.


# p0 = float(sys.argv[1]) ## the probability of success or we can say the probability of selecting an A allele. the starting alle frequency
# pop = int(sys.argv[2]) ## the population size
p = 0.5
pop = 100
# n = 2*pop ## the initial number of alleles in the generation.
## i is the number of A allele
## the number of generation
# np.random.binomial(n,p0)

# plot(p, pop, 'part2.png')

fix, ax = plt.subplots()

# plt.hist(multiple(0.5, 100, 1000), bins= 100)
# ax.set_ylabel("Density")
# ax.set_xlabel("Number of Generation for Fixation")
# plt.savefig("part3.png")
# plt.show()


# population = [100, 1000, 10000, 100000, 1000000, 10000000]
# fixation = []
# for i in population:
#     avg = np.mean(multiple(0.5, i, 1))
#     fixation.append(avg)
# log_pop = np.log10(population)
# log_fix = np.log10(fixation)
# plt.scatter(log_pop, log_fix)
# ax.set_ylabel("Number of Generation for Fixation (Log10)")
# ax.set_xlabel("Population size (Log10)")
# ax.set_xticks([2, 3, 4, 5, 6,7])
# plt.savefig("part4.png")
# plt.show()

frequency = np.arange(0, 1, 0.1)
# print(frequency)
fixation = []
standard_dev = []
full_sims = []
for i in frequency:
    sim_part5 = multiple(i, 100, 100)
    full_sims.append(sim_part5)
    avg = np.mean(sim_part5)
    std = np.std(sim_part5)
    fixation.append(avg)
    standard_dev.append(std)
ax.set_title("Wright Fisher simulation with varing starting frequency and population size of 100")
ax.set_ylabel("Number of Generation for Fixation")
ax.set_xlabel("Starting Frequency")
# plt.violinplot(dataset=full_sims, positions=frequency) ## options width
# plt.scatter(frequency, fixation)
plt.errorbar(frequency, fixation, yerr=standard_dev)
plt.savefig("part5_1.png")
plt.show()


















