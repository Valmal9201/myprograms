# 1
def q1(x): # factorial
    if x == 1 or x == 0:
        return 1
    else:
        return x * q1(x - 1)

print("Factorial", q1(5))

# 2
def power(base, exponent): # Exponential
    if base == 0 and exponent == 0:
        return 1
    elif base == 0 or base == 1:
        return base
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * power(base, exponent - 1)

print("Power", power(2, 4))

# 3
def is_palindrome(word): # Palindrome
    if len(word) <= 1:
        return True
    elif len(word) <= 3:
        return word[0] == word[-1]
    else:
        if word[0] != word[-1]:
            return False
        else:
            return True and is_palindrome(word[1:-1])
        
print("Palindrome", is_palindrome("tacocat"))

# 4
def reverse_str(word):
    def helper(text, result = "", i = - 1):
        if i == (- 1 * len(text)):
            return result + text[i]
        else:
            return helper(text, result + text[i], i - 1)
    
    # Base Case 1 & 2 -> Single and empty
    if len(word) <= 1:
        return word
    else:
        return helper(word)
        
print("Reverse", reverse_str("Park"))
# str > list = O(n)
# list > str = O(n)

# Base case, recursive call, work towards base case

# 5
def maximum(array):
    def helper(arr, largest, i = 1):
        if i >= len(arr):
            return largest
        else:
            if arr[i] > largest:
                return helper(arr, arr[i], i + 1)
            else:
                return helper(arr, largest, i + 1)
    # end of helper
    if not array:
        return None
    elif len(array) == 1:
        return array[0]
    else:
        return helper(array, array[0])

def maximum2(array):
    if not array:
        return None
    elif len(array) == 1:
        return array[0]
    else:
        largest = array[0]
        if largest > maximum2(array[1:]):
            return largest
        else:
            return maximum2(array[1:])
    return largest

array = [3, 1, 4, 5, 1, 9]
print("Max1", maximum(array))
array1 = [3, 1, 4, 5, 1, 8]
print("Max2", maximum2(array1))

# 6
def mergeIt(arr1, arr2):
    if not arr1 and not arr2:
        return []
    elif not arr1:
        return arr2
    elif not arr2:
        return arr1
    else:
        if arr1[0] < arr2[0]:
            return [arr1[0]] + mergeIt(arr1[1:], arr2)
        else:
            return [arr2[0]] + mergeIt(arr1, arr2[1:])

print("Merged", mergeIt([1, 3, 5], [2, 4, 6]))

# 7
def prime(num, divider = 3):
    if num in {2, 3}:
        return True
    elif num % 2 == 0 or num < 2:
        return False
    else:
        if divider == num:
            return True
        else:
            if num % divider == 0:
                return False
            else:
                return prime(num, divider + 2)

print("Prime", prime(25))

# 8
def primeFactors(num, divider = 2):
    if num == 1: #1. Establish our base case
        return []
    elif num % divider == 0: # 2. work towards base num // divider
        return [divider] + primeFactors(num // divider, divider) 
        # 3. return to craft your solution by recalling itself
    else:
        return primeFactors(num, divider + 1)
    
print("Prime Factors", primeFactors(90))

# 9
def stairs(n):
    if n == 0 or n == 1:
        return n
    else:
        return stairs(n - 1) + stairs(n - 2)

print("Stairs", stairs(18))

# 10
def digitSum(str, sum = 0, list = []):
    for i in str:
        
    if len(list) == 1:
        return list[0]
    else:
        return sum + digitSum(str[1: ], sum)

print(digitSum(list("8765")))

# Teacher Solutions
# 7
def is_prime(num):
    def helper(num, divider):
        if num == divider:
            return True
        else:
            if num % divider == 0:
                return False
            else:
                return helper(num, divider+2)
    
    if num == 1:
        return False
    elif num in {2,3}:
        return True
    elif num % 2 == 0:
        return False
    else:
        return helper(num, 3)
# end of is_prime()

def is_prime2(num, divider=3, tail=True):
    if not tail:
        return False
    elif num == divider:
        return tail
    elif num <= 1:
        return False
    elif num in {2,3}:
        return True
    elif num % 2 == 0:
        return False
    else:
        if num % divider == 0:
            return is_prime2(num, divider, False)
        else:
            return is_prime2(num, divider+2, True)
# end of is_prime2()

# Q8. Prime Factors of a Number
def prime_factors(num, divider=2):
    if num == 1:
        return []
    elif num == divider:
        return [num]
    else:
        if num % divider == 0:
            return [divider] + prime_factors(num//divider, divider)
        else:
            return prime_factors(num, divider+1)
# end of prime_factors()

def prime_factors2(num, divider=2, tail=[]):
    if num == 1:
        return tail
    elif num == divider:
        return tail + [num]
    else:
        if num % divider == 0:
            return prime_factors2(num//divider, divider, tail+[divider])
        else:
            return prime_factors2(num, divider+1, tail)
# end of prime_factors2()

# Q10. String Binary Number to Integer Digits
def to_int(binary):
    if not binary:
        return 0
    elif binary == '1':
        return 1
    elif binary == '0':
        return 0
    else:
        if binary[0] == '1':
            exponent = len(binary)-1
            return 2**exponent + to_int(binary[1:])
        else:
            return to_int(binary[1:])
# end of to_int()

def to_int2(binary, tail=0):
    if not binary:
        return tail
    else:
        if binary[0] == '1':
            exponent = len(binary)-1
            return to_int(binary[1:], tail + 2**exponent)
        else:
            return to_int(binary[1:])
# end of to_int2()

# Q11. Twenty Questions
def twentyQ(start=1, end=100, q=0):
    if q == 20:
        print("I lose!")
        return False
    else:
        mid = (start+end) // 2
        user = input(f"Is your number {mid}? (Y/N): ")
        q = q + 1

        if user in 'Yy':
            print(f"I win with {q} questions asked!")
            return True
        else:
            user = input(f"Is your number higher or lower than {mid}? (H/L): ")
            q = q + 1
            if user in 'Hh':
                return twentyQ(mid+1, end, q)
            else:
                return twentyQ(start, mid-1, q)
# end of twentyQ()