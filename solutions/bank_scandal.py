x = raw_input()
array = raw_input().split()
array = map(int, array)

best=0
s=0

for i in range(len(array)):
    x=array[i]
    if array[i]<0:
        array[i]=array[i]*1.5
    elif array[i]%2!=0:
        array[i]=array[i]*2
    else:
        continue

for i in array:
    s = max(i, s+i)
    best = max(best,s)
print "%.1f" % (best)