def countdown(n):
    print('starting from ',n)
    while n>0:
        yield n
        n-=1
    print('done') 
a=countdown(3) 
# for i in a:
#     print(i)    
next(a)
next(a)
# next(a)

