#from collections import Counter
import sys
import re

#Insert the outputs from question ii
if len(sys.argv )> 1:
    file = sys.argv[1]
else:
    file = 'q3-ii-result.txt'

#Open the file to read
if file:
    try:
        result = open(file, 'r').read()
        result = result.strip()
        # new line
    except Exception as e:
        print(e)

# these code are based on re module and the findall function which work to match the similar values
print('The zero-runs of length ten =',len(re.findall(r'(?=(%s))' % re.escape('0000000000'), result)))
print('The one-runs of length ten =',len(re.findall(r'(?=(%s))' % re.escape('1111111111'), result)))
print('The zero-runs of length nine =',len(re.findall(r'(?=(%s))' % re.escape('10000000001'), result)))
print('The one-runs of length nine =',len(re.findall(r'(?=(%s))' % re.escape('01111111110'), result)))
print('The zero-runs of length eight =',len(re.findall(r'(?=(%s))' % re.escape('1000000001'), result)))
print('The one-runs of length eight =',len(re.findall(r'(?=(%s))' % re.escape('0111111110'), result)))
print('The zero-runs of length seven =',len(re.findall(r'(?=(%s))' % re.escape('100000001'), result)))
print('The one-runs of length seven =',len(re.findall(r'(?=(%s))' % re.escape('011111110'), result)))
print('The zero-runs of length six =',len(re.findall(r'(?=(%s))' % re.escape('10000001'), result)))
print('The one-runs of length six =',len(re.findall(r'(?=(%s))' % re.escape('01111110'), result)))
print('The zero-runs of length five =',len(re.findall(r'(?=(%s))' % re.escape('1000001'), result)))
print('The one-runs of length five =',len(re.findall(r'(?=(%s))' % re.escape('0111110'), result)))
print('The zero-runs of length four =',len(re.findall(r'(?=(%s))' % re.escape('100001'), result)))
print('The one-runs of length four =',len(re.findall(r'(?=(%s))' % re.escape('011110'), result)))
print('The zero-runs of length three =',len(re.findall(r'(?=(%s))' % re.escape('10001'), result)))
print('The one-runs of length three =',len(re.findall(r'(?=(%s))' % re.escape('01110'), result)))
print('The zero-runs of length two =',len(re.findall(r'(?=(%s))' % re.escape('1001'), result)))
print('The one-runs of length two =',len(re.findall(r'(?=(%s))' % re.escape('0110'), result)))
print('The zero-runs of length one =',len(re.findall(r'(?=(%s))' % re.escape('101'), result)))
print('The one-runs of length one =',len(re.findall(r'(?=(%s))' % re.escape('010'), result)))
