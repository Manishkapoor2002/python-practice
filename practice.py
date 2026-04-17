# Given a list of words, return a new list containing only the words that are palindromes, converted to uppercase.
#
# A palindrome reads the same forward and backward.

words = ["level", "python", "madam", "code", "radar"]

result = [word for word in words if word.upper() == word[::-1].upper() ]
print(result)



# Write a function that takes a string and returns all duplicate characters along with their counts.
# Requirements
# Case-insensitive ("A" and "a" are the same)
# Ignore spaces
# Return a dictionary where:
# key = duplicated character
# value = number of occurrences
# Only include characters that appear more than once

input_string = "Programming"
# Example:
# {
#     "r": 2,
#     "g": 2,
#     "m": 2
# }
 
 
def get_duplicate_count(sentence : str):
    clean_sentence = sentence.lower().replace(" ","")
    
    dict = {}
    
    for char in clean_sentence:
        dict[char] = dict.get(char,0)  + 1 
        
    return {char : count for char,count in dict.items() if count > 1 }


print(get_duplicate_count(input_string))
