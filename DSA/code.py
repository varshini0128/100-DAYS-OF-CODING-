# 1. Create a list of 5 student names and print the 3rd one.
student_list=['ram','ravi','sita','geetha','shyam']
print(list[2])


# 2. Write code to calculate the product of two numbers.
num1=int(input('Enter a number: '))
num2=int(input('Enter a second number: '))
product=num1*num2
print('product od two numbers: ',product)


# 3. Write a loop that prints numbers 1–10 and count iterations.
count=0
for i in range(1,11):
    print(i)
    count+=1

# 4. Write Python code for **O(1)** and **O(n²)** examples.
# O(1)
student_list=['ram','ravi','sita','geetha','shyam']
print(list[2])
# O(n²)
for i in range(1,5):
    for j in range(1,3):
        print(i,j)


# 5. Find the smallest number in a list.
list1=[22,33,44,33,4,32,56,679]
smallest=23
for num in list1:
    if smallest>num:
        smallest=num
print(smallest)


# # 6. Write an algorithm to reverse a list without using built-in functions.
list5=['1','2','3','4','5']
rev_list=[]
i=len(list5)-1
for j in range(len(list5)):
    rev_list.extend(list5[i])
    i-=1
print(rev_list)


# # 7. Count the number of even and odd numbers in a list.
even_count=0
odd_count=0
list2=[1,2,3,4,5,6,7,8,9,10]
for i in list2:
    if i%2==0:
        even_count+=i
    else:
        odd_count+=i
print(even_count,'odd')
print(odd_count)


# # 8. Find the sum of all elements in a list.
sum=0
for i in list2:
    sum+=i
print(sum)


# # 9. Write a program to check if a number is prime.

def is_prime(num):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(num, "is Not a Prime number")
                break
        else:
            print(num, "is a Prime number")
    else:
        print(num, "is Not a Prime number")

# Main program
num = int(input("Enter a number: "))
is_prime(num)



# # 10. Write an algorithm to find the maximum of three numbers.
a=int(input('enter a number: '))
b=int(input('enter a number: '))
c=int(input('enter a number: '))
if a > b and a > c:
    print('a is greatest')
if b > a and b > c:
    print('a is greatest')
if c > b and c > a:
    print('a is greatest')
# # 11. Display all pairs of elements from a list (O(n²) approach).
# Create a list
numbers = [1, 2, 3, 4]

print("All pairs of elements:")

# Nested loops → O(n²)
for i in range(len(numbers)):
    for j in range(len(numbers)):
        print(f"({numbers[i]}, {numbers[j]})")




# # 12. Write a program that prints the factorial of a given number.
fact=0
num3=int(input("Enter a number to find factorial: "))
for i in range(1,num3+1):
    fact*=i
print(fact)



# # 13. Implement a function to check if a string is a palindrome.
string = input("Enter a string: ")
reversed_string = ""
i = len(string) - 1
while i >= 0:
    reversed_string = reversed_string + string[i]
    i = i - 1
if string == reversed_string:
    print("Palindrome")
else:
    print("Not Palindrome")

# # USING USER-DEFINED FUNCTION:

def is_palindrome(string):
    # Step 1: Reverse the string manually
    reversed_string = ""
    i = len(string) - 1
    while i >= 0:
        reversed_string = reversed_string + string[i]
        i = i - 1

    # Step 2: Compare original and reversed
    if string == reversed_string:
        return True
    else:
        return False


# Main program
text = input("Enter a string: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")

# USING BUILT IN
def is_palindrome(string):
    # Using slicing to reverse the string
    if string == string[::-1]:
        return True
    else:
        return False
# Main program
text = input("Enter a string: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")




# 14. Create a list of integers and print only the unique elements.
# Create a list of integers
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 5]
print("Unique elements are:")
for num in numbers:
    if numbers.count(num) == 1:
        print(num)



# 15. Write a program that calculates the average of numbers in a list.

for i in list2:
    avg=sum/len(list2)
print(avg)