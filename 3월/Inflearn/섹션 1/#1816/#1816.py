import sys
sys.stdin = open("3월\Inflearn\섹션 1\#1816\input.txt")
n = int(input())

for _ in range(n): 
    x = int(input())
    flag = False
    for i in range(2,1000001):
        if x%i==0:
            flag = True
            break
    if flag == True :
        print("NO")
    else:
        print("Yes")

    