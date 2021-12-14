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

for x in data:
    for k in range(len(data[0])):
        if x[k]=="1":
            ans[k][1]+=1
        else:
            ans[k][0]+=1
print(ans)
e=""
g=""
for k in ans:
    if k[0]>k[1]:
        e=e+"1"
        g=g+"0"
    else:
        g=g+"1"
        e=e+"0"
print (int(g,2)*int(e,2))
