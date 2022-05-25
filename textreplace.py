import re
text="today's date is 24/05/2022 and yesterdays date is 25/05/2022"
m=re.sub(r'(\d+)/(\d+)/(\d+)',r'\1-\3-\2',text)
print(m)