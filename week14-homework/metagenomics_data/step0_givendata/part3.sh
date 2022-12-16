for bin in 1 2 3 4 5 6
do
	for names in $(grep ">" bins_dir/bin.${bin}.fa | cut -d '>' -f 2)
	do
		grep $names KRAKEN/assembly.kraken
	done | cut -d '	' -f 2 > tax.txt
	for column in 5 6 7 8 9 10 11 12
	do
		cut -d ';' -f$column tax.txt| sort | uniq -c
	done
done