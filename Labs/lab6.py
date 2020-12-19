#LABB5 SOLUTİON
##Multiplication Table  Write a Python program that takes an integer from user and displays the multiplication table for it. 
x=int(input("Enter the values:"))
for i in range(1,11):
  i*=x
  print(str(x),"x",str(i),"=",i)
##% of evens  Write a Python program that takes N integers from user and displays % of even ones. Hint: Take N from user at the beginning and use it to create a loop.  
number=int(input('How many numbers:'))
num_even=0
for i in range (1,number+1):
 num_=int(input('How many numbers:'))
 if num_%2==0:
   num_even+=1
print((num_even/number)*100)
##Matching Digits Write a Python program that asks the user for two positive integers and finds the number of matching digits (starting from units digit).


n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
t1 = min(n1,n2)
t2 = max(n1,n2)
counter = 0
while(t1 > 0):
    h1 = t1%10
    h2 = t2%10
    
    if(h1 == h2):
        counter +=1
    t1 = t1 //10
    t2 = t2 //10
print(counter)

#Password CheckerWrite a Python program that asks the user for a password as soon as he/she enters the right password.Display “Wrong” when password and input don’t match. Display the first letter of the password when input is “help”. Display “Welcome” and exit when input and password match.Hint: Define a static password “abc123” at the beginning.
x=input("Enter the Password:")
password="abc147"
while x!=password:
  x=input("don’t you remember the password? You must write Help.:")
  if x=="Help":
   print(password[0])
   x=input("TRY AGAİN:")
if x==password:
  print("Welcome the Your website")
##FibonacciWrite a Python program that asks the user how many Fibonacci numbers to generate and then displays them. Hints: ● The Fibonacci sequence is a sequence of numbers where any number is the sum of the previous two numbers. ● The sequence looks like this:1, 1, 2, 3, 5, 8, 13, 21 
adet = int(input("How many fibonacci numbers do you want to see: "))
sayac = 0
a = 1
b = 0
liste = []
while (adet > sayac):
    a = a + b
    a,b=b,a
    liste.append(b)
    sayac += 1
print(liste)