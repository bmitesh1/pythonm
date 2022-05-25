import os
import re
#filename=os.listdir('.')
filename='i kept that card in somefile'
# #print(filename)
# a=any(name.startswith('g') for name in filename)
# print(a)
datematch=re.compile(r'\d+/\w+/\d+')
text='todays date is 11213/qw/2017'
# m=datematch.match(text)
# a=re.search('kept',filename)
# print(m)
m=datematch.findall(text)
print(m)