
#1.Whether it is positive, negative, or zero
if a > 0 :
    print('positive')
elif a < 0 :
    print('negative')
else :
    print('zero')

#2.Whether it is even or odd
if a % 2 == 0 :
    print('EVEN')
else :
    print('ODD')

#3.Whether it is divisible by 3 and 5
if num % 3 == 0 and num % 5 == 0:
    print('divisible by 3 and 5')
elif num % 3 == 0 :
    print('divisible by 3')
elif num % 5 == 0 :
    print('divisible by 5')
else :
    print('error')

'''#4.Get the number of electricity units consumed.
   Calculate the bill:
   Units	Rate
   0–100	₹2/unit
  101–200	₹3/unit
  201–300	₹5/unit
  Above 300	₹7/unit
'''
units = float(input(" units: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = units * 3
elif units <= 300:
    bill = units * 5
else:
    bill = units * 7

print("Total Bill: ", bill)

'''5.Get a number from the user.
   Print its multiplication table from 1 to 20.'''
num = int(input('enter:'))
for i in range(1, 21):
    print(num, "x", i, "=", num * i)


#6.Get a number from the user and determine whether it is prime or not.
num = int(input("Enter a number: "))
factors = 0

for i in range(1, num + 1):
    if num % i == 0:
        factors += 1
if factors == 2:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")



'''7.Pattern program
* 
* * 
* * * 
* * * * 
* * * * *
'''
rows = 5

for i in range(1, rows + 1):
    print("* " * i)



'''
8.Pattern Program
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
'''
rows = 5

for i in range(1, rows + 1):
    spaces = "  " * (rows - i)
    stars = "* " * (2 * i - 1)
    print(spaces + stars)



'''
9.Pattern Program
1 
1 2 
1 2 3 
1 2 3 4 
'''
rows = 4

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


'''
9.Pattern Program
1 
1 2 
1 2 3 
1 2 3 4 
'''
rows = 4

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


#10. Check whether the given year is leap year or non leap year
year = int(input("Enter a year: "))

if year % 400 == 0:
    print(year, "is a leap year.")
elif year % 100 == 0:
    print(year, "is a non-leap year.")
elif year % 4 == 0:
    print(year, "is a leap year.")
else:
    print(year, "is a non-leap year.")





#11. Print the maximum and minimum of the given three numbers
# Input three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    maximum = a
elif b >= a and b >= c:
    maximum = b
else:
    maximum = c

if a <= b and a <= c:
    minimum = a
elif b <= a and b <= c:
    minimum = b
else:
    minimum = c

print("Maximum number is:", maximum)
print("Minimum number is:", minimum)

















