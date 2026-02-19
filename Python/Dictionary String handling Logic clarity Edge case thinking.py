'''Today we train:

Dictionary

String handling

Logic clarity

Edge case thinking'''

# Problem – First Non-Repeating Character

'''
Task:

Given a string, return the first character that does NOT repeat.

If all characters repeat, return None.

Example 1:

Input:

"leetcode"

Output:

"l"

Example 2:

Input:

"aabbcc"


Output:

None
'''

def first_unique_char(s):
    unique_char = {}    
    # Step 1: Count the frequency of each character
    for char in s:
        if char in unique_char:
            unique_char[char] += 1
        else:
            unique_char[char] = 1
            
    # Step 2: Find the first character with a count of 1
    for char in s:
        if unique_char[char] == 1:
            return char
            
    return None  # Return None if no unique character exists

# Correct way to call the function:
print(first_unique_char("leetcode"))   # Output: "l"
print(first_unique_char("aabbcc"))     # Output: None