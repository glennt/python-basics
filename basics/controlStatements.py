
x = 10

#if
if (x < 12):
    print "Less than 12!"

if (x > 12):
    print "Greater than 12!"
elif (x < 12):
    print "Else less than 12!"


#loop
list = ['one','two','three']

for v in list:
    print v



print range(2,20,2)


headers = {
    'Content-Type': 'applications/json',
    'Other': 'other'
}

for key, value in headers.iteritems():
    print key.lower() + ' ' + value.lower()