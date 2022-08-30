# feedback.md
# day1-lunch

All looks great! 

Not that important (the wording was a bit vague), but for the question 4c, rather than counting total samples per superpopulation, I think the question wanted you to consider each superpopulation in turn and count samples in the corresponding subpopulations.

Another minor tip is that in markdown files (.md), if you enclose code in triple backticks, it will format nicely on GitHub, e.g.:

```
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
```
