class People: # CREATING A CLASS
   x=5 # THINGS IN THE CLASS

p1=People() # CREATING THE OBJECT
print(p1.x)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person('VAM',12)
print(p1.name)
print(p1.age)

## palindrome or not
def palin(num):
    string=str(num)
    if string == string[::-1]:
         print(f"{string} IS A PALINDROME")
    else :
        print(f"{string} IS NOT A PALINDROME")
stuff=int(input("ENTER THE NUMBER TO CHECK WHETHER IT IS A PALINDROME OR NOT:"))
palin(stuff)

### fibonacci numbers
def fibo(num):
    a=0
    b=1
    if num <=0:
        print("NOT VALID")
    elif num ==1:
        print("0")
    elif num > 1:
        for num in range(2,num+1):
            c=a+b
            a=b
            b=c
        return b

entry=int(input("ENTER THE NUMBER:"))
print(fibo(entry))

# anagrams
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted versions of the strings are equal
    return sorted(str1) == sorted(str2)


# Example usage
string1 = "listen"
string2 = "silent"
if are_anagrams(string1, string2):
    print("The strings", string1, "and", string2, "are anagrams.")
else:
    print("The strings", string1, "and", string2, "are not anagrams.")


#armstrong
def is_armstrong(number):
    # Convert number to string to iterate over digits
    num_str = str(number)
    num_digits = len(num_str)
    total = 0

    # Calculate the sum of each digit raised to the power of the number of digits
    for digit in num_str:
        total += int(digit) ** num_digits

    # Check if the total equals the original number
    return total == number


# Example usage
num = 153
if is_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

