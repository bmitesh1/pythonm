records=[('bar',4,5),('foo',8),('tiger',6,7,8)]
def do_bar(*args):
    print(*args)

for tag,*args in records:
    if tag=='tiger':
      do_bar(tag,*args)    
