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

# This is a great script. It is SOOOOO close to being totally right. The only
# issue that tripped you up was the indexing to get the last "n_lines" lines
# from your list. [-n] will give you the n'th from the end line. So [-1] is the 
# last line of the list. To get the last "n_lines" lines, you would use the
# index [-n_lines:]. Otherwise, the script looks great! I really appreciate that
# your comments are your pseudo-code. Keep it up! - Mike