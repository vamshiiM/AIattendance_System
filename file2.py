# ### to check is a triangle is equilateral,isocelse,scalene
#
# print("ENTER THE SIDES OF TRIANGLE:")
# s1=int(input("S1:"))
# s2=int(input("S2:"))
# s3=int(input("S3:"))
# print("THE ANS IS:")
#
#
# def func():
#     if s1== s2 == s3:
#         print("equilateral")
#     elif s1 == s2 or s2 == s3 or s1== s3:
#         print("isoceles")
#     else:
#         print("SCALENE")
# func()
# CODE FOR DIVIDIBLE BY 3 AND 7 VALA
# def mul():
#     print("HERE'S THE LIST")
#     for i in range(1500,2700):
#         if i%7==0 and i%3==0:
#             print(i)
# mul()

# CODE FOR MULTIPLICATION TABLE
# def mul2():
#     num = int(input("ENTER THE NUMBER: "))
#     print("HERE THE TABLE")
#     for i in range(1, 11):
#         ans = num * i
#         print(f"{num} x {i} = {ans}")
#
# mul2()

# CODE FOR EVEN ODD
# def eo(numb):
#     a=0
#     b=0
#     for i in numb:
#         if i%2==0:
#            a+=1
#         else :
#             b+=1
#     return a,b
#
# tu=[1,2,3,4,5,6,7,8,9,10]
# even,odd=eo(tu)
# print("EVEN NUMBERS:",even)
# print("ODD NUMBERS:",odd)
#
# def sum_of_digits(n):
#     if n < 10:
#         return n  # Base case: if n is a single digit, return n
#     else:
#         return n % 10 + sum_of_digits(n // 10)  # Recursively call the function with the quotient of n divided by 10
#
# # Get input from the user
# num = int(input("Enter a non-negative integer: "))
#
# # Calculate the sum of digits
# result = sum_of_digits(num)
#
# # Display the result
# print("The sum of digits of", num, "is:", result)
#
#
# def is_palindrome(number):
#     # Convert the number to a string for easier comparison
#     num_str = str(number)
#
#     # Check if the string is equal to its reverse
#     if num_str == num_str[::-1]:
#         return True
#     else:
#         return False
#
#
# # Test the function
# num = int(input("Enter a number to check if it's a palindrome: "))
#
# if is_palindrome(num):
#     print(num, "is a palindrome.")
# else:
#     print(num, "is not a palindrome.")

# code for fibo series




### plaindriome
#
# def palin(num):
#     string=str(num)
#     if string==string[::-1]:
#         return True
#     else :
#         return False
#
# let=int(input("ENTER THE NUMBER TO CHECK IS IT PALINDROME OR NOT:"))
# palin(let)
# print(palin(let))


# def palin(num):
#     default=[0,1]
#     if num==0:
#      return(f"INVALID")
#     elif num ==1:
#      return 0
#     elif num ==2:
#         return default
#
#     for i in range(2,num):
#         new_num=default[-1]+default[-2]
#         default.append(new_num)
#     return default
#
# mun = int(input("ENTER THE NUMBER:"))
# print(palin(mun))



### factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage
num = 5
print("Factorial of", num, "is:", factorial(num))

#GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
num1 = 48
num2 = 18
print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))






