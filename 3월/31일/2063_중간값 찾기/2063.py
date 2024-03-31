n = int(input())
data =list(map(int,input().split()))
answer = sorted(data)
print(answer)
print(answer[n//2]) # 중간값은 총길이/2 + 1 이지만 배열은 0부터 시작