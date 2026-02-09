#Problem : 1

print ("Given a list 1st with elements [2, 33,222, 14, 25], you want to subtract 1from each element in the list.")

list1 = [2, 33, 222, 14, 25]
list1 = [x - 1 for x in list1]
print(list1)


# problem : 2

print("You want to print the odd numbers between 0 and 100 in Python using list comprehension " )

for num in range(0, 101):
    if num % 2 != 0:
        print(num)


# problem : 3

print("You have a list 1st containing several values, and you want to extract only the unique values from the list. ")

lst = [ 1, 2, 3, 4 , 4 , 6 , 7, 3, 4, 5, 2, 7]
unique_values =[]
for i in lst :
    if i not in unique_values:
        unique_values.append(i)
print(unique_values)

# problem : 4
print("You want to access an attribute of a function in Python and print its value. Specifically, you want to print the value of the what attribute of the function my_function. ")
def my_function():
    pass
my_function.what = "This is the value of the what attribute."
print(my_function.what)

# problem : 5
print('You have two variables, a and b, and you want to swap their values without using an intermediary variable. This operation is commonly referred to as a "value swap."')

a= 10 
b = 20

a,b = b,a
print("After swapping: a =", a, "b =", b)