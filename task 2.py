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
