import re
s = "winter is coming.season1. there are lot of episodes accummulated to watch."
#match=re.search(r'\.',s)
# match=re.search(r'^winter',s)
# match=re.search('c.m',s)
# match=re.search(r'[cm]',s)
# match=re.findall('c*m',s)
# p=re.compile('c*m')
# match=p.findall(s)
regex='\bwin'
match=re.findall(regex,s)
print(match)