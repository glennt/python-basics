
values = range(0,22,1)
print values

def f(x):
    if(x % 2 == 0):
        return True
    else:
        return False


print filter(f,values)

seq = range(4)
seq2 = range(4,8,1)
def add(a,b):
    return a + b

# Pass args in sequences to add
print (seq)
print (seq2)
mapList = map(add, seq, seq2)
print mapList