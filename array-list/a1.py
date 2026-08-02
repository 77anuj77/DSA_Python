import numpy as np

marks = [88,43,61,43,56]
arr= np.array(marks)
print(arr[-1], " ")

#list can be used as array
#using O(1) with 
''' #append() because it is adding in the end or inserting in middle its is like insertion sort
# delete() or pop(index_no) it delete and shift the lest element'''
print(marks.pop(1))
print(marks.append("anuj"))
print(marks)
print(marks.insert(1, "anujp"))
print("original: " , marks)

#O(k)
'''slicing''' 
print("sliced: ",marks[::-1])
print("reversing")
for marks in reversed(marks):
    print(marks)

print("matrix")
mar=[23,45,67,88,56,44,33,44,55]
clas=np.reshape(mar,(3,3))
print(clas)
print(" martix ")
for i in clas:
    for j in i:
        print(j,end=" ")
    print(" ")