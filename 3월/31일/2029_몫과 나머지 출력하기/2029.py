t = int(input())
for _ in range(1, t+1):
    a,b = map(int,input().split())
    print("#" + str(_), (a//b),(a%b))