# nth fibonacci number
def fibo(num):
    a=0
    b=1
    if num==0:
        return 0
    elif num ==1:
        return 1
    elif num>1:
        for num in range(2,num+1):
           c=a+b
           a=b
           b=c
        return b

print(fibo(9))

#
# def fibonacci(n):
#     fib_series = [0, 1]  # Initialize the Fibonacci series with the first two numbers
#
#     if n <= 0:
#         return "Invalid input! Please enter a positive integer."
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return fib_series
#
#     # Generate Fibonacci series
#     for i in range(2, n):
#         next_num = fib_series[-1] + fib_series[-2]
#         fib_series.append(next_num)
#
#     return fib_series
#
#
# # Test the function
# num_terms = int(input("Enter the number of terms in the Fibonacci series: "))
# fib_series = fibonacci(num_terms)
# print("Fibonacci series up to", num_terms, "terms:", fib_series)
#
#
# # fizzbuzzz
# def mul():
#   for num in range(1,51):
#     if num%3==0 & num%5==0:
#         print("FUCK OFF")
#     elif num%3==0:
#         print("FUCK YOURSLEF")
#     elif num%5==0:
#         print("FUCK SIDEWAYS")
#     else:
#         print(num)
#
# mul()



# pattern
n=int(input("ENTER THE NUMBER:"))
for i in range(1, n):
    print('*' * i)


