 # QBB2022 - Day 2 - Homework Excercises Submission
#!/usr/bin/env python3

import sys

def parse_vcf(fname): #define function parse_vcf to argument fname
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
                        Type = info_type[name] # change value into correct datatype. I want to dig more later!!
                        info[name] = type_map[Type](value)
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
		
		
		
		
		
		
		

# goal is to replace ID from db to random snippet if it has correct position
# make dictionaries position:id from dbSNP
# compare with random

first_file = "/Users/cmdb/qbb2022-answers/day2-homework/random_snippet.vcf"
second_file = "/Users/cmdb/qbb2022-answers/day2-homework.dbSNP_snippet.vcf"



from vcfParser import *
rand = parse_vcf('random_snippet.vcf')
fs = open('dbSNP_snippet.vcf', 'r')


from vcfParser import *
rand = parse_vcf('random_snippet.vcf')
fs = open('dbSNP_snippet.vcf', 'r')

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
    for k, v in snp: #TypeError: cannot unpack non-iterable int object
        print (k,v)