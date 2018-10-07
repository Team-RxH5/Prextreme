q=int(input())
if(1>q or q>10):
    exit

def isAnagram(par1,par2):
    par1.sort()
    par2.sort()

   # print(len(par1))

    for i in range(len(par1)):
        if(par1[i]!=par2[i]):
            return False

    return True

def init():
    strings=[]
    count=0
    q=int(globals()['q'])
    while(q!=0):
        strings.append(input())
        q-=1

    for string in strings:
        s=list(string)
        for n in range(len(s)-1): #max length-1 of a pair
            for p in range(int(len(s)-n+1)):
                k=p+1
                par1=s[p:(p+n + 1)]
                
                while(k<len(s)-n):
                    
                    par2=s[k:(k+n + 1)]
                    if(isAnagram(par1,par2)):
                        count+=1
                    k+=1

        print(count)
        count=0

init()