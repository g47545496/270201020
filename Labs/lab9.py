#Harmonic Sum
def harmonicsum(n):
  if n ==1:
    return 1
  else:
    return 1/n+harmonicsum(n-1)
print(harmonicsum(5))
#Reverse List
def get_reverse(n):
    if len(n)==0:
        return[]
    return [n.pop()]+get_reverse(n)
liste=[1,2,3,4,5]
print(get_reverse(liste))
#Get Number of Evens
def get_number_even_recursive(l,c=0):
   if len(l)==0:
     return c
   current=l.pop()
   if current%2==0:
     c += 1
   return get_number_even_recursive(l,c)
def get_number(l):
  return get_number_even_recursive(l,c=0)
a=[1,2,3,4,5,6]
print(get_number(a))

#Simple Timer
import time
def recursive_timer(n):
    if n == 0:
        print("the end")
        return None
    print(f"time remaining: {n}")
    time.sleep(1)
    return recursive_timer(n - 1)

recursive_timer(3)