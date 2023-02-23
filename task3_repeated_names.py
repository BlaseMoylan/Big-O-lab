# Given a list of names, determine if any names are contained 
# in the list more than once.
# The function should take in the list as a parameter 
# and return a boolean value (True if there are any repeated names, 
# False if there are no repeats).
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment 
# to your personal instructors chat.

# O(n^2)

def duplicate_names(list_of_names):
    for name in list_of_names:
        count=0
        for item in list_of_names:
            if item==name:
                count+=1
                if count==2:
                    print('there is a name contained more than once!')
                    return True
    print('no duplicates')
    return False

duplicate_names(['james','ham','jane','dan'])
