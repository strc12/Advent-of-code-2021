f=open("aoc1.txt","r")
data=[]
for line in f:
    data.append(int(line))
f.close()
inc=0
print(data)
for k in range(1,len(data)):
    if data[k]>data[k-1]:
        inc+=1
print(inc)       
