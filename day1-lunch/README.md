# QBB2022 repository

# QBB2022 - Day 1 - Lunch Exercises Submission

 1. I am excited to learn Unix.
a.
change directory to day1-lunch
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
find #  of exons for each gene Sort Find what is most common

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
substract third and second columns to find the size
sort by state 
add the same state's size
and find the largest.

a.
(base) [~/qbb2022-answers/day1-lunch $]cp ~/data/metadata_and_txt_files/integrated_call_samples.panel .

b.
grep AFR integrated_call_samples.panel | cut -f 2 | sort -k 2 |  uniq -c 90 ACB
  123 ACB
  112 ASW
  173 ESN
  180 GWD
  122 LWK
  128 MSL
  206 YRI

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
