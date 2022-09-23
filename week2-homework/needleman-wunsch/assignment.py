#!/usr/bin/env python3

import numpy as np
import sys
from fasta import readFASTA

# Write a script to perform global alignment between two sequences using a given scoring matrix and gap penalty. Your script will take four inputs:
# sys.arg [0] is my python file

score_name = np.loadtxt(sys.argv[2], max_rows = 1, dtype = str) 
length = len(score_name)
column = tuple(range(1,length))

fname = sys.argv[1] # A FASTA-style file containing two sequences to align
score = np.loadtxt(sys.argv[2], skiprows = 1, usecols = column) # A text file containing the scoring matrix you’d like to use for this alignment
gap_penalty = float(sys.argv[3]) # Should be negative
filepath = sys.argv[4]

# print(score_name)
# print (score)

input_sequences = readFASTA(open(fname))
# print (input_sequences)

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]

F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1)) # stores the score of each “optimal” sub-alignment
traceback = np.empty((len(sequence1)+1, len(sequence2)+1), dtype=str) # a traceback matrix that allows you to determine the optimal global alignment (as a path through this matrix).
# numpy array can be string

for i in range(len(sequence1)+1):
    F_matrix[i,0] = i*gap_penalty
for j in range(len(sequence2)+1):
    F_matrix[0,j] = j*gap_penalty
# print (F_matrix)

for i in range(len(sequence1)+1): # row
    traceback[i,0] = 'v'
for j in range(len(sequence2)+1):
    traceback[0,j] = 'h'
# print (traceback)

score_dictionary = {}
for i in range(len(score_name)):
    score_dictionary.update({score_name[i]:i})
# print (score_dictionary)
# M is 12

for i in range(1, len(sequence1)+1): # loop through rows
    for j in range(1, len(sequence2)+1): # loop through columns
        # print (i,j) # starts from 1 to legth+1
        # if sequence1[i-1] == sequence2[j-1]:
        d = F_matrix[i-1, j-1] + score[score_dictionary[sequence1[i-1]], score_dictionary[sequence2[i-1]]]
        h = F_matrix[i,j-1] + gap_penalty
        v = F_matrix[i-1,j] + gap_penalty
        maximum = max(d,h,v)
        F_matrix[i,j] = maximum
        if maximum == d:
            traceback[i,j] = 'd'
        elif maximum == h:
            traceback[i,j] = 'h'
        else:
            traceback[i,j] = 'v'

# print(F_matrix)
print(traceback)

# while condition (not at topleft)
# do something

# h is gap in sequence1
# v is gap in sequence2
# if h, we want '-' in sequence1
# if v, we want '-' in sequence2
# if d, we want the sequence1[] and sequence2

seq1_align = ''
seq2_align = ''

k = len(sequence1)
l = len(sequence2)

# print(sequence1[k-1])

while (k!=0 or l!=0):
    current_dir = traceback[k,l]
    if current_dir == 'd':
        seq1_align = sequence1[k-1] + seq1_align
        seq2_align = sequence2[l-1] + seq2_align
        k-=1
        l-=1
    if current_dir == 'h':
        seq1_align = '-' + seq1_align
        seq2_align = sequence2[l-1] + seq2_align
        l-=1
        print(sequence2[l-1])
        print(current_dir)
    if current_dir == 'v':
        seq2_align = '-' + seq2_align
        seq1_align = sequence1[k-1] + seq1_align
        k-=1

print (seq1_align) # incorrect
print (seq2_align)

print (len(seq1_align)) 
print (len(seq2_align)) 



# save seq1_align and seq2 align (and their ids) to output file
# print the number of gaps in each sequence
# print the score of the alignment == sum of scores???


f = open('filepath', 'a')
f.write(seq1_align)















# if sequence1[0] == sequence2[0]:
#     print(score[score_dictionary[sequence1[0]], score_dictionary[sequence2[0]]])

# print (F_matrix[len(sequence1),len(sequence2)])

# top = F_matrix[len(sequence1)-1,len(sequence2)]
# left = F_matrix[len(sequence1),len(sequence2)-1]
# topleft = F_matrix[len(sequence1)-1, len(sequence2)-1]
# maximum = max(top, left, topleft)
# print(maximum)


# if maximum == topleft:
#     traceback[len(sequence1), len(sequence2)] = "d"
# if maximum == top:
#     traceback[len(sequence1), len(sequence2)] = "v"
# if maximum == left:
#     traceback[len(sequence1), len(sequence2)] = "h"
# print(traceback[len(sequence1), len(sequence2)])











# (base) [~/qbb2022-answers/week2-homework/needleman-wunsch $]./assignment.py CTCF_38_M27_AA.faa BLOSUM62.txt -10 ./output.txt













