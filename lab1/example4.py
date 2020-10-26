#Write a Python program that reads a month and day from the user. Your program should display the season associated with the date that was entered.​ 

a=int(input("day_number:"))
b=int(input("mounth_number:"))
if a>=20 and  3==b or 1<= a <=31 and 4<= b <=5 or a<=20 and b==6:
 print("Spring")
elif a>= 21 and 6==b or 1<= a  <= 31 and 7<= b <=8 or a<=21 and b==9:
  print("summer")
elif a>= 22 and 9==b or 1<= a  <= 31 and 10<= b <= 11 or a<=20 and b==12:
  print("Autumn")
else:
  print("winter")





#Write a Python code that asks the user for parameters(a, b, c) of a quadratic equation represented as: ax2 + bx + c. The code should calculate & print out the roots accordingly.​
#Discriminant:​
#When Δ>0, there are two real roots ​
#When Δ=0, there is one real root​
#When Δ<0, there are two complex roots ​
#Hint: Δ = b2 - 4ac​

a=int(input("number_1:"))
b=int(input("number_2:"))
c=int(input("number_3:"))

Delta=b**2-4*a*c 
if Delta > 0:
   x1=(-b+Delta**0.5)/2*a 
   x2=(-b-Delta**0.5)/2*a
   print("There are two real roots",x1,x2)
elif Delta==0:
   x1=(-b+Delta**0.5)/2*a
   print("there is one real root",x1)
elif Delta < 0:
  print("There are two complex roots")

  
  

import random 
x=("Ahmet","Ali","Ayşe","mehmet")
