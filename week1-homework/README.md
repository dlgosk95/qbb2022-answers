Question 1. Coverage simulator

Question 1.1. How many 100bp reads are needed to sequence a 1Mbp genome to 5x coverage? How many are needed for 15x coverage?
1000000*5/100=50000
1000000*15/100=150000


Question 1.2. Write a program (in Python) to simulate sequencing 5x coverage of a 1Mbp genome with 100bp reads. The output of this simulation should be an array of length 1 million, where each element in the array is the coverage at that base (i.e. a count of the number of reads that overlapped that base’s position). You do not actually need to consider the sequence of the genome or the strand of the reads. Using this array, plot a histogram of the coverage. Then, overlay the histogram with a Poisson distribution with lambda=5.

See the script question1_2.py
See the image histogram.png and with_poisson2.png

I have some questions written within the script, particularly about bin


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

See the script question1_4.py
See the image histogram2.png and with_poisson2.png

Question about with_poisson2.png because poisson is much lower than histogram. Should I multiply by 15?

```
array = np.array(x) # make list into array
zero = array[np.where(array == 0)]
print(zero.size) # gives 6

y = poisson.pmf(0, mu=15)*1000000
print (y) # 0.3059023205018258
```

Very close. off by about 6.



Question 2. De novo assembly

```
(base) [~/qbb2022-answers/week1-homework/asm $]~/qbb2022-answers/week1-homework/asm/SPAdes-3.15.5-Darwin/bin/spades.py --pe1-1 frag180.1.fq --pe1-2 frag180.2.fq --mp1-1 jump2k.1.fq --mp1-2 jump2k.2.fq -o asm -t 4 -k 31

Question 2.1. How many contigs were produced? [Hint: try grep -c '>' contigs.fasta]
(base) [~/qbb2022-answers/week1-homework/asm/asm $]grep -c '>' contigs.fasta
4
```


Question 2.2. What is the total length of the contigs? [Hint: try samtools faidx, plus a short script if necessary]

```
(base) [~/qbb2022-answers/week1-homework/asm/asm $]samtools faidx contigs.fasta
(base) [~/qbb2022-answers/week1-homework/asm/asm $]less -S contigs.fasta.fai 
NODE_1_length_105830_cov_20.649193      105830  36      60      61
NODE_2_length_47860_cov_20.367392       47860   107665  60      61
NODE_3_length_41351_cov_20.528098       41351   156358  60      61
NODE_4_length_39426_cov_20.336388       39426   198434  60      61
```

NAME	Name of this reference sequence
LENGTH	Total length of this reference sequence, in bases
OFFSET	Offset in the FASTA/FASTQ file of this sequence's first base
LINEBASES	The number of bases on each line
LINEWIDTH	The number of bytes in each line, including the newline
QUALOFFSET	Offset of sequence's first quality within the FASTQ file

```
(base) [~/qbb2022-answers/week1-homework/asm/asm $]awk '{SUM+=$2}{print SUM}' contigs.fasta.fai
105830
153690
195041
234467
(base) [~/qbb2022-answers/week1-homework/asm/asm $]awk '{SUM+=$2}END{print SUM}' contigs.fasta.fai
234467
```

The total length of the contigs is 234467bp.

# What is END??
# What is offset??


Question 2.3. What is the size of your largest contig? [Hint: check samtools faidx plus sort -n]

```
(base) [~/qbb2022-answers/week1-homework/asm/asm $]sort -k2 -n contigs.fasta.fai
NODE_4_length_39426_cov_20.336388	39426	198434	60	61
NODE_3_length_41351_cov_20.528098	41351	156358	60	61
NODE_2_length_47860_cov_20.367392	47860	107665	60	61
NODE_1_length_105830_cov_20.649193	105830	36	60	61
```

Node  1 is the largest contig with a legth of 105830bp.


Question 2.4. What is the contig N50 size? [Hint: Write a short script if necessary]

