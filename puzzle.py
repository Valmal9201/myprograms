# puzzle a < b < c
a = int(input())
b = int(input())
c = int(input())
tmp = max(a, b)
a = min(a, b) # a = 1st or 2nd smallest
b = tmp # b = 2nd or 3rd largest
tmp = max(b, c)
b = min(b, c) # b = 2nd or 1st smallest
c = tmp # c = largest
tmp = max(a, b)
b = tmp # b = 2nd smallest
a = min(a, b) # a = smallest
print(a, b, c)