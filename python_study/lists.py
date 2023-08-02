# Lists (array)
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)
print(names[1])
print(names[2:])
print(names[2:4])
    # when using a range for lists the output will return all of the items from the first input index up to, excluding, the second input index 
names[3] = 'Alex'
print(names)

numbers = [3, 4, 2, 5, 6, 10]
max = numbers[0]
for number in numbers: 
    if number > max:
        max = number
print(max)

# 2D Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)

# List Methods/Functions
nums = [5, 2, 1, 5, 7, 2, 2, 4]
nums.append(20)
    # list.append(x) adds the x to the end of the list
nums.insert(0, 30)
    # list.insert(index, x) inserts the x at the input index given
nums.remove(7)
    # list.remove(x) searches for and removes x from the list
print(nums.index(2))
    # list.index(x) searches for x within the list and then returns its index within the list 
    # if x does not exist in the list it will throw an error 
print(30 in nums)
    # x in list checks for the existence of x in a list and returns a boolean 
print(nums.count(5))
    # list.count(x) counts and returns the number of times x appears in your list
nums.sort()
    # list.sort() sorts the items in our list in ascending order
nums.reverse()
    # list.reverse() reverses the order of the items in our list 
    # in this case along with nums.sort() our list will be ordered in descending order
nums2 = nums.copy()
    #list.copy() creates a copy of our original list, any changes on this new list will NOT be reflected in the original list
nums2.append(50)
print(nums)
print(nums2)
# nums.clear()
    # list.clear() removes all of the items within a list 

# Remove duplicates from list
nums1 = [5, 2, 1, 5, 7, 2, 2, 4]
uniqes = []
for n in nums1:
    if n not in uniqes:
        uniqes.append(n)
print(uniqes)

# Tuples
nums3 = (1, 2, 3)
    # tuples are represented by using parentheses (), while lists are represented by using square brackets []
    # tuples are similar to lists but are instead immutable (can not be modified(can't add or remove items))
    # many of the list methods can be used on a tuple except for append, insert, and remove

# Unpacking 
coordinates = (1, 2, 3)
x, y, z = coordinates
    # this is unpacking, it essentially is a shorthand version of this:
        # coordinates[0] = x
        # coordinates[1] = y
        # coordinates[2] = z
        # assigning each of the first 3 items of our tuple into their own variables 

