#Given a numeric value, determine if it is even or odd.
#The function should take the value in as a parameter 
# and return a boolean value (True if even, False if odd).
#Leave a comment above the function stating the time complexity.
#Send a screenshot of your solution and time complexity comment 
#to your personal instructors chat.

# O(1) constant

def even_or_odd(num):
    if num%2==0:
        print('True')
        return True
    else:
        print('False')
        return False

even_or_odd(44)