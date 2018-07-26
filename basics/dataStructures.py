from collections import deque

list = ['one', 'two', 'three']

print list.pop()

queue = deque(['one','two','three'])
print queue.popleft()


dic1 = {'bleh':'yo', 'stuff': {'yeh':'yeh'}}
dic2 = dic1['stuff'].copy()

print(dic2)





