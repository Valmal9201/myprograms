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
num = int(input("Enter a number: "))
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
    print(f"{num} is a deficient number.")
elif total > num:
    print(f"{num} is a abundant number.")
else:
    print(f"{num} is a perfect number.")