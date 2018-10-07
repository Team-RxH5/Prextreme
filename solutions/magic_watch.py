h = int(input())
if(1>h or 12<h):
    exit
m = int(input())
if(0>m or 59<m):
    exit

hours = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]
mins = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","twenty one","twenty two","twenty three","twenty four","twenty five","twenty six","twenty seven","twenty eight","twenty nine","thirty"]

def init(h,m):
    if(m==0):
        print(hours[h-1],"o' clock")
    elif(m<30):
        if(m==1):
            print("one minute past",hours[h-1])
        else:
            if(m==15):
                print("quarter past",hours[h-1])
            else:
                print(mins[m-1],"minutes past",hours[h-1])
    elif(m==30):
        print("half past",hours[h-1])
    elif(m==45):
        if(h==12):
            print("quarter to 1")
        else:
            print("quarter to",hours[h])
    else:
        if(h==12):
            if(60-m==1):
                print("one minute to one")
            else:
                print(mins[59-m],"minutes to one")
        else:
            if(60-m==1):
                print("one minute to",hours[h])
            else:
                print(mins[59-m],"minutes to",hours[h])

init(h,m)