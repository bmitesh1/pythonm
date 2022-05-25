import heapq

a = [1,2,3,4,54,34,32]
b = [6,59,3,4]
print(heapq.nlargest(4,a))
print(heapq.heapify(a))
print(a)
c=list(heapq.merge(a,b))
print(c)