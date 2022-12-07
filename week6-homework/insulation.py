#!/usr/bin/env python

import sys

import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def remove_dd_bg(mat):
    N = mat.shape[0]
    mat2 = numpy.copy(mat)
    for i in range(N):
        bg = numpy.mean(mat[numpy.arange(i, N), numpy.arange(N - i)])
        mat2[numpy.arange(i, N), numpy.arange(N - i)] -= bg
        if i > 0:
            mat2[numpy.arange(N - i), numpy.arange(i, N)] -= bg
    return mat2

def smooth_matrix(mat):
    N = mat.shape[0]
    invalid = numpy.where(mat[1:-1, 1:-1] == 0)
    nmat = numpy.zeros((N - 2, N - 2), float)
    for i in range(3):
        for j in range(3):
            nmat += mat[i:(N - 2 + i), j:(N - 2 + j)]
    nmat /= 9
    nmat[invalid] = 0
    return nmat

in1_40kb_fname = '/Users/cmdb/qbb2022-answers/week6-homework/matrix/dCTCF_full.40000.matrix'
# bin_40kb_fname = '/Users/cmdb/qbb2022-answers/week6-homework/matrix/40000_bins.bed'

data_40kb = numpy.loadtxt(in1_40kb_fname, dtype=numpy.dtype([('F1', int), ('F2', int), ('score', float)]))#
# frags_40kb = numpy.loadtxt(bin_40kb_fname, dtype=numpy.dtype([('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))

start_bin = 54878
end_bin = 54951+1

data_40kb_filtered = data_40kb[numpy.where((data_40kb['F1']>=start_bin) & (data_40kb['F2']<end_bin))[0]]

# print(data_40kb_filtered)

## Log-transform the scores (the dynamic range of data makes it hard to visualize the non-transformed data).

for i in range(len(data_40kb_filtered)):
    data_40kb_filtered[i][2] = numpy.log(data_40kb_filtered[i][2])

## Also, shift the data by subtracting the minimum value so the new minimum value is zero (this will prevent issues where there is missing information)

minimum40kb = data_40kb_filtered[0][2]
for i in range(len(data_40kb_filtered)):
    if data_40kb_filtered[i][2]< minimum40kb:
        minimum40kb = data_40kb_filtered[i][2]

for i in range(len(data_40kb_filtered)):
    data_40kb_filtered[i][2] = data_40kb_filtered[i][2] - minimum40kb
    data_40kb_filtered[i][0] = data_40kb_filtered[i][0] - 54878
    data_40kb_filtered[i][1] = data_40kb_filtered[i][1] - 54878
# print(data1_filtered)
# print (len(data_40kb_filtered))

## Convert the sparse data into a square matrix (note that the sparse data only contains one entry per interaction with the lower-numbered bin in the first column). By converting the sparse matrix it into a complete matrix for plotting, you have two entries per interaction. For one line of the sparse data format, the data relates to the full matrix as follows:

empty40kb = numpy.zeros((54951+1-54878,54951+1-54878))

empty40kb[data_40kb_filtered['F1'], data_40kb_filtered['F2']] = data_40kb_filtered['score']
empty40kb[data_40kb_filtered['F2'], data_40kb_filtered['F1']] = data_40kb_filtered['score']
print(empty40kb)
# print(54951+1-54878) ## 74

print(len(empty40kb))

insulation = numpy.zeros((len(empty40kb),))
for i in range(2, len(empty40kb)-2):
    insulation[i] = numpy.mean(empty40kb[(i - 2):(i + 2), (i - 2):(i + 2)])
    # for j in range(2, len(empty40kb)-3):
    #     if i==j:
    #         insulation[i-2] = numpy.mean(empty40kb[(i - 2):(i + 2), (j - 2):(j + 2)])
# print(insulation)
insulation[0] = numpy.nan
insulation[1] = numpy.nan
insulation[-1] = numpy.nan
insulation[-2] = numpy.nan
insulation[-3] = numpy.nan
x = numpy.arange(0, len(empty40kb), 1)
print(x)
y = insulation

print(13400000-10400000)

fig, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(5,6.25))
ax[0].axis('off')
plt.margins(x=0)
# ax[1].set_xlim(10400000, 13400000)
plt.subplots_adjust(left=0.15, bottom=0.1, right=1.0, top=1.0, wspace=0.4, hspace=0.0)
ax[0].imshow(empty40kb,cmap = "magma_r", vmax = 7)
ax[1].plot(x, y)
ax[1].set_xlabel("Base Pair on Chromosome 15")
ax[1].set_ylabel("Insulation Score")
ax[1].set_xticks(numpy.arange(0,74+1, 74/6), numpy.arange(10400000, 13400000+1, 500000))
plt.xticks(rotation = 45)
fig.tight_layout()
plt.savefig("insulation.png")
plt.show()

# fig, ax = plt.subplots(2,1)
# ax[0].imshow(empty40kb,cmap = "magma_r", vmax = 4)
# ax[1].plot(x,y)
# plt.show()
