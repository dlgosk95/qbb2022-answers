# QBB2022 repository

# QBB2022 - Day 1 - Lunch Exercises Submission

 1. I’m excited to learn Unix.
a.
 cp ~/data/bed_files/exons.chr21.bed .
 cp ~/data/bed_files/genes.chr21.bed .

b. 
13653/219
wc -l exons.chr21.bed
wc -l genes.chr21.bed
echo 13653/219 >> README.mds

c.
I would sort and collapse the same things using
sort filename | uniq -c
will tell us the number and the name

a.
cp ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed .

b.
cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed > column4
sort column4 | uniq -c 
 305 1
  17 10
  17 11
  30 12
  62 13
 228 14
 992 15
 678 2
  79 3
 377 4
 808 5
 148 6
1050 7
 156 8
 654 9
 
c.
Go through the first column and find the biggest number, which is 1050. Its second column is 7, so the state 7 comprises the largest fraction of the genome. 


a.
(base) [~/qbb2022-answers/day1-lunch $]cp ~/data/metadata_and_txt_files/integrated_call_samples.panel .

b.
(base) [~/qbb2022-answers/day1-lunch $]grep AFR integrated_call_samples.panel | cut -f 2 | uniq -c
 90 ACB
   6 GWD
  31 ACB
  12 GWD
   2 ACB
 126 GWD
  33 ESN
  21 GWD
  35 MSL
  70 ESN
   4 MSL
  12 GWD
  55 ESN
  65 MSL
  15 ESN
   3 GWD
  24 MSL
  77 YRI
  23 LWK
 129 YRI
  99 LWK
 112 ASW

c.
(base) [~/qbb2022-answers/day1-lunch $]sort -k 3 integrated_call_samples.panel | cut -f 3 | uniq -c
1044 AFR
 535 AMR
 673 EAS
 670 EUR
 661 SAS
   1 super_pop
a.
(base) [~/qbb2022-answers/day1-lunch $]cp ~/data/vcf_files/random_snippet.vcf .

b. 
(base) [~/qbb2022-answers/day1-lunch $]cut -f 13 random_snippet.vcf > HG00100.vcf

c.
(base) [~/qbb2022-answers/day1-lunch $]sort HG00100.vcf | uniq -c
9514 0|0
 127 0|1
 178 1|0
 181 1|1
   1 HG00100

d.
(base) [~/qbb2022-answers/day1-lunch $]cut -f 8 random_snippet.vcf | grep AF=1 | wc -l
      34

e.
6 times per row

f.
(base) [~/qbb2022-answers/day1-lunch $]cut -f 8 random_snippet.vcf | cut -d\; -f7
