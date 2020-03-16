import sys

def readFile():
	"""read the output file
	in question II and and insert the outputs here.
	"""
	with open('q3-ii-result.txt', 'r') as f:
		data = f.read()
		data = data.strip()
	if data:
		return data
	else:
		print('check the file name, this filename is not existed!!')
		sys.exit()
		
def converBin(val):
	"""This  functions takes a decimal and converts it to binary
	checks if length is less than zero, if that is the case adds
	zeros infront to it and finally convert the result to list
	and returns the list.
	"""
	val = "{0:b}".format(val)	
	lenthval = len(val)
	newval = '0' *(15 - lenthval) + val	
	lnewval = list(newval)
	lnfinal = list(map(int, lnewval))
	return lnfinal
  
def xor(arg1):
	"""
	This functions gets a 15 bit LFSR and returns a 1000 bit
	output 
	"""
	output = []
	for i in range(0,1000):
				
		Xored = (arg1[0] + arg1[-1]) % 2     
		output.append(arg1[-1])        
		arg1.pop()        
		arg1.insert(0,Xored)
		
	return output
           
       
#REad the file      
data = readFile()

#Check for all the possible combinations
for i in range(0, 32767):
	convertI = converBin(i)
	lsf = xor(convertI)   
	strlsf = ''.join(str(k) for k in lsf)

	if strlsf[500:] == data[500:]:
		#Match found 
		#Print Match and break
		print('the lfsr seed is:',''.join(str(k) for k in converBin(i)))
		#print(strlsf)
		break
        
       



