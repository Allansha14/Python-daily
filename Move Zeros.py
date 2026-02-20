'''Day 3 Mission

Today we train:

Two pointers thinking

In-place array modification

Clear condition writing '''

# Problem: Move Zeros

''' Write a function:

def move_zeros(nums):
    
that takes a list of integers and moves all zeros to the end while maintaining the order of non-zero elements. The function should modify the list in-place and return it.
Task:

Given a list of integers, move all zeros to the end
while maintaining the order of non-zero elements.

You must modify the list in-place.

Return the modified list.

Example 1:

Input:

[0,1,0,3,12]

Output:

[1,3,12,0,0]
Example 2:

Input:

[0,0,1]

Output:

[1,0,0]'''

def move_zeros(nums):
    
    non_zero = []
    
    # Step 1: collect non-zero elements
    for num in nums:
        if num != 0:
            non_zero.append(num)
    
    # Step 2: count zeros
    zero_count = len(nums) - len(non_zero)
    
    # Step 3: add zeros at end
    result = non_zero + [0] * zero_count
    
    return result


print(move_zeros([0,1,0,3,12]))
print(move_zeros([0,0,1]))