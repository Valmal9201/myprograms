# # Is this number a prime number?
# # 1, 4, 6, 8, 10, 12
# # 9, 27

# # print "Enter a number: ", asks for input form user, converts to int
# num = int(input("Enter a number: "))
# print(num)
# # Logic = if num has on 2 factors, prime!
# factor_counter = 0
# divider = 1
# while divider <= num:
#     if num % divider == 0: # this means divder is a factor!
#         factor_counter += 1
#     divider += 1
# # end of while loop
# if factor_counter == 2:
#     print(f"{num} is a prime number!")
# else:
#     print(f"{num} is a composite number!")

# # inefficient, b/c checks all numbers, 69 feels prime, 42 easy to tell
# # 2 only even prime, all other odd
# num = int(input("Enter a number: "))
# if num != 2 and num % 2 == 0:
#     print(f"{num} is a composite number.")
# elif num in [2,3]: # technically I should write: num in {2,3}
#     print(f"{num} is a prime number.")
# else:
#     # guaranteed 5 or higher
#     # divider = 1
#     # counter = 0
#     # while divider <= num:
#     # if num % divider == 0:
#     #     counter += 1
#     # divider += 1

#     # if counter >= 2:
#     #     break
    
#     divider = 2
#     # counter = 0
#     isPrime = True
#     while divider < num:
#         if num % divider == 0:
#             isPrime = False
#             print(f"{num} is a composite number.")
#             break
#         divider += 1

# How Make faster
# 6 * 7 = 42, 3 * 4 = 42, 7 * 6 = 46, 4 * 3 = 12
# sqrt of N
# if n % x == 0
#     f1 = x
#     f2 = n//2

# import math # importing math module
# # Primes again
# num = int(input("Enter a number: "))
# divider = 1
# stop = int(math.sqrt(num)) + 1 # kicks and giggles
# while divider < stop:
#     if num % divider ==0:
#         quotient = num // divider
#         print(divider, quotient)
#     divider += 1

# Actual Faster
import math # importing math module
num = int(input("Enter a number: "))
stop = int(math.sqrt(num)) + 1 # stop = int(num ** 0.5) + 1
isPrime = True # variable intialization
if num == 2 or num == 3:
    isPrime = True
elif num % 2 == 0:
    isPrime = False
else:
    divder = 3
    isPrime = True
    while divider <= stop:
        if num % divider == 0:
            isPrime = False
            break
        divider += 2
#Output
if isPrime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is a composite number.")