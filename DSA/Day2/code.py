# Create an array of 5 integers and print all elements using a loop.
arr1=[1,2,3,4,5]
for i in arr1:
    print(i)
# Insert an element at the beginning, middle, and end of an array.
arr1.insert(0,0)
arr1.insert(3,3)
arr1.append(6)
print(arr1)
# Delete a given element from an array.
arr1.remove(3)  #value

# Search for an element in an array and print its index.
for i in arr1:
    if i == 5:
        print(arr1[i])
# Update a specific element in an array.
arr1[2]=80


# Find the sum and average of all array elements.
sum_val=0
for i in arr1:
    sum_val+=i
print(sum_val)
avg=sum_val/len(arr1)
print(avg)
# Find the maximum and minimum elements in an array.
min_val=arr1[0]
max_val=arr1[0]
for i in arr1:
    if min_val>i:
        min_val=i
    if max_val<i:
        max_val=i
print(max_val,min_val)
# Count even and odd numbers in an array.
even_count=0
odd_count=0
for i in  arr1:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1

# Reverse an array without using built-in functions.


# Merge two arrays and display the result.
# arr2=[1,23,4,56,7,78,]
# arr3=[1,2,3,4]
# arr2.append(arr3)
# Copy elements of one array into another.

# Print all elements greater than a given value.

# Print all pairs of elements (nested loop → O(n²)).

# Find the second largest number in an array.

# Check if an element exists in an array (True/False).