f=open("aoc4.txt","r")
numbers=f.readline().split(",")

for k in range (len(numbers)):
    numbers[k]=int(numbers[k])
#print(numbers)
f.readline()
boards=[]

    
temparr=[]
count=0
for line in f:
    temp=[]
    if line!="" and count!=5:
        for k in range (0,len(line)-1,3):
            #print(k)
            y=(line[(0+(k)):(2+(k))].strip())
            temp.append(y)
        #print(temp)
        for t in range(len(temp)):
            temp[t]=int(temp[t])

        temparr.append(temp)
        count+=1
        #print (temparr)
        
    else:
        boards.append(temparr)
        temparr=[]
        count=0
        #print(boards)
win=False
#print(boards)    
#def checknums(num)
while win==False: 
    for num in numbers:
        #print(num)
        for board in boards:
            #print(board)
            for line in board:
                #print(line)
                #input()
                if num in line:
                    for n in range(len(line)):
                        if line[n]==num:
                            line[n]="x"
                            for t in range(5):
                                #print(board)
                                #input()
                                #horiz check
                                for y in range(5):
                                    #print(t,y)
                                    lined=board[t][y]
                                    if lined==["x","x","x","x","x"]:
                                        #print("win")
                                        #print(board)
                                        winboard=board
                                        boards.remove(winboard)
                                        #print(boards)
                                        total=0
                                        print(len(boards))
                                        if len(boards)==1:
                                            print(boards)
                                            for row in boards[0]:
                                                print(row)
                                                for digit in row:
                                                    if digit!="x":
                                                        total=total+int(digit)
                                            k=numbers.index(num)
                                            #print(boards[t],numbers[k+1],(total-num), numbers[k+1]*(total-num-numbers[k+1]))
                                            print(numbers[k+1],(total-num), numbers[k+1]*(total-num-numbers[k+1]))
                                            quit()
                                #vert check
                                for k in range(5):
                                    row=[]
                                    for j in range(5):
                                        row.append(board[j][k])
                                    if row ==["x","x","x","x","x"]:
                                        winboard=board[t]
                                        board.remove(board[t])
                                        total=0
                                        print(len(boards))
                                        if len(boards)==1:
                                            print(boards)
                                            for row in boards[0]:
                                                for digit in row:
                                                    if digit!="x":
                                                        total=total+int(digit)
                                            k=numbers.index(num)
                                            #print(boards[t],numbers[k+1],(total-num), numbers[k+1]*(total-num-numbers[k+1]))
                                            print(numbers[k+1],(total-num), numbers[k+1]*(total-num-numbers[k+1]))

                                            quit()

