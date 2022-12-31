#binary search is spliting data in half, and measuring and finding target
#function that takes a list and target parameter
#multiple variables : middle, start , end , steps
#recursion, or a while loop to keep spliting data
#increse steps each time a split is done
#conditions to track target position
import numpy as np
def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0
    while (start<=end):
        print("step", steps, ":", str(list[start:end+1]))
        steps = steps+1
        middle = (start+end) // 2
        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle -1
        else:
            start = middle +1
    return -1
          



my_list = [1,2,3,4,5,6,7,8,9]
target = 1

binary_search(my_list, target)

      