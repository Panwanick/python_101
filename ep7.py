# While Loop

# A = []
# x = 0
# while x < 5:
#     a = input()
#     A.append(a)
#     x += 1
# print(A)

# lst = []
# mystr = str(input())
# print(len(mystr))
# while len(mystr) > 0:
#     lst.append(mystr)
#     mystr = input()
# print(lst)

# n = 1
# count = 0
# while n <= 30:
#     if n%3 == 0:
#         print(n)
#     n += 1
# print('Count = ', count)

# n = 1
# count = 0
# while n <= 20:
#     if n%2 == 1:
#         print(n)
#     n += 1

# rows = 5
# for i in range (1 , rows+1):
#     for j in range(-1 , i-1):
#         print('*' , end = '')
#     print()

A = [int(e) for e in input().split()]
x = int(input('x = '))

found = -1
index = 0
while index < len(A):
    a = A[index]
    if a == x:
        print(x, "was found at ", index)
        found = index
    index += 1
if found == -1:
    print(x, 'was not found')