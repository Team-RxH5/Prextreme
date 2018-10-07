import sys

pattern=[[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."]]

def change(j,i):
    if pattern[i][j]==".":
        pattern[i][j]="X"
    elif pattern[i][j]=="X":
        pattern[i][j]="."

def press(x,y):
    if (y-1>=0 and y-1<=9) and (x-1>=0 and x-1<=9):
        change(y-1,x-1)
    # else:
        # print "Out of grid",y-1,x-1
    
    if (y>=0 and y<=9) and (x-1>=0 and x-1<=9):
        change(y,x-1)
    # else:
        # print "Out of grid",y,x-1
    
    if (y+1>=0 and y+1<=9) and (x-1>=0 and x-1<=9):
        change(y+1,x-1)
    # else:
        # print "Out of grid",y+1,x-1
    
    if (y>=0 and y<=9) and (x>=0 and x<=9):
        change(y,x)
    # else:
        # print "Out of grid",y-1,x-1
    
    if (y-1>=0 and y-1<=9) and (x+1>=0 and x+1<=9):
        change(y-1,x+1)
    # else:
        # print "Out of grid",y-1,x+1
    
    if (y>=0 and y<=9) and (x+1>=0 and x+1<=9):
        change(y,x+1)
    # else:
        # print "Out of grid",y,x+1
    
    if (y+1>=0 and y+1<=9) and (x+1>=0 and x+1<=9):
        change(y+1,x+1)
    # else:
        # print "Out of grid",y+1,x+1

f = sys.stdin.read()
inputs=f.split()
inputs=map(int, inputs)

i=0
while i<len(inputs):
    press(inputs[i+1],inputs[i])
    i=i+2
    

# output
# print "\nprinting pattern"
for i in range(10):
    for j in range(10):
        print pattern[i][j],
    print ""
