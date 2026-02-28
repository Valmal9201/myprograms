# My Solution
def digitSum(num):
    """ digitSum determines the number of rimes you would need to add its digit until it becomes a signle digit

    num: integer input; expect > 0; orginal number

    returns:
    ctr for number of times
    """
    total = 0
    ctr = 0
    sum1 = 0
    total1 = 0

    while num != 0:
        total += num % 10
        num = num // 10
        if num == 0:
            ctr += 1
    total1 = total

    while total1 > 9:
        total1 = 0
        while total > 9:
            total1 += total % 10
            total = total // 10
            if total <= 9:
                ctr = ctr + 1
                break
        total = total1
    return ctr
# end of digitsum()

num = int(input())
print(digitSum(num))


# In Class Solution
def digitSum(num):
    total = 0
    while num != 0:
        last = num % 10
        total += last
        num = num // 10

    value = int(input())
    counter = 0
    while value > 9:
        value = digitSum(value)
        counter = counter + 1

print(f"It took {counter} tries.")