t = int(input())

for _ in range(1,t+1):
    li = map(int,input().split())
    sum = 0
    for i in li:
        if i%2!=0:
            sum+=i
    print("#" + str(_),sum)