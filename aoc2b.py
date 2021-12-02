f=open("aoc2.txt","r")
data=[]
for line in f:
    temp=line.split(" ")

    data.append([temp[0],int(temp[1])])
f.close()
h=0
d=0
aim=0
print(data)
p=0
for x in range(len(data)):
    p+=1
    if data[x][0]=="forward":
        h=h+data[x][1]
        d=d+(aim*data[x][1])
    elif data[x][0]=="up":
        #d=d-data[x][1]
        aim=aim-data[x][1]
    elif data[x][0]=="down":
        #d=d+data[x][1]
        aim=aim+data[x][1]
print(h*d,p)
