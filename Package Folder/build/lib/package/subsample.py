#!/mnt/c/Users/wahid/OneDrive/Documents/DecodeAge/Downsizing tool/Subsampling Package/subsample-env/bin/python
#to check location of python you can type which python and copy the directory from there
import argparse
class SubSamplingProcess:
    def __init__(self):
        pass
    def sorted_read_length(self,file):
        reads=[]
        
        with open(file) as input_file:
            for i,line in enumerate(input_file):
                if i%4==0:
                    header=line.strip()
                    #print(header)
                elif i%4==1:
                    sequence=line.strip()
                    #print(sequence)
                elif i%4==2:
                    adder=line.strip()
                    #print(adder)
                elif i%4==3:
                    qc=line.strip()
                    #print(qc)
                    reads.append((header, sequence,adder, qc))
                
                #sorting based on read length
                reads.sort(key=lambda x: len(x[1]), reverse=True)
                #writing an output file after sorting according to the read length
                with open("sorted_read_lentgh_%s"%(file), 'w') as output:
                    for i in range(len(reads)):
                        output.write(f"@{reads[i][0]}\n{reads[i][1]}\n+\n{reads[i][3]}\n")
                    
    #to check the length of the sorted file
    def read_length(self,file):
        with open(file) as infile:
            for i,line in enumerate(infile):
                if i%4==1:
                    print(len(line.strip()))
    def subsampling_read_length(self,file,percentage):
        with open(file) as input_file:
            for i,line in enumerate(input_file):
                pass
            total_reads = int((i+1)/4)
            
            #percentage = 0.1  # 10% of total reads

            # Calculate the number of reads to be taken (10% of total reads)
            num_reads = int(total_reads * percentage)

            # Read the Fastq file and write the first num_reads reads to a new Fastq file
            with open(file) as input_file, open('subset%s.fastq'%(percentage), 'w') as output_file:
                for i, line in enumerate(input_file):
                    output_file.write(line)
                    if i % 4 == 3:  # Check if the current line is the quality scores line
                        if i // 4 + 1 == num_reads:  # Check if the desired number of reads is reached
                            print("done")
                            break


def main():
    parser=argparse.ArgumentParser(prog='subsample',description="Subsampling with read length and start time")
    parser.add_argument("-f","--file",help="input filename",type=str)
    parser.add_argument("-p","--percentage",help="Subsampling percentage",type=float)
    args=parser.parse_args()
    process=SubSamplingProcess()
    if args.file:
        process.sorted_read_length(args.file)
    if args.percentage:
        process.subsampling_read_length(args.file,args.percentage)
    process.read_length(args.file)
    

if __name__=="__main__":
    main()