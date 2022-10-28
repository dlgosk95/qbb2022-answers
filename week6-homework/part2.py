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


# in1_fname, in2_fname, bin_fname, out_fname = sys.argv[1:5]
in1_fname = '/Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix'
in2_fname = '/Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix'
bin_fname = '/Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed' 

data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([('F1', int), ('F2', int), ('score', float)]))
data2 = numpy.loadtxt(in2_fname, dtype=numpy.dtype([('F1', int), ('F2', int), ('score', float)]))
frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))

chrom = b'chr15'
start = 11170245
end = 12070245
start_bin = frags['bin'][numpy.where((frags['chr'] == chrom) & (frags['start'] <= start) & (frags['end'] > start))[0][0]]
end_bin = frags['bin'][numpy.where((frags['chr'] == chrom) & (frags['start'] <= end) & (frags['end'] > end))[0][0]] + 1

length =  end_bin - start_bin
# print(start_bin)
# print(end_bin)
# print (length) 
## 141

# print (data1)

## Filter out data with one or both interaction ends falling outside the desired bin range
## cut the in1 in2 matrix with start_bin and end_bin
## in1 dCTCF_ontarget_6400_iced.matrix
## in2 ddCTCF_ontarget_6400_iced.matrix

# print(numpy.where((data1['F1']>=start_bin) & (data1['F2']<=end_bin))[0])

## & is running two ((data1['F1']>=start_bin) and (data1['F2']<=end_bin)) siulatenously row-wise comparison
## np.where gives tuple ([], []) although it should be one dimensioal.

data1_filtered = data1[numpy.where((data1['F1']>=start_bin) & (data1['F2']<end_bin))[0]]
data2_filtered = data2[numpy.where((data2['F1']>=start_bin) & (data2['F2']<end_bin))[0]]
# print(data1_filtered)

## Log-transform the scores (the dynamic range of data makes it hard to visualize the non-transformed data).

# print(data1_filtered[0][2])
# print(numpy.log(data1_filtered[0][2]))

for i in range(len(data1_filtered)):
    data1_filtered[i][2] = numpy.log(data1_filtered[i][2])
# print(data1_filtered)
for i in range(len(data2_filtered)):
    data2_filtered[i][2] = numpy.log(data2_filtered[i][2])

# numpy.savetxt("log_data1.txt", data1_filtered)

## Also, shift the data by subtracting the minimum value so the new minimum value is zero (this will prevent issues where there is missing information)

minimum1 = data1_filtered[0][2]
for i in range(len(data1_filtered)):
    if data1_filtered[i][2] < minimum1:
        minimum1 = data1_filtered[i][2]

minimum2 = data2_filtered[0][2]
for i in range(len(data2_filtered)):
    if data2_filtered[i][2] < minimum2:
        minimum2 = data2_filtered[i][2]

# print(minimum1)
# print(minimum2)

minimum_column0 = data1_filtered[0][0]
minimum_column1 = data1_filtered[0][0]

for i in range(len(data1_filtered)):
    data1_filtered[i][2] = data1_filtered[i][2] - minimum1
    data1_filtered[i][0] = data1_filtered[i][0] - minimum_column0
    data1_filtered[i][1] = data1_filtered[i][1] - minimum_column1
# print(data1_filtered)
for i in range(len(data2_filtered)):
    data2_filtered[i][2] = data2_filtered[i][2] - minimum2
    data2_filtered[i][0] = data2_filtered[i][0] - minimum_column0
    data2_filtered[i][1] = data2_filtered[i][1] - minimum_column1
# print (data2_filtered)

## Convert the sparse data into a square matrix (note that the sparse data only contains one entry per interaction with the lower-numbered bin in the first column). By converting the sparse matrix it into a complete matrix for plotting, you have two entries per interaction. For one line of the sparse data format, the data relates to the full matrix as follows:

## make matrix 141x141
empty1 = numpy.zeros((length,length))
empty2 = numpy.zeros((length,length))

empty1[data1_filtered['F1'], data1_filtered['F2']] = data1_filtered['score']
empty1[data1_filtered['F2'], data1_filtered['F1']] = data1_filtered['score']
# print(empty1)

empty2[data2_filtered['F1'], data2_filtered['F2']] = data2_filtered['score']
empty2[data2_filtered['F2'], data2_filtered['F1']] = data2_filtered['score']
# print(empty2)

empty3 = numpy.subtract(smooth_matrix(empty2), smooth_matrix(empty1))
remove_dd_bg(empty3)

# print(empty3)

# numpy.savetxt("data1_matrix.txt", empty1)

## Plot the two matrices using the same maximum value (set vmax in imshow). I suggest using the magma color map, although you need to flip your scores to mimic the paper figure

fig, ax = plt.subplots(1, 3)

ax[0].imshow(empty1, cmap = "magma_r", vmax = 4)
ax[1].imshow(empty2, cmap = "magma_r", vmax = 4)
ax[2].imshow(empty3, cmap = "seismic", norm = colors.CenteredNorm())

## labeling
plt.savefig("three_plots_subsampled.png")
plt.show()




