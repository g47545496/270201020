def sum_values():
  a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
  b=0
  for i in a_list:
    b+=i
  print(b)
sum_values()


def binary_values(a):

  c=""
  while a>0:

   
   c+=str(a%2)
   a//=2
  
  return (c[::-1])
  
def binary_to_dec(b):
  d=0
  b_rev =str(b)[::-1]
  for i in range(len(b_rev)):
    d+=(2**i)*int(b_rev[i])
  return(d)
def main():
  b="111111"
  print(binary_to_dec(b))
  a=48
  print(binary_values(a))
main()

#Prime Numbers
def is_prime(n):
   if n<=1:
      return False
   for i in range(2,(n//2)+1):
      if n % i==0:
         return False
   return True

def print_primes_between(n,m):
  for i in range(n,m):
    if is_prime(i):
      print(i)
first=int(input("Enter the first number:"))
last=int(input("Enter the last number:"))
print_primes_between(first, last)
#List Overlap
import random
random.seed(1)
def get_rand_list(b,e,N):
  r_list=random.sample(range(b,e),N)
  return(r_list)
def get_overlap(L1,L2):
  L3=[]
  for num in L1:
    if num in L2:
      L3.append(num)
  return(L3)
def main():
  liste1=get_rand_list(0,10,5)
  liste2=get_rand_list(0,10,5)
  print(liste1)
  print(liste2)
  liste3=get_overlap(liste1,liste2)
  print(liste3)
main()