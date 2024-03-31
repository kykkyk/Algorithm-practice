# 약수 구하기!
x = 30
result = []
for i in range(1,x+1):
    if x%i==0:
        result.append(i)
print(result)