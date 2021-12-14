def mostfreq(list,place): 
    g=0
    for d in list:
        if d[place]=="1":
            g+=1
        else:
            g-=1
        #print(g)
    if g>=0:
        return 1
    else:
        return 0
def leastfreq(list,place): 
    g=0
    for d in list:
        if d[place]=="1":
            g+=1
        else:
            g-=1
    if g>=0:
        return 0
    else:
        return 1
f=open("aoc3.txt","r")
data=[]
for line in f:
    data.append(line.strip("\n"))
f.close()
print(data)
ans=[]
for k in range(len(data[0])):
    ans.append([0,0])
print(ans)
g=0
e=0
rem=[]
temp=[]
for k in range(len(data[0])):
    if len (data)>1:
        rem=mostfreq(data,k)
        #print("remving",rem,k)
        for d in data:
            #print(d,d[k],str(rem))
            if d[k]==str(rem):
                #print("keep",d)
                temp.append(d)
    data=[]
    for k in temp:
        data.append(k)
    temp=[]
o2=int(data[0],2)
f=open("aoc3.txt","r")
data=[]
for line in f:
    data.append(line.strip("\n"))
f.close()
temp=[]
for k in range(len(data[0])):
    if len (data)>1:
        rem=mostfreq(data,k)
        #print("remving",rem,k)
        for d in data:
            #print(d,d[k],str(rem))
            if d[k]!=str(rem):
                #print("keep",d)
                temp.append(d)
    
    data=[]
    for k in temp:
        data.append(k)
    if len(temp)==1:
        break
    temp=[]
co2=int(data[0],2)
print(co2*o2)