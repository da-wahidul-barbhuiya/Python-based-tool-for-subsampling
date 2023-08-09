from datetime import datetime,timedelta
import argparse
class StartTime:
    def __init__(self) -> None:
        pass
    def start_time(self,file):
        global reads
        reads=[]
        with open(file) as infile:
            for i,line in enumerate(infile):
                if i%4==0:

                    header=line.strip()
                    strtsrch='start_time'
                    endsrch=' flow_cell_id'
                    idx1=header.find(strtsrch)
                    idx2=header.find(endsrch)
                    res=header[idx1+len(strtsrch)+1:idx2]
                                    
                elif i%4==1:
                    sequence=line.strip()
                    #print(sequence)
                elif i%4==2:
                    adder=line.strip()
                    #print(adder)
                elif i%4==3:
                    qc=line.strip()
                    #print(qc)
                    reads.append((res,header, sequence,adder, qc))
                reads.sort(key=lambda x:datetime.strptime(x[0], '%Y-%m-%dT%H:%M:%S.%f%z'))

                with open('timestamp_sorted_%s'%(file), 'w') as output:
                        for i  in range(len(reads)):
                            output.write(f"@{reads[i][1]}\n{reads[i][2]}\n+\n{reads[i][4]}\n")

    
    def reads_in_hour(self,file,num):
        time_reads=reads[0][0]
        dt = datetime.strptime(time_reads, '%Y-%m-%dT%H:%M:%S.%f%z')
        dt += timedelta(hours=num)
        updated_timestamp = dt.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        # Insert the colon ':' in the offset part
        updated_timestamp = updated_timestamp[:-2] + ':' + updated_timestamp[-2:]
        with open(file) as input_file, open('subset_test_hrs.fastq', 'w') as output_file:
            for i, line in enumerate(input_file):
                if i%4==0:
                    name=line.strip()
                    strtsrch='start_time'
                    endsrch=' flow_cell_id'
                    idx1=name.find(strtsrch)
                    idx2=name.find(endsrch)
                    global res
                    res=name[idx1+len(strtsrch)+1:idx2]
                    if res<=updated_timestamp:
                        #print(res)
                        output_file.write(line)
                        
                
                elif i%4==1: #sequence line
                    #print(line.strip())
                    if res>updated_timestamp:
                        break
                    output_file.write(line)
                    
                elif i%4==2:
                    #print(line.strip())
                    if res>updated_timestamp:
                        break
                    output_file.write(line)
                    
                elif i%4==3:
                    #print(line.strip())
                    if res>updated_timestamp:
                        break
                    output_file.write(line)
def main():
    parser=argparse.ArgumentParser(prog='subsample',description="Subsampling with read length and start time")
    parser.add_argument("-f","--file",help="input filename",type=str)
    parser.add_argument("-hr","--hours",help="Subsampling hour",type=int)
    #parser.add_argument("-l","--length",help="read length",type=int)
    args=parser.parse_args()
    process=StartTime()
    if args.file:
        process.start_time(args.file)
        #process.read_length(args.file)  # Call read_length only if args.file is not None
    if args.hours:
        process.reads_in_hour(args.file,args.hours)
        
    #process.read_length(args.file)
    

if __name__=="__main__":
    main()