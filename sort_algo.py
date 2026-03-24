a_list = ["e", "d", "f", "b", "a", "g", "c"]
# In Class Solution
# Thinking about sorting :)
# Bubble Sort
print(a_list)
def bubble(a_list):
    # assume a_list is unsorted :) least to greatest
    swapped = True
    while swapped:
        swapped = False
        i = 1
        # write the bubbling portion first
        for i in range(i, len(a_list)):
            if a_list[i - 1] > a_list[i]:
                # swapping identity
                a_list[i - 1], a_list[i] = a_list[i], a_list[i - 1]
                swapped = True
    return a_list
print(bubble(a_list))

# # No Return b/c not change value just order
# #In class
# a_list = ["e", "d", "f", "b", "a", "g", "c"]
# def destruction_select(a_list):
#     b_list = []
#     while a_list:
#         smoll = min(a_list)
#         b_list.append(smol)
#         a_list.remove(smol)
#     return b_list
# print(bubble(a_list))

# a_list = ["e", "d", "f", "b", "a", "g", "c"]
# def insertion(a_list):
#     for i in range(len(a_list) - 1):
#         for j in range(i + 1, 0, - 1):
#             if a_list[j-  1] > a_list[j]:
#                 a_list[j - 1], a_list[j] = a_list[j], a_list[j - 1]
#                 print(a_list)
#             else:
#                 break
#     return a_list
# print(insertion(a_list))