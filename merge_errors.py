#!/usr/bin/env python3
import sys
import argparse
import statistics


def parseArgs():
	parser=argparse.ArgumentParser(description="Merge error absolute frequencies")
	parser.add_argument('-i','--infile',dest='infile',help='Path to input file',nargs='+',required=True)
	parser.add_argument('-o','--outfile',dest='outfile',help='Name of the output files',required=True)
	args=parser.parse_args(sys.argv[1:])
	return(args)	
	
def merge_errors_abs_freq(infile,outfile):
	lines=newlines=name=value=[]
	n,m,fn,sample_name=[-1,1,1,""]	
	outfilename=str(outfile)+".xls"
	file=infile[0]
	
	with open(file) as f:
		line1=f.readline()
		parts=line1.split('\t')
		name1=file.split("-")[0]
		with open(outfilename, 'w') as g:
			g.write(parts[2]+'\t'+parts[3]+'\t'+parts[4]+'\n')
		for line in f:	
			parts=line.split('\t')			
			with open(outfilename, 'a') as g:	
				g.write(parts[2]+'\t'+parts[3]+'\t'+parts[4]+'\n')	
					
	for filename in infile:	
		with open(filename) as f:
			name2=filename.split("-")[0]
			for line in f:
				if n<0:
					n+=1
					if name1==name2:
						sample_name= str(name2+"_"+str(m))
						m+=1
					else:
						m=1
						sample_name= str(name2+"_"+str(m))
						name1=name2	
						m+=1
				else:
					n+=1
					parts=line.split('\t')
					ref=parts[4]
					
					if ref == "A":
						value.append(float(parts[6])+float(parts[7])+float(parts[8])+float(parts[9])+float(parts[10])+float(parts[11]))
						
					elif ref == "C":					
						value.append(float(parts[5])+float(parts[7])+float(parts[8])+float(parts[9])+float(parts[10])+float(parts[11]))
						
					elif ref == "G":					
						value.append(float(parts[5])+float(parts[6])+float(parts[8])+float(parts[9])+float(parts[10])+float(parts[11]))	
						
					elif ref == "T":					
						value.append(float(parts[5])+float(parts[6])+float(parts[7])+float(parts[9])+float(parts[10])+float(parts[11]))	
						
			newlines=[str(sample_name)+'\n']
		
			for i in range(n):
				newlines.append(str(value[i])+'\n')
			
			with open(outfilename) as f:
				lines=f.readlines()
	
			with open(outfilename, 'w') as g:
				for i in range (n+1):
					g.write(lines[i].rstrip()+'\t'+newlines[i])
		n=-1
		value=[]				
if __name__=='__main__':
	args=parseArgs()
	merge_errors_abs_freq(args.infile,args.outfile)