You have the longest contig first, then the second longest, and so on with the shortest ones in the end. Then you start adding up the lengths of all contigs from the beginning, so you take the longest contig + the second longest + the third longest and so on — all the way until you’ve reached the number that is making up 50% of your total assembly length. That length of the contig that you stopped counting at, this will be your N50 number.

Total is 234467. >50% is 117234.

```
(base) [~/qbb2022-answers/week1-homework/asm/asm $]awk '{SUM+=$2}{print SUM}' contigs.fasta.fai
105830
153690
195041
234467
```

N50 is 47860bp (the length of the second longest contig)



Question 3. Whole Genome Alignment

Question 3.1. What is the average identify of your assembly compared to the reference? [Hint: try dnadiff]

```
(base) [~/qbb2022-answers/week1-homework/asm/asm $]dnadiff ref.fa contigs.fasta
```

```
Output will be...
   out.report  - Summary of alignments, differences and SNPs
   out.delta   - Standard nucmer alignment output
   out.1delta  - 1-to-1 alignment from delta-filter -1
   out.mdelta  - M-to-M alignment from delta-filter -m
   out.1coords - 1-to-1 coordinates from show-coords -THrcl .1delta
   out.mcoords - M-to-M coordinates from show-coords -THrcl .mdelta
   out.snps    - SNPs from show-snps -rlTHC .1delta
   out.rdiff   - Classified ref breakpoints from show-diff -rH .mdelta
   out.qdiff   - Classified qry breakpoints from show-diff -qH .mdelta
   out.unref   - Unaligned reference sequence IDs and lengths
   out.unqry   - Unaligned query sequence IDs and lengths
```

```
(base) [~/qbb2022-answers/week1-homework/asm/asm $]less -S out.report 

                               [REF]                [QRY]
[Sequences]
TotalSeqs                          1                    4
AlignedSeqs               1(100.00%)           4(100.00%)
UnalignedSeqs               0(0.00%)             0(0.00%)

[Bases]
TotalBases                    233806               234467
AlignedBases          233755(99.98%)       233755(99.70%)
UnalignedBases             51(0.02%)           712(0.30%)

[Alignments]
1-to-1                             5                    5
TotalLength                   233755               233755
AvgLength                   46751.00             46751.00
AvgIdentity                   100.00               100.00
```

I am not sure what the question is asking. Average Identify? You mean Identity? 100?


Question 3.2. What is the length of the longest alignment [Hint: try nucmer and show-coords]

```
(base) [~/qbb2022-answers/week1-homework/asm/asm $]nucmer ref.fa contigs.fasta

(base) [~/qbb2022-answers/week1-homework/asm/asm $]less -S out.delta 
/Users/cmdb/qbb2022-answers/week1-homework/asm/asm/ref.fa /Users/cmdb/qbb2022-answers/week1-homework/asm/asm>
NUCMER
>Halomonas NODE_1_length_105830_cov_20.649193 233806 105830
127965 233794 1 105830 1 1 0
0
>Halomonas NODE_2_length_47860_cov_20.367392 233806 47860
40651 88510 1 47860 0 0 0
0
>Halomonas NODE_3_length_41351_cov_20.528098 233806 41351
3 26789 1 26787 0 0 0
0
26790 40641 27500 41351 0 0 0
0
>Halomonas NODE_4_length_39426_cov_20.336388 233806 39426
88532 127957 1 39426 0 0 0
0
```

The four coordinates are the start and end in the reference and the start and end in the query respectively. The three digits following the location coordinates are the number of errors (non-identities + indels), similarity errors (non-positive match scores), and stop codons (does not apply to DNA alignments, will be "0"). 

