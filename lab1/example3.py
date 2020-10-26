#Write a Python code that asks the user for a number, calculate the absolute value of the number and print it.​

#(without using abs function)​
x=int(input("please take a number :"))
x=x*5+63
print(x)
#Write a Python code that asks the user for three numbers, calculate the minimum of them and print it.
a=int(input("number 1: "))
b=int(input("nnumber 2: "))
c=int(input("number3: "))

if a<=6:
  print("HOME")
elif a+b*c>=60:
    print(b)

else:
  print(c)
#Write a Python code to ask user to enter two values: one for GPA and the other for Number of Lectures. According to the below table, decide whether user will be graduated or not. If not, give an appropriate message as given table.​

a=float(input("gpa:"))
b=int(input("number_of_lectures:"))
if a<2.0 and b < 47:
 print("Not enough number of lectures and GPA")
elif a>=2.0 and b<47:
 print("Not enough number of lectures")
elif a<2.0 and b>=47:
 print("Not enough Gpa")
else:
  print("GRUATED")
# Write a Python program that asks user for age and calculates ticket price accordingly:​
#Normal bus ticket price is 3 TL.​
#Bus ticket price for people younger than 6 and older than 60 years old is free.​
#People whose age are between 6 and 18 take 50% discount.​ 
age=int(input("Number1:"))
if age<6 or age>60:
  bus_ticket=0
  print(bus_ticket)
elif  18>age>=6:
  bus_ticket=3*0.5+3
  print(bus_ticket)
else:
  bus_ticket=3
  print(bus_ticket)







