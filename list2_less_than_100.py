#Given a list of numbers, determine if each item in the list is lower than 100.
#The function should take in the list as a parameter and 
# return a boolean value (False if there are any numbers 
# greater than or equal to 100, True if all numbers are less than 100).
#Leave a comment above the function stating the time complexity.
#Send a screenshot of your solution and time complexity comment 
# to your personal instructors chat.

#O(n) linear

def less_than_100(list_of_numbers):
    for num in list_of_numbers:
        if num>99:
            print('False')
            return False
    print('True')
    return True
less_than_100([1,3,44,34])