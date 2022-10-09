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