# QBB2022 - Day 2 - Homework Excercises Submission

Exercise 1
Comment on the VCF parser

```
#!/usr/bin/env python3

import sys

def parse_vcf(fname):
    vcf = []
    info_description = {}
    info_type = {}
    format_description = {}
    type_map = {
        "Float": float,
        "Integer": int,
        "String": str
        }
    malformed = 0

    try:
        fs = open(fname)
    except:
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr)

    for h, line in enumerate(fs):
        if line.startswith("#"):
            try:
                if line.startswith("##FORMAT"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            if fields[start:i].count("=") == 1:
                                name, value = fields[start:i].split('=')
                                if name == "ID":
                                    ID = value
                                elif name == "Description":
                                    desc = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    format_description[ID] = desc.strip('"')
                elif line.startswith("##INFO"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            if fields[start:i].count("=") == 1:
                                name, value = fields[start:i].split('=')
                                if name == "ID":
                                    ID = value
                                elif name == "Description":
                                    desc = value
                                elif name == "Type":
                                    Type = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    info_description[ID] = desc.strip('"')
                    info_type[ID] = Type
                elif line.startswith('#CHROM'):
                    fields = line.lstrip("#").rstrip().split("\t")
                    vcf.append(fields)
            except:
                raise RuntimeError("Malformed header")
        else:
            try:
                fields = line.rstrip().split("\t") #split column based tabs save into fields list (string)
                fields[1] = int(fields[1]) # make second column as integer and overwrite
                if fields[5] != ".": # if quality is not . make it a float
                    fields[5] = float(fields[5])
                info = {}
                for entry in fields[7].split(";"): #for every info in a list splited by ; 
                    temp = entry.split("=") # split by = to make tmeporary sublist of string
                    if len(temp) == 1: # if it only has one (key), keep the key with value None in info dictionary 
                        info[temp[0]] = None
                    else:
                        name, value = temp # make the 1st of temp as name and 2nd of temp as value. name = temp[0], value = temp[1]
                        Type = info_type[name] # change value into correct datatype. Info type is a dictionary made above ID:Type based on ##INFO. ex. AC : Integer
                        info[name] = type_map[Type](value) # if type is Integer -> int(value). info is a dictionary with name and value in correct data type
                fields[7] = info # replace info column with temporary info dictionary
                if len(fields) > 8: # if column 8 (format) exists 
                    fields[8] = fields[8].split(":") # split format column into a list and overrite
                    if len(fields[8]) > 1: # if format list has more than one value
                        for i in range(9, len(fields)): # for everything after column 9
                            fields[i] = fields[i].split(':') # make list by splitting with : (similiarly to format) and overwrite
                    else:
                        fields[8] = fields[8][0] # if we have only one value in list, just replace column 8 with it, keep it same
                vcf.append(fields)
            except:
                malformed += 1 # if any code fail, skip the line and add one to malformed count
    vcf[0][7] = info_description # we update vcf list with info and format lists
    if len(vcf[0]) > 8:
        vcf[0][8] = format_description
    if malformed > 0: # if we have any malformed, report the error
        print(f"There were {malformed} malformed entries", file=sys.stderr)
    return vcf # close function

if __name__ == "__main__": # making this scrip executable
    fname = sys.argv[1] # user input filename
    vcf = parse_vcf(fname) # run function on this file
    for i in range(10): # print 10 column 
        print(vcf[i])
```

Exercise 2

```
# goal is to replace ID from db to random snippet if it has correct position
# make dictionaries position:id from dbSNP
# compare with random snippet and replace
# counter if not replaced

first_file = "/Users/cmdb/qbb2022-answers/day2-homework/random_snippet.vcf"
second_file = "/Users/cmdb/qbb2022-answers/day2-homework.dbSNP_snippet.vcf"

from vcfParser import *
#import vcfParser and everytime call function vcfParser.parse_vcf
#from vcfParser import parse_vcf

rand = parse_vcf('random_snippet.vcf')
fs = open('dbSNP_snippet.vcf', 'r')
counter = 0

snp ={}
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

#counter is 78
```