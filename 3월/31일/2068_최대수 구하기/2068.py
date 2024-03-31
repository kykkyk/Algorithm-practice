t = int(input())

for _ in range(1,t+1):
    data = list(map(int,input().split()))
    print("#" + str(_),max(data))