```
(base) [~/qbb2022-answers/week1-homework/asm/asm $]show-coords out.delta
/Users/cmdb/qbb2022-answers/week1-homework/asm/asm/ref.fa /Users/cmdb/qbb2022-answers/week1-homework/asm/asm/contigs.fasta
NUCMER

    [S1]     [E1]  |     [S2]     [E2]  |  [LEN 1]  [LEN 2]  |  [% IDY]  | [TAGS]
=====================================================================================
  127965   233794  |        1   105830  |   105830   105830  |    99.99  | Halomonas	NODE_1_length_105830_cov_20.649193
   40651    88510  |        1    47860  |    47860    47860  |   100.00  | Halomonas	NODE_2_length_47860_cov_20.367392
       3    26789  |        1    26787  |    26787    26787  |   100.00  | Halomonas	NODE_3_length_41351_cov_20.528098
   26790    40641  |    27500    41351  |    13852    13852  |   100.00  | Halomonas	NODE_3_length_41351_cov_20.528098
   88532   127957  |        1    39426  |    39426    39426  |   100.00  | Halomonas	NODE_4_length_39426_cov_20.336388
```

The length of the longest alignment is 105830.


Question 3.3. How many insertions and deletions are in the assembly? [Hint: try dnadiff]

```
(base) [~/qbb2022-answers/week1-homework/asm/asm $]less -S out.report 

Insertions                         5                    1
InsertionSum                      51                  712
InsertionAvg                   10.20               712.00

TotalBases                    233806               234467
AlignedBases          233755(99.98%)       233755(99.70%)
UnalignedBases             51(0.02%)           712(0.30%)
```

51 insertions in reference, 712 insertionn in query, no deletion



Question 4. Decoding the insertion

Question 4.1. What is the position of the insertion in your assembly? Provide the corresponding position in the reference. [Hint: try show-coords]
26788 to 27499 in NODE_3_length_41351_cov_20.528098


Question 4.2. How long is the novel insertion? [Hint: try show-coords]
712 bp


Question 4.3. What is the DNA sequence of the encoded message? [Hint: try samtools faidx to extract the insertion]

```
(base) [~/qbb2022-answers/week1-homework/asm/asm $]samtools faidx contigs.fasta NODE_3_length_41351_cov_20.528098:26788-27499
>NODE_3_length_41351_cov_20.528098:26788-27499
CGCCCATGCGTAGGGGCTTCTTTAATTACTTGATTGACGCATGCCCCTCGTTCTACATGT
CTAGCTTCGTAACTGCCCCGATTTATACAGGAGCATATGCGTTTCGTAGTGCCGGGAATG
CATACCAAAGGGCTCACGGCGGGTACGCCACAATGGCTCAAGTCGAAAATGAATCGAAGA
CAACAAGGAATACCGTACCCAATTACTCAAGGACCTCATACACCATCCCATGCTACTTAT
CTACAGACATACACGCCAGCACCCAGCAACCAAAGCACACCGACGATAAGACTACAATCG
CGATAAGCACAACTTACATTAGGAGGCCCGGCAAATCTTGACGGCGTTAAGTCCGACACG
AATACCCCCCGACAAAAGCCTCGTATTCCGAGAGTACGAGAGTGCACAAAGCACCAAGGC
GGGGCTTCGGTACATCCACCAGTAGTCCCGTCGTGGCGGATTTTCGTCGCGGATGATCCG
AGGATTTCCTGCCTTGCCGAACACCTTACGTCATTCGGGGATGTCATAAAGCCAAACTTA
GGCAAGTAGAAGATGGAGCACGGTCTAAAGGATTAAAGTCCTCGAATAACAAAGGACTGG
AGTGCCTCAGGCATCTCTGCCGATCTGATTGCAAGAAAAAATGACAATATTAGTAAATTA
GCCTATGAATAGCGGCTTTAAGTTAATGCCGAGGTCAATATTGACATCGGTA

(base) [~/qbb2022-answers/week1-homework/asm/asm $]samtools faidx contigs.fasta NODE_3_length_41351_cov_20.528098:26788-27499 > insertion.fasta
```

Question 4.4. What is the secret message? [Hint: Run the provided script dna-decode.py to decode the string from 4.3.]

```
(base) [~/qbb2022-answers/week1-homework/asm/asm $]chmod a+x dna-decode.py 
(base) [~/qbb2022-answers/week1-homework/asm/asm $]./dna-decode.py -d --input insertion.fasta 
The decoded message :  Congratulations to the 2021 CMDB @ JHU class!  Keep on looking for little green aliens...
```
