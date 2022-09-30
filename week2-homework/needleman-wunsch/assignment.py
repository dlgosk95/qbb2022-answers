#!/usr/bin/env python3

import numpy as np
import sys
from fasta import readFASTA

# Write a script to perform global alignment between two sequences using a given scoring matrix and gap penalty. Your script will take four inputs:
# sys.arg [0] is my python file

score_name = np.loadtxt(sys.argv[2], max_rows = 1, dtype = str) 
length = len(score_name)
column = tuple(range(1,length+1)) # range is exlusive last #.
# print (column)

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
# numpy array can be string but one word

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

# print(score_dictionary)
# print(score)
# print(score.shape)
for i in range(1, len(sequence1)+1): # loop through rows
    for j in range(1, len(sequence2)+1): # loop through columns
        # print (i,j) # starts from 1 to legth+1
        # if sequence1[i-1] == sequence2[j-1]:
        try:
            d = F_matrix[i-1, j-1] + score[score_dictionary[sequence1[i-1]], 
            score_dictionary[sequence2[j-1]]]
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
        except:
            print(score_dictionary[sequence1[i-1]])
            print(score_dictionary[sequence2[j-1]])
            quit()

# print(F_matrix)
# print(traceback)

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
    elif current_dir == 'h':
        seq1_align = '-' + seq1_align
        seq2_align = sequence2[l-1] + seq2_align
        l-=1
        # print(sequence2[l-1])
        # print(current_dir)
    elif current_dir == 'v':
        seq2_align = '-' + seq2_align
        seq1_align = sequence1[k-1] + seq1_align
        k-=1

print (seq1_id)
print (seq1_align)
print (seq2_id)
print (seq2_align)
print (seq1_align.count('-'))
print (seq2_align.count('-'))
print (F_matrix[len(sequence1),len(sequence2)])

# print (len(seq1_align))
# print (len(seq2_align))


# save seq1_align and seq2 align (and their ids) to output file
# print the number of gaps in each sequence
# print the score of the alignments


f = open(filepath, 'w')
f.write(seq1_id)
f.write('\n')
f.write(seq1_align)
f.write('\n')
f.write(seq2_id)
f.write('\n')
f.write(seq2_align)

f = open('additional_info.txt', 'w')
f.write('The number of gaps in sequence1')
f.write('\n')
f.write(str(seq1_align.count('-')))
f.write('\n')
f.write('The number of gaps in sequence2')
f.write('\n')
f.write(str(seq2_align.count('-')))
f.write('\n')
f.write('The score of the alignments')
f.write('\n')
f.write(str(F_matrix[len(sequence1),len(sequence2)]))


# (base) [~/qbb2022-answers/week2-homework/needleman-wunsch $]./assignment.py CTCF_38_M27_AA.faa BLOSUM62.txt -10 ./aa.txt

# (base) [~/qbb2022-answers/week2-homework/needleman-wunsch $]./assignment.py CTCF_38_M27_DNA.fna HOXD70.txt -300 ./dna.txt














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

# I mistakenly stashed these and git pulled.
    # modified:   week1-homework/README.md
    # modified:   week1-homework/histogram.png
    # modified:   week1-homework/question1_2.py
    # modified:   week1-homework/question1_4.py
    # modified:   week1-homework/with_poisson2.png













