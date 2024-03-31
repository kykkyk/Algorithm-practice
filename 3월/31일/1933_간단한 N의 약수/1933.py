t = int(input())
list =[]
for i in range(1,t+1):
    if t%i==0:
        list.append(i)
print(*list)