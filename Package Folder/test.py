
with open("sorted_read_lentgh_new.fastq") as file:
    for i, line in enumerate(file):
        if i%4==1:
            print(len(line.strip()))