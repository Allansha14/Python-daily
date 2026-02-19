# problem : Most Frequent Element

'''Task:

Given a list of integers, return the element that appears the most times.

Write a Python function:
def most_frequent(nums):

Input:

[1, 3, 2, 3, 4, 3, 5]
Output:
3

Input:
[5, 5, 2, 2, 3]
Output:
5
👉 If two numbers have same frequency, return the one that appears first.
'''

# What is the input?
#What is the expected output?
#What data structure will you use?
#Time complexity?

def most_frequent(nums):
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    most_frequent_num = max(frequency, key=frequency.get)
    return most_frequent_num
# Test cases
print(most_frequent([1, 3, 2, 3, 4, 3, 5]))  # Output: 3
print(most_frequent([5, 5, 2, 2, 3]))  # Output: 5
