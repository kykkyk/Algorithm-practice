# number = int(input())
# print(number)

# string = input()
# print(string)

# first, second, third = map(int, input().split())
# print(first,second,third)

# first, second, third = map(str, input().split())
# print(first,second,third)

list1 = list(map(int,input().split()))
print(*list1)

list2 = list(map(str, input().split()))
print(*list2)