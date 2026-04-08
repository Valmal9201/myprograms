# 3. a) Construct an algorithm in code to calculate and output the mean of the data values stored in the one-dimensional array DATA that contains N elements. You 
# may assume that the DATA array containing N elements has been inputted.

def mean(array):
    total = 0
    for i in range(0, len(array)):
        total += array[i]
    meanf = total/len(array)
    return meanf

array = [2, 3, 3, 6, 5, 9, 10, 100, 14, 17]
print(mean(array))

# The median of the data values stored in a one-dimensional array can be determined as follows: 1. Arrange the data values from the lowest to highest value. 2. The 
# median is the data value in the middle of the array. 3. If there are two data values in the middle, then the median is the mean of those two values.

array = [2, 3, 3, 6, 5, 9, 10, 100, 14, 17]
def median(array):
    array.sort()
    if len(array) % 2 != 0:
        med = array[len(array) // 2]
    else:
        med = (array[len(array) // 2 - 1] + array[len(array) // 2]) / 2 
    return med
print(median(array))

# 4 b) Construct a searching algorithm that out-performs linear search when finding a target value knowing that the given collection is sorted from
# least to greatest.

# 5. 
array = [2, 3, 3, 6, 5, 9, 10, 100, 14, 17]
target = [14]
def binary_search(a_list, target):
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

test = ["CAT", "DOG", "SUN", "BED", "QUIZ"]

def scrabble(word):
    table = {
        "AEIOULNSTR" : 1,
        "DG" : 2,
        "BCMP" : 3,
        "FHVWY" : 4,
        "K" : 5,
        "JX" : 8,
        "QZ": 10
    }
    score = 0
    scores = []
    for c in word:
        for key in table.keys():
            if c in key:
                score += table[key]
    return scores
print(scrabble(test))

# In Class Example
# 5. Scrabble
def scrabble(word):
    score = 0
    for c in word:
        if c in "AEIOULNSTR":
            score += 1
        elif c in "DG":
            score += 2
        elif c in "BCMP":
            score += 3
        elif c in "FHVWY":
            score += 4
        elif c in "K":
            score += 5
        elif c in "JX":
            score += 8
        elif c in "QZ":
            score += 10
    return score
# end of scrsbble

def alternative(word):
    def scrabble_value(character):
        table: {
            "AEIOULNSTR" : 1,
            "DG" : 2,
            "BCMP" : 3,
            "FHVWY" : 4,
            "K" : 5,
            "JX" : 8,
            "QZ": 10
        }
        for key in table.keys():
            if character in key:
                return table[key]
        return 0
    # end of scrabble_value
    score = 0
    for c in word:
        score += scrabble_value(c)
    return score
#end of alternative
def scores(word_list):
    result = []
    for word in word_list:
        result.append(scrabble(word))
    return result

def i_sort(arr1, arr2):
    # let arr1 be list of words
    # let arr2 be list of their scores
    for i in range(len(arr2) - 1):
        for j in range(i+1, 0, -1):
            if arr2[j] > arr2[j-i]:
                arr2[j], arr2[j-1] = arr2[j-1], arr2[j]
                arr1[j], arr1[j-1] = arr1[j-1], arr1[j]

test = ["CAT", "DOG", "SUN", "BED", "QUIZ"]
test_scores = scores(test)

i_sort(test, test_scores)
print(test, test_scores)

def combine(arr1, arr2):
    # let arr1 be list of words
    # let arr2 be list of their scores
    result = {}

    for i in range(len(arr1)):
        word = arr1[i]
        score = arr2[i]
        result[word] = score
    
    return result

# Practice Example
table = {
    "Student" : 83,
    "Student1" : 86,
    "Student2" : 97,
    "Student3" : 100,
    "Student4" : 80
}
students = list(table.keys())
grade = list(table.values())
def highgrade(students, grade):
    for i in range(len(grade) - 1):
        for j in range(i + 1, 0, - 1):
            if grade[j - 1] < grade[j]:
                grade[j - 1], grade[j] = grade[j], grade[j - 1]
                students[j - 1], students[j] = students[j], students[j - 1]
            else:
                break
    table1 = {}
    for i in range(len(grade)):
        table1[grade[i]] = students[i]
    return table1
print(highgrade(students, grade))

# My Solution
def fibonacci(number):
    table2 = {
        0: 0,
        1: 1
    }
    if number == 0 or number == 1:
        return number
    else:
        for i in range(2, number + 1):
            table2[i] = table2[i - 2] + table2[i - 1]
    return table2[number]
print(fibonacci(20))
    
# In Class
# Fibonacci :o
def fib(n):
    table = {
        0:0,
        1:1
    }
    for ctr in range(2, n+1):
        if ctr in table: # *Important* is ctr a key in table, in operator (string/list) 0(n), in operator (dict) 0(1), value = .values 0(n)
            return table
        else:
            table[ctr] = table[ctr - 2] + table[ctr - 1]
    
    return table[n]
print(fib(20))

# Keys must be immutable
# Values anything, can be dict, in dict, in dict
# len(a), str(a), type(a) x in a = check for key x 0(1), x not in a 0(1)
# A.clear() no key/value, a.copy() copy, .dictcopy$
# A.keys() = all keys, A.values() = all values, A.items() = both [(key,value), ...]
# A.get(address) or A[address]
# del A[address]
# empty dict "name" == {}, empty dict "name["address"] == value
# for key, value ub students.items():
#   print('key:', key)
#   print('Value:', value)