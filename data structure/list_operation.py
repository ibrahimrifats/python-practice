print("------append------ \n")

arr=[21,12,34,23]
arr1=[4,65,23,65]
a = 3
# add an item to the end of the list
arr[len(arr):] = [a]
print("after append(value): ",*arr)
# using append
arr.append(a)

print("after append: ",*arr)

print("------Extend------ \n")

arr[len(arr):] = arr1

print("after extend: ",*arr)

arr.extend(arr1)
print("after extend(array): ",*arr)


print("------Insert------ \n")

arr= [23,34,743,32]
# insert(index,value)
arr.insert(0,1)
print("after insert(index, value): ",*arr)


print("------Remove------ \n")

print(*arr)
# remove(value that is exist in list and you wannna delete)
arr.remove(743)

print(*arr)


print("------pop------ \n")
# pop(index value. which index value you wanna delete from array) 
arr.pop(1)
print("index value 1 deleted: ", *arr)

print("------clear------ \n")

# Remove all items from the lsit : `del array[:]`

del arr[:]

print("after remove all element from array.clear or del array[:]: ",*arr)

arr= [23,34,743,32]

arr.clear()
print("after remove all element from array.clear or del array[:]: ",*arr)

arr= [23,34,743,32,23]
print("------count item in array------ \n")

result = arr.count(23)
print("count number of element 23 exists in array: ",result)

print("------reverse array------ \n")

arr.reverse()
print("result after reverse: ",arr )

print("------sort array------ \n")

arr.sort()
print("array after sort : ", arr)

print("------pop using array[:n]------ \n")

print("pop last 2 element : ",arr[:2])


print("------copy array------ \n")

copy_arr = arr.copy()
print("after copy : ", copy_arr)

print("------index(x[, start[,end]]------ \n")

print("find index() of specific value: ",copy_arr.index(32))

arr= [23,34,743,32,23]
fruit = ['apple','orange', 'pear','banana', 'apple', 'banana']


print("Find the index of 'apple' between index 1 and 5 (exclusive) \n")

index = fruit.index('apple', 1,5)
print("index found in : ", index)

print("------find index in fixed area------ \n")
index = arr.index(743, 1,5)
print("index found in : ", index)