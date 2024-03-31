t = int(input())

for _ in range(1,t+1):
    data = list(map(int,input().split()))
    a = " "
    for i in data:
        if (data[0] > data[1]):
            a = ">"
        elif (data[0] < data[1]):
            a = "<"
        else:
            a = "="
    print("#" + str(_) , a)