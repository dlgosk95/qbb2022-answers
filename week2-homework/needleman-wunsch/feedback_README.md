Really really great work! There are just a few minor issues:

When you're filling in the F matrix, I think you have a small type for the `d` case. You should be checking `sequence1[i-1]` and `sequence2[j-1]`. (-0.25)

When you're doing traceback you should be using `elif` statements instead of `if` statements. As it stands right now, if there's a tie between any of these, you'll actually step backwards through the traceback matrix twice, and update the alignment twice. (no points deducted)

We also want you to print out the alignment statistics: number of gaps in each sequence, and the alignment score. Also, don't forget to upload the DNA and AA alignments in separate files (-2)

7.75/10
