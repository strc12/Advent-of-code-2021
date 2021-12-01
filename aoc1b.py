f=open("aoc1.txt","r")
data=[]
for line in f:
    data.append(int(line))
f.close()
inc=0
print(data)
summy=[]
for k in range(1,len(data)-2):
    tot=data[k]+data[k+1]+data[k+2]
    summy.append(tot)
print(summy)   
for k in range(1,len(summy)):
    if summy[k]>summy[k-1]:
        inc+=1
print(inc)
