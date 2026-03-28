# Strings, list and dictionary
def things(num):
    if num < 1:
        return [] # [] is an empty list
    
    a_list = [] # lists are mutable :D * ON TEST
    for c in range(num): # 0, 1, 2, ... num
        value = input("Enter a value: ")
        a_list.append(value) # add to the end
    
    return a_list
# YAY
# Nag a ram!/Anagram
# # string to list ... where charcters are position in list
# for ch in word1:
#     if ch.isalpha():
#         # only adding alphatebtical characters
#         a_list.append(ch.lower())

# If word1 has charcters that doesn't exist in word2 ... NOT ANAGRAMS
# If the length of words aren't equal NOT ANAGRAMS
# If a character isn't used the same amount NOT ANAGRAMS
# When towrds are sorted, and euqal to each other ... ANAGRAM!! :)

word1 = input()
word2 = input()
def isAnagram(word1, word2):
    a_list = list(filter(str.isalpha, word1.lower()))
    b_list = list(filter(str.isalpha, word2.lower()))
    a_list.sort()
    b_list.sort()
    if a_list == b_list:
        return True
    return False
print(isAnagram(word1, word2))

def isAnagram(word1, word2):
     # 1 of many solutions
    a_list = list(word1.lower())
    b_list = list(word2.lower())
    if len(word) != len(word):
        return False
    for c in word1:
        if c.isalpha():
            if word1.count(c) != word2.count(c):
                return False
    return True

# In Class Solution:
def clean(word):
    # remove digits, makes it lowercase, remove special charcters
    result = ""
    for c in word:
        if c.isalpha():
            result += c.lower()
    return result

# Two anagram solutions:
# 1. Sort both strings and compare equality
def anagram1(word1, word2):
    word1 = list(clean(word1))
    word2 = list(clean(word2))
    word1.sort() # only list
    word2.sort() # word2 = sorted(word2)
    return word1 == word2

# 2 Compare the frequency of characters
def anagram1(word1, word2):
    word1 = clean(word1)
    word2 = clean(word2)
    dic_word1 = {}
    dic_word2 = {}
    for char in word1:
        if char in dic_word1: # Frequency Table
            
            dic_word1[char] += 1
        else:
            dic_word1[char] = 1

    for char in word2:
        if char in dic_word2:
            dic_word2[char] += 1
        else:
            dic_word2[char] = 1
    
    for key, value in dic_word1.items():
        if key not in dic_word2:
            return False
        elif dic_word2[key] != value:
            return False
    
    return len(dic_word1.keys()) == len(dic_word2.keys())

# How to convert a list of characters -> string
a = list("Hello") # H,e,l,l,o
b = 'LOL'.join(a) #HLOLeLOLlLOLlLOLo or 
print(b)

a = list("Hello") # H,e,l,l,o
b = ''.join(a) #Hello #String method
print(b)

# Some points:
# - if two strings are cleaned, then anagrams must have equal length
# - if two strings are cleaned, the anagrams must share the same set of characters

# How to sort w/o sorted() and .sort()