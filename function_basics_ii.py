#Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(number):
    num_list = [*range(0, number + 1)]
    num_list.reverse()
    return(num_list)
print(countdown(6))


#Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def p_and_r(list):
    print(list[0])
    return(list[1])
test_list = [0,1,2,3]
print(p_and_r(test_list))

#First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

def f_p_l(list):
    sum = list[0] + len(list)
    return sum
test_list1 = [1,2,3,4]
print(f_p_l(test_list1))

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def length_value(size, value):
    empty_list = []
    for x in range(0,size):
        empty_list.append(value)
    return(empty_list)
print(length_value(5,7))
