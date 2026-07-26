import numpy as np
#this method only works with the sorted array
def find_two_numbers(numbers, target):
    right=len(numbers)-1
    left=0
    while left< right:
        total= numbers[left]+ numbers[right]
        if total==target:
            return [numbers[left], numbers[right]]
        elif total> target:
            right=right-1
        else :
            left = left-1
    return -1

arr= np.arange(1,10,1)
print(find_two_numbers(arr, 6))
