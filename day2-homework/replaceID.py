#!/usr/vin/env python

# goal is to replace ID from db to random snippet if it has correct position
# make dictionaries position:id from dbSNP
# compare with random snippet and replace
# counter if not replaced

first_file = "/Users/cmdb/qbb2022-answers/day2-homework/random_snippet.vcf"
second_file = "/Users/cmdb/qbb2022-answers/day2-homework.dbSNP_snippet.vcf"



from vcfParser import *
#import vcfParser and everytime call function vcfParser.parse_vcf
#from vcfParser import parse_vcf
rand = parse_vcf('random_snippet.vcf') # read in random_snippet.vcf
fs = open('dbSNP_snippet.vcf', 'r')
counter = 0

snp ={} # smake empty dictionary
for i, line in enumerate(fs):
    if line.startswith("#"):
        continue
    else:
        fields = line.strip().split('\t')
        fields[1] = int(fields[1])
        position = fields[1]
        identification = fields[2]
        snp[position]=identification
#print (snp)

#for position, identification in snp.items(): 

#for position in snp.keys():
#   if position == rand[1][1]:
#       rand[1][2] = identification
#   else:
#       continue

#very inefficient because it has to go through all length of dictionary(n) as well as vcf (m) so it ran n*m 



for i in range(1,len(rand)):
    record = rand[i]
    pos = record [1]
    #if pos in snp:
        #iden = snp[pos]
        #rand[i][2] = iden
    try:
        rand[i][2] = snp[pos]
    except:
        counter+=1

print (rand, counter)