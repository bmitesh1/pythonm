import collections
from typing import DefaultDict
a=[1,2,3,5,4]
b='harry'
d=DefaultDict(str)
for i in range(len(a)):
    d[i]=b[i]
print(d)    