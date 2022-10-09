Part 1

samtools view -b -q 10 D2_Sox2_R1.bam > D2_Sox2_R1_filtered.bam
or -o option for output
run for all 4 bam files
samtools view -b -q 10 D2_Sox2_R1_input.bam > D2_Sox2_R1_input_filtered.bam
samtools view -b -q 10 D2_Sox2_R2.bam > D2_Sox2_R2_filtered.bam
samtools view -b -q 10 D2_Sox2_R2_input.bam > D2_Sox2_R2_input_filtered.bam

parameter for the effective genome size
mice chromosome 17 genome size 
mm10 genome
95 Mb in length
mm: 1.87e9

target and control (input) samples.

to create a bedgraph of read pileups for the treatment and control conditions

macs2 callpeak -t D2_Sox2_R1_filtered.bam -c D2_Sox2_R1_input_filtered.bam -B -g 95e6 -n R1
macs2 callpeak -t D2_Sox2_R2_filtered.bam -c D2_Sox2_R2_input_filtered.bam -B -g 95e6 -n R2

bedtools intersect -wa -a R1_peaks.narrowPeak -b R2_peaks.narrowPeak > intersect_peaks.narrowPeak

THIS IS SOX2 PEAKS: 
(base) [~/qbb2022-answers/week5-homework $]wc -l intersect_peaks.narrowPeak 
     593 intersect_peaks.narrowPeak

THIS IS KLF4 PEAKS: 
(base) [~/qbb2022-answers/week5-homework $]wc -l D2_Klf4_peaks.bed 
      60 D2_Klf4_peaks.bed

THIS IS INTEERSECT PEAKS: 
bedtools intersect -wa -a intersect_peaks.narrowPeak -b D2_Klf4_peaks.bed > klf4_intersect.narrowpeak
(base) [~/qbb2022-answers/week5-homework $]wc -l klf4_intersect.narrowpeak 
      41 klf4_intersect.narrowpeak

What is the percentage of Klf4 peaks colocalized with Sox2?
41/60*100

cp ~/cmdb-quantbio/assignments/lab/ChIP-seq/extra_data/bdg_loader.py .
loads in and bins the bedgraph file data, returning the coordinates of each bin’s midpoint and the sum of read counts for that bin
the returned bin positions and values are cropped to include only those falling in the genomic window shown in the paper’s figure

cp ~/cmdb-quantbio/assignments/lab/ChIP-seq/extra_data/scale_bdg.py .
scaling the bedgraph files
by adjusting each value such that the mean signal is one read per base

python scale_bdg.py R1_treat_pileup.bdg scaled_R1.bdg

awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaled_R1.bdg > cropped_R1.bdg

sox2
klf4
h3k27ac_day0
h3k27ac_day0

D0_H3K27ac_treat.bdg
D2_H3K27ac_treat.bdg
D2_Klf4_treat.bdg

python scale_bdg.py D0_H3K27ac_treat.bdg scaled_D0.bdg
python scale_bdg.py D2_H3K27ac_treat.bdg scaled_D2.bdg
python scale_bdg.py D2_Klf4_treat.bdg scaled_Klf4.bdg

awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaled_D0.bdg > cropped_D0.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaled_D2.bdg > cropped_D2.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaled_Klf4.bdg > cropped_Klf4.bdg


Part 2

meme-chip
intersect_peaks.narrowPeak
300 strongest ChIP-seq peaks
awk
samtools faidx

conda activate meme
conda install -c conda-forge openmpi=4.1.4 -y
ln -s /Users/cmdb/data/genomes/mm10.fa ./

```
(meme) [~/qbb2022-answers/week5-homework $]sort -k5 -n -r intersect_peaks.narrowPeak > size_sorted_intersect_sox2.narrowpeak
(meme) [~/qbb2022-answers/week5-homework $]head -n300 size_sorted_intersect_sox2.narrowpeak > first_300.narrowpeak
(meme) [~/qbb2022-answers/week5-homework $]awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' first_300.narrowpeak > formated_300.narrowpeak
```

string:integer-integer/newline
chr17:35503729-35504323
-r, --region-file FILE
Read regions from a file. Format is chr:from-to, one per line.
ndex reference sequence in the FASTA format or extract subsequence from indexed reference sequence. If no region is specified, faidx will index the file and create <ref.fasta>.fai on the disk. If regions are specified, the subsequences will be retrieved and printed to stdout in the FASTA format.

```
(meme) [~/qbb2022-answers/week5-homework $]conda deactivate
(base) [~/qbb2022-answers/week5-homework $]samtools faidx mm10.fa -r formated_300.narrowpeak > samtools.fa
(meme) [~/qbb2022-answers/week5-homework $]conda activate meme
(meme) [~/qbb2022-answers/week5-homework $]meme-chip -maxw 7 samtools.fa
```


Part 3

tomtom ./motif_databases/MOUSE/HOCOMOCOv11_full_MOUSE_mono_meme_format.meme ./memechip_out/combined.meme

Query_ID	Target_ID	Optimal_offset	p-value	E-value	q-value	Overlap	Query_consensus	Target_consensus	Orientation
KLF4_MOUSE.H11MO.0.A	1	-6	3.88836e-06	1.16651e-05	2.33301e-05	7	TGGAGTGGGTGTGGC	GGGTGGG	-
SOX2_MOUSE.H11MO.0.A	2	-2	6.40402e-05	0.000192121	0.000384241	7	TCCTTTGTTATGCAAA	CTTTGTT	+
SOX2_MOUSE.H11MO.1.A	2	-3	5.72779e-07	1.71834e-06	3.43667e-06	7	TTCCTTTGTTCTG	CTTTGTT	+



