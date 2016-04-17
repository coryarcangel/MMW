import csv

def get_sec(s):
    l = s.split(':')
    return int(l[0]) * 60 + int(l[1])

def write(a,b,c):
	f.write('{}\t{}\tTony_Conrad_matmotw_{}\n'.format(a,b,c))
	
GB_FILE_NAME_OLD = "null"
COUNTER = 0;

with open('MMW-Master.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:

		MATMOTW = row['MATMOTW'] 
		GB_FILE_NAME = row['GB_FILE_NAME'] 
		START_TIME = row['START_TIME']
		
		if COUNTER == 0:
			f = open(GB_FILE_NAME,"w")
		
		if GB_FILE_NAME != GB_FILE_NAME_OLD:
			f.close()
			filename = "%s.txt" % GB_FILE_NAME
			f = open(filename,"w")
			write(get_sec(START_TIME.split("-")[0]),get_sec(START_TIME.split("-")[1]),MATMOTW)
			print GB_FILE_NAME
			print MATMOTW, get_sec(START_TIME.split("-")[0]),"\t",get_sec(START_TIME.split("-")[1])		
		else:
			write(get_sec(START_TIME.split("-")[0]),get_sec(START_TIME.split("-")[1]),MATMOTW)
			print MATMOTW, get_sec(START_TIME.split("-")[0]),"\t",get_sec(START_TIME.split("-")[1])
		
		GB_FILE_NAME_OLD = GB_FILE_NAME
		COUNTER = COUNTER + 1;
	
	f.close()
