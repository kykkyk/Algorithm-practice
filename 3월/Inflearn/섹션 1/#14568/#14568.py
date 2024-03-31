import sys
sys.stdin = open("3월\Inflearn\섹션 1\#14568\input.txt")
n = int(input())
result = 0
for i in range(n):
    a=i
    if a < 1:
        continue
    for j in range(2,n):
        b = a+j
        if a + b > n:
            continue
        c = n-a-b
    # a = 1 , 3    
        if c <= 0 :
            continue
        elif c %2 !=0:
            continue
        result +=1
        print(a,b,c)
print(result)

# a b c
# 1 3 2
# 1 4 1
# 1 5 0
# 2 4 0

