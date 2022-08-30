
import sys

def bed_parser(fname):
	# open up file and put filestream in fs
	fs = open(fname, mode='r')
	# create empty list to hold entries
	bed = []
	data_types = [str, int, int, str, float, str, int, int, str, str, str, str]
	for h, line in enumerate(fs):
		fields = line.rstrip().split("\t")
		assert len(fields) != 10 and len(fields)!= 11, "Error the file has 10 or 11 fields"
		
		
		#try:
		for i in range(min(len(data_types), len(fields))):
			if fields[i] != ".":
				converter = data_types[i]
				fields[i] = converter(fields[i])
		bed.append(fields[:min(len(data_types), len(fields))])
		#except:
			#print(f"line {h} is malformed", file=sys.stderr)
	fs.close()
	return bed

if __name__ == "__main__":
	bed = bed_parser(sys.argv[1])
	# pull out first 2 entries as list and look
	# at each entry in variable i
	for i in bed[0:2]:
		#print entry i
		print(i)
