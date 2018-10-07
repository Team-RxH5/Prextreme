n=int(raw_input())

for i in range(n):
    x=int(raw_input())
    t=0
    ex=0

    while x>1:
        if x%2!=0:
            ex+=1
        t=t+x
        x=x/2

    print t+ex+1