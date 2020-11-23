#Sum of the last two digits  Write a Python program that asks the user for an integer and prints the sum of the last two digits of the number. Note: If it is a single-digit number, assume it has 0 at the beginning, e.g. 07 for 7.
x=input("Enter the Numbers:")
result=0
if len(x)>=2:
  result =+int(x[-1]) + int(x[-2])
  print(result)
else:
  print("0")
#Leap year
#Write a Python program that asks the user for a year and then it checks whether the entered year is a leap year or not. Note: Leap years are "exactly divisible" by 4 but century years which are not divisible by 400 arenot leap years. Examples:100, 1900, 2017 → not leap years 4, 400, 1992, 2000 → leap years
result=0
years=int(input("Enter the Years:"))
if years <= 99 and years%4==0:
  print("This is Leap year")
elif years >= 100 and years%400==0:
  print("This is Leap year")
else:
  print("This is not leap year")
#Sum of list
#Write a Python program which calculates sum of the elements of a given list.
nums = [8, 60, 43, 55, 25, 134, 1]
x=0
for i in nums:
  x += i
print(x)
#Power
#Write a Python program that asks the user for two integers a and b and calculates ab without using ** operator and pow function.
x=int(input("Enter the n1:"))
y=int(input("Enter the n2:"))
z=1
for i in range(y):
  z*=x
print(z)
##Write a Python program which calculates n factorial where n is given by the user. n! = n * (n-1) * … * 1
x=int(input("Enter the Fac number:"))
a=1
for i in range(x):
  a*=i+1
print(a)
## Second way
x=int(input("Enter the Fac number:"))
a=1
for i in range(1,x+1):
  a*=i
print(a)

x=input("Enter the tree values:")

x1 , x2 , x3=x.split(',')
x1=int(x1)
x2=int(x2)
x3=int(x3)
print(x3)
dic1= {"Osman":15,"Ahmet":18,"Kerem":17}

print(dic1)