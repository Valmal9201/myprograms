# Abundant, Deficient, Perfect? My Solution
# import math
# num = int(input("Enter a number: "))
# stop = int(math.sqrt(num)) + 1
# isPrime = True
# divider = 2
# sum = 0
# while divider < stop:
#     if num % divider == 0:
#         quotient = num // divider
#         sum = sum + divider + quotient
#     divider += 1
# #Output
# sum += 1
# if sum == num:
#     print(f"{num} is a perfect number.")
# elif sum < num:
#     print(f"{num} is a deficient number.")
# else:
#     print(f"{num} is a abundant number.")

# Perfect Numbers Solutions in Class Solution
# num = int(input("Enter a number: "))

def numType(num):
    # Doc String, 3 """ 1st line for purpose, define variable,
    # and values returned.
    """ numType determine if input is either abundant, perfect, or deficient

    num: integer input; expect > 0

    returns:
    1 for abundant
    0 for perfect
    -1 deficient
    """
    total = 1 # adding factor 1
    stop = int(num ** 0.5) + 1
    divider = 2
    while divider < stop:
        if num % divider == 0:
            # divider is a factor
            other = num // divider
            if divider != other:
                total += divider
                total += other
            else:
                total += divider
        divider += 1
    # end of while loop
    if total < num:
        # print(f"{num} is a deficient number.")
        return -1
    elif total > num:
        # print(f"{num} is a abundant number.")
        return 1
    else:
        # print(f"{num} is a perfect number.")
        return 0
# end of numType()

# # Perfect Square < 1 000 000 My Solution
# import math
# num = 1
# stop = int(math.sqrt(1000000)) + 1
# sum = 0
# while num < stop:
#     sum += num * num
#     num += 1
# #Output
# print(sum)

# Perfect Square < 1 000 000 In Class Solution
value = 1
perfect_sum = 0
while value <= 1000000
    if numType(value) == 0:
        # numType() returned a perfect result
        perfect_sum += value
    value += 1

print(f"Total sum of all perfect number under 1000 000:" {perfect_sum})