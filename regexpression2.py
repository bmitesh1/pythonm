import re
s='the quick brown fox jumped quickly over lazy dog'
match=re.search(r'\bbrown\s',s)
print(match)