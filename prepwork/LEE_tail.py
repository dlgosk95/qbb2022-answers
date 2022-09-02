import sys #import module
filename = sys.argv[1] #SET input filename
if len(sys.argv) > 2: #IF user-specified number of lines provided
  n_lines = int(sys.argv[2]) #SET the desired number of lines
else: #OTHERWISE
  n_lines = 10 #SET the desired number of lines to a default

#for a storage list for lines in the file
all_line = []
for line in open(filename):
    all_line.append(line)

#__ a subset of the storage list to be the last ____ items in the storage list
#slice
subset_line = all_line[(-1-n_lines):-1]


#for every line in the subset
for subset in subset_line:
    print(subset.strip('\r\n')) #PRINT the line
