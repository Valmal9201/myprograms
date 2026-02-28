# 1 My Solution
def repeat101(num):
    i = 1
    ctr = 0
    word = ""
    while i <= num:
        while ctr < i:
            if ctr % 2:
                word += "0"
            else:
                word += "1"
            ctr += 1
        ctr = 0
        word += "\n"
        i += 1
    return word

num = int(input("Enter the number of lines you want: "))
print(repeat101(num))

# 1 In Class Solution
def pattern(num):
    ctr = 1
    str_pattern = ""
    while ctr <= num:
        if ctr % 2 == 0:
            str_pattern += "0"
        else:
            str_pattern += "1"
        print(str_pattern)
        ctr += 1 

pattern(10)

# 2
def longString(word, word2):
    long = ""
    if len(word) < len(word2):
        long = word2
    else:
        long = word
    return long

word = input("First word: ")
word2 = input("Second word: ")
print(f"The longer word is: {longString(word, word2)}")

# 3 My Solutiom
def average(num):
    i = 1
    total = 0
    while i <= num:
        digit = int(input(f"Enter number {i}: "))
        total += digit
        i += 1
    ave = total/num
    return ave

num = int(input("Enter number of numbers that you want the average of : "))
print(f"The average of these numbers is {average(num)}")

# 3 In Class Solution
def averageInput(amount):
    total_sum = 0
    ctr = 0
    while ctr < amount:
        value = int(input())
        total_sum += value
        ctr += 1

    return total_sum/amount

averageInput(5)

# 4
def totalSum(num):
    i = num
    total = 0
    while i > 0:
        total += i
        i -= 1
    return total

num = int(input("Enter a number you wish to sum up: "))
print(f"The total of all numbers form 1 to {num} is {totalSum(num)}.")

# 5
def factor(num):
    num ** 0.5 + 1
    divisor = 2
    ctr = 2
    while divisor < num:
        if num % divisor == 0:
            ctr += 1
        divisor += 1
    return ctr

num = int(input("Enter a number that you wish to know the number of factors of: "))
print(f"{num} has {factor(num)} factors.")

# 6
def prime(num):
    isPrime = True
    stop = num ** 0.5 + 1
    check = 3
    if num == 2 or num == 3:
        isPrime = True
    elif num % 2 == 0:
        isPrime = False
    else:
        while check < stop:
            if num % check == 0:
                isPrime = False
                break
            check += 1
    prime = ""
    if isPrime:
        prime = "prime"
    else:
        prime = "composite"
    return prime

num = int(input("Enter a number you wish to check: "))
print(f"{num} is {prime(num)}.")

# 7
import math
def pythag(x1, y1, x2, y2):
    a2 = math.pow((x2 - x1), 2)
    print(a2, " a")
    b2 = math.pow((y2 - y1), 2)
    print(b2, "b")
    c = (a2 + b2) ** 0.5
    return c

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
print(f"The euclidian distance between ({x1}, {y1}) and ({x2}, {y2}) is {pythag(x1, y1, x2, y2)}.")

# 8
def gcd(num, num1):
    divisor = min(num, num1)
    while divisor > 0:
        if num % divisor == 0 and num1 % divisor == 0:
            break
        divisor -= 1
    return divisor

num = int(input("Enter your first number: "))
num1 = int(input("Enter your second number: "))
print(f"The GCD is {gcd(num, num1)}.")


# 9 In Class Solution
def power(base, exponent):
    return base ** exponent

def power1(base, exponent):
    ctr = 0
    result = 1
    while ctr < exponent:
        result = result * base
        ctr += 1
    
    return result

def power2(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        # exponent > 1
        return base * power2(base, exponent - 1)