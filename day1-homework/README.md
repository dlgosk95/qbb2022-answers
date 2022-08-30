# qbb 2022 day 1 homework

# !/bin/bash
#USAGE: bash exercise1.sh input_VCF

vcffile=$1

for nuc in A C G T
do
  echo "Considering " $nuc 
  awk -v nuc="$nuc" '/^#/{next} {if ($4 == nuc) {print $5}}' $vcffile | sort | uniq -c
done


Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G
 
 Yes it answers if Reference is A (or c or g or T) how many there are alternative SNPs Transversion
 
 No promoter parts are not clear. I assume promoters to be including and upstream of TSS. 
 

 awk '{if ($4 == 1 || $4 == 2 || $4 == 3) {print}}' ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed > promoter.bed

 vcffile=/Users/cmdb/data/vcf_files/random_snippet.vcf
 promoter=/Users/cmdb/qbb2022-answers/day1-homework/promoter.bed

 bedtools intersect -a $vcffile -b $promoter -wa > intersect.vcf
 
 
 Exercise 3
 
 #!/bin/bash

 #USAGE: bash exercise3.sh input_VCF

 awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed
 
 if the beggining starts with #, skip
 print column 1 (begi, result of column2-1 (size), and column2 (end)
 export as variants.bed
 sort -k1,1 -k2,2n ~/data/bed_files/genes.bed >  genes.sorted.bed
 from ~/data/bed_files/genes.bed
 sort column 1 (end at column 1)
 and sort column 2 (end at column 2) numerically not alphabetically
 export as genes.sorted.bed
 bedtools closest -a variants.bed -b genes.sorted.bed
 use bedtools to find sorted genes that intersect or be closest to the variant
 
Error: unable to open file or unable to determine types for file
The error because variants.bed file format is delimited by space but it must be tab.
awk '/^#/{next} {print $1"\t"$2-1"\t"$2}' $1 > variants.bed

Error: Sorted input specified, but the file variants.bed has the following out of order record
It ran into the error while running because the previous file (variants.bed) is not sorted (out of order) and for some technical reason (Why??) it needs to be sorted first
awk '/^#/{next} {print $1"\t"$2-1"\t"$2}' $1 > variants.bed
sort -k1,1 -k2,2n variants.bed > variants.sorted.bed
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
bedtools closest -a variants.sorted.bed -b genes.sorted.bed > closest.bed


(base) [~/qbb2022-answers/day1-homework $]wc -l closest.bed 
10293 closest.bed
sort -k7 closest.bed | cut -f 7 | uniq -c | wc -l
200
the average is 10293/200
