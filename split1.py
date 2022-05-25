import re
line='nobody:2,-2*Unprivileged User:/var/empty:/usr/bin/false'
a=re.split(r'[:,\s*]\s*',line)
print(a)
#print(b)

