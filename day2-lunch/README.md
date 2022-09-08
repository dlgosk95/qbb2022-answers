Exercise 1
```
#!/usr/bin/env python3

import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")

    bed = []
    field_types = [str, int, int, str, float, str, int, int]
    malformed = 0 # create a counter for malformed lines

    for i, line in enumerate(fs):
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)

        # check that we have 3-9 or 12 columns, but not 10 or 11 columns
        if fieldN < 3:
            print(f"Line {i} appears malformed", file=sys.stderr)
            continue
        try:
            # for files with 9 columns, verify that there are 3 integers for itemRGB (9th column)
            # 0. make sure the file we're working with ahs at least 9 column
            if fieldN >= 9:
                # 1. pull out the 9th column
                rgb = fields[8]
                # 2. convert 9th colum into a list
                rgb_list = rgb.split(',')
                # rgb_list looks like ["254", "0", "0"]
                # 3. convert every item of that list into an integer
                for m, item in enumerate(rgb_list):
                    # i : 0
                    # item : "254"
                    # rgb_list[0] = int("254") -> rgb_list[0] = 254
                    # 4. replace the 9th column with our list
                    rgb_list[m] = int(item)
                fields[8] = rgb_list
            # 0. only do this for files that have 12 columns
            if fieldN == 12:
                # 1. strip the extra comman from blockSsizes (column 11)
                # 2. convert colum 11 into a list
                # 3. convert column 12 into a list
                blockSizes = fields[10].rstrip(",").split(",")
                blockStarts = fields[11].rstrip(",").split(",")
                # blockSizes looks like : ["76", "140", "86", "211"]
                # blockStarts looks like : ["0", "749", "2587", "5136"]
                # convert items within blockSizes, blockStarts to integers
                for k, item in enumerate(blockSizes):
                    blockSizes[k] = int(item)
                # replace the 10th column  with our converted list
                fields[10] = blockSizes
                # convert items within blockSizes, blockStarts to integers
                for l, item in enumerate(blockStarts):
                    blockStarts[l] = int(item)
                # replace the 10th column  with our converted list
                fields[10] = blockStarts
                # 4. check that blockSizes and blockStarts length matches block count
                blockCount = int(fields[9])
                if len(blockStarts) != blockCount:
                    malformed += 1
                if len(blockSizes) != blockCount:
                    malformed += 1
            # if any of that fails, we want to increment our malformed_counter
            # replace 10th column with its integer version
            fields[9] = blockCount
        except:
            # Issue : it's not updating i? Solved - typo and making blockCount integer
            print(f"Line {i} appears malformed", file=sys.stderr)
            
        try:
            for j in range(min(len(field_types), len(fields))):
                fields[j] = field_types[j](fields[j])
                # if data type conversion works, append this correct line to the bed list
            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)

    fs.close()
    print(malformed)
    return bed

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
```

Exercise 2
```
#!/usr/bin/env python

from TA_bed_parser import parse_bed

parsed = parse_bed("hg38_gencodev41_chr21.bed")
block_count = []
for nested in parsed:
    block_count.append(nested[9])

block_count.sort()

print(block_count[len(block_count)//2])

# 3272 // 2 is 1636
# print(block_count[1636])
# gives 4.
```