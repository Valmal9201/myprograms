a_list = []
for i in range(1,101):
    a_list.append(i)

#Linear Search
def linear_search(a_list, target):
    i = 0
    for i in range(len(a_list)):
        if a_list[i] == target:
            return i
        else:
            i += 1

def binary_search(a_list,target):
    sorted(a_list)
    left = 0
    right = len(a_list) - 1
    while left <= right:
        middle = (left + right) // 2
        if left == right and a_list[middle] != target:
            return -1
        elif a_list[middle] == target:
            return middle
        elif a_list[middle] > target:
            right = middle - 1
        else:
            left = middle + 1

from random import randrange
test = []
for i in range(10):
    test.append(randrange(1,20))

print(f"Random: List {test}")
answer1 = linear_search(test, 6)
answer2 = binary_search(sorted(test), 6)
print(f"Linear: {answer1} & Binary: {answer2}")

num = int(input())
answer1 = linear_search(a_list, num)
answer2 = binary_search(sorted(a_list), num)
print(f"Linear: {answer1} & Binary: {answer2}")

#In Class Example
def linear_search(a_list, target):
    i = 0
    for i, value in enumerate(a_list):
        if a_list[i] == target:
            return i
    return -1

def binary_search(a_list,target):
    sorted(a_list)
    left = 0
    right = len(a_list) - 1
    while left <= right:
        middle = (left + right) // 2
        if a_list[middle] == target:
            return middle
        elif a_list[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return -1

from random import randrange
test = []
for i in range(10):
    test.append(randrange(1,20))

print(f"Random: List {test}")
answer1 = linear_search(test, 6)
answer2 = binary_search(sorted(test), 6)
print(f"Linear: {answer1} & Binary: {answer2}")