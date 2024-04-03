import sys

sys.stdin = open("3월\Inflearn\섹션 1\#1816\input.txt")

a = int(input())

for _ in range(a):
    b = int(input())
    for i in range(2,100001):
        if b%i==0:
            print("No")
            break
        if i==100000:
            print("Yes")