n=raw_input().split()
n = map(int, n)

for number in n:
    x=number
    name=""
    while number>0:
        if number>=1000:
            name=name+"Z"
            number-=1000
        elif number>=100:
            name=name+"Y"
            number-=100
        elif number>=10:
            name=name+"X"
            number-=10
        elif number>=5:
            name=name+"V"
            number-=5
        elif number==4:
            name=name+"IIII"
            break
        elif number==3:
            name=name+"III"
            break
        elif number==2:
            name=name+"II"
            break
        elif number==1:
            name=name+"I"
            break
    
    print str(x)+": "+name
