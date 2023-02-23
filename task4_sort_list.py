# Given a list of numbers, manually sort the list into ascending order 
# (may not use built in .sort() method).
# Suggested strategy:
# Starting with the first two numbers, compare them to see which is larger. 
# Place the lower number to the left and the higher number to the right.
# Iterate through the list, checking each pair of numbers one at a time.
# Repeat from the start until the entire list is sorted.
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment 
# to your personal instructors chat.

#O(n^2) quadratic

def sort_list(list):
    for num1 in range(0,len(list)):
        for num2 in range(0,len(list)):
            if list[num2]>list[num1]:
                item=list[num1]
                list[num1]=list[num2]
                list[num2]=item
    return list

print(sort_list([5,7,23,4,65,7]))