a_list = [3, 1, 4, 1, 5, 9]
b_list = a_list.copy()

b_list[-1] = "POOPOO LOL!"
print(a_list)
print(b_list)

# Changes both
# To save RAM, Same address
# To make it actually do what you want: list.copy or list[:]

empty_string1 = ""
empty_string2 = ''
