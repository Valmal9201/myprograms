# # My Attempt
# def combine(left, right):
#     list = left.append(right)
#     swapped = True
#     while swapped:
#         swapped = False
#         i = 1
#         for i in range(i, len(list)):
#             if list[i - 1] > list[i]:
#                 list[i - 1], list[i] = list[i], list[i - 1]
#                 swapped = True
#     return list

# def merge(a_list):
#     if len(a_list) <= 1: #1 base case
#         return a_list
#     left = merge(slice(0, len(a_list) // 2)) 
#     right = merge(slice(len(a_list) // 2, len(a_list)))
#     return combine(left, right) # assume left and right is sorted # return

# a_list = (3, 6, 7, 1, 4, 9, 0, 2, 3)
# for i in a_list:
# print(merge(a_list))

# In Class Example
def mergeSort(a_list): # O(n log n)
    def split(a_list):
        if len(a_list) <= 1: #1 base case
            return a_list
        
        middle = len(a_list) // 2 
        left = a_list[: middle]
        right = a_list[middle: ]
        left = split(left) # always splits left 1st
        right = split(right)

        return combine(left, right) # Combining sorted list easier thasn bubble/insertion/selection O(n + m), O(n^2), O(m^2)

    # end of merge
    def combine(list1, list2):
        if not list2:
            return list1
        if not list1:
            return list2
        
        result = []
        i = 0
        j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        # end of while
        while i < len(list1):
            result.append(list1[i])
            i += 1
        while j < len(list2):
            result.append(list2[j])
            j += 1
        
        return result
    return split(a_list)
a_list = [3, 1, 4, 1, 5, 9]
print(mergeSort(a_list))