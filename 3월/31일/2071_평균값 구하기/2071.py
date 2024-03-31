t = int(input())

for _ in range(1,t+1):
    data = map(int,input().split())
    sum = 0
    for i in data:
        sum+=i
    print("#" + str(_), round(sum/10))