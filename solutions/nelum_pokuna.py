cases=int(raw_input())

for case in range(cases):
    answers=[0,0]
    grid=[[0 for x in range(4)] for y in range(2)]
    common=[]

    for i in range(2):
        answers[i]=int(raw_input())
        for j in range(4):
            grid[i][j]=raw_input().split()
            grid[i][j] = map(int, grid[i][j])

    # Code begins
    for i in grid[0][answers[0]-1]:
        if i in grid[1][answers[1]-1]:
            common.append(i)

    if len(common)>1:
        print "Bad magician!"
    elif len(common)==1:
        for i in common:
            print i
    elif len(common)==0:
        print "Volunteer cheated!"
