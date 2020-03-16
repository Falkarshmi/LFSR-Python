from collections import Counter
ExamNumericID = 11111111
print("\nThe exam ID is:", ExamNumericID)
     
output = []
# defined an array called output which will print the 1000 bits of the sequence

def xor():
    
    start = "{0:b}".format(ExamNumericID)
    start = start[-15:]
    start = list(map(int, list(start)))
    print(start)
    # define the seed function
    for i in range(0,1000):
        
        # using loops for restrict the outputs to the first 1000 bits
        Xored = (start[0] + start[-1]) % 2
        # define the function of xoring the first bit which hold the position 0 and the last bit by using the logic of xor ( b+b) %2, b = binary
       
        output.append(start[-1])
        # ADD the value that computed from xoring the tap 1 and 15 to the outputs " the generated sequences"
        start.pop()
        # delete the last value of computed sequence after shifting
        start.insert(0,Xored)
       
    return output
def savetoFile(s):
    with open('result.txt', 'w') as f:
        f.write(s)
        f.close()
        # save files function, which save the comupted outputs to the file q3-result.txt
        
def convertString(list):
    return ''.join(str(c) for c in list)
    # convernting the array [1,1,1] to string list which print 111
    
lsf = xor()
   
string = convertString(lsf)
savetoFile(string.strip())
print('The bit sequences:\n',string)
print('\nThe lenght of the bits is: ',len(output))

