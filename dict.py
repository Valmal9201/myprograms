# My Solution
def dictpractice(value):
    sequence = {
        1: 1
    }
    ctr = 1
    old = 0
    for i in range(1, value):
        num = i
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            ctr += 1
        if ctr > old:
            sequence[i] = ctr
            store = i
            old = ctr
        ctr = 1
    return store, sequence[store]

print(dictpractice(1000000))

#In Class Solution
def collatz(num, table):
    if num == 1:
        return 1
    elif num in table:
        return table[num]
    else:
        next_num = 0
        if num % 2 == 0:
            next_num = num // 2
        else:
            next_num = (3 * num) +1
        table[num] = 1 + collatz(next_num, table)
        return table[num]

table = {
    1: 1
}
max_size = 0
max_answer = 0

for num in range(1, 1000000):
    current_size = collatz(num, table)

    if current_size > max_size:
        max_size = current_size
        max_answer = num

print(max_answer, max_size)