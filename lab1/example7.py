##You’re given a tuple of name and age for everyone in a group. Printout the names of people who are older than 18.
a=[("jon",15), ("Ned",45), ("Arya",9), ("Catelyn",44), ("Bran",10)]
for name, age in a:
  if age>18:
    print(name)
#Construct a dictionary “book_dict”:○ The keys should be book names,○ The value of each element should be a tuple that contains two elements: the number of characters in the corresponding book name, and the number of unique characters in that name.○ For example, if the key is"ULYSSES", its value is (7,5).

books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}
a=[]
c=[]
for i in books:
  d=len(i)
  a=list(set(i))
  b=len(a)
  f=(d+b)/2
  book_dict[i]=(d,b,f)
  
print(book_dict)

#Employees● Assume that there is a company with 5 employees. ● Take each employee’s name and salary from the user, and store them in a dictionary “employees”. ● Print the names of the employees with the highest three salaries.

dic={"O":5,"A":7,"s":8,"d":9,"f":10}
dic_2={}
liste=[]
for i in dic.values():
  liste.append(i)
liste.sort()
print(liste)
for key,value in dic.items():
  dic_2[value]=key
  print(dic_2)
for i in liste[2:5]:
  print(dic_2[i])
#Check a Password● Write a Python program that determines and prints whether a password is valid or not.● A valid password is at least 8 characters long and contains at least one uppercase letter (A-Z), at least one lowercase letter (a-z), and at least one number (0-9). 
l=0
u=0
p=0
d=0
s =input("Enter the password:")
if (len(s) >= 8): 
    for i in s: 
  
         
        if (i.islower()): 
            l+=1            
  
         
        if (i.isupper()): 
            u+=1            
  
       
        if (i.isdigit()): 
            d+=1            
  
         
        if(i=='@'or i=='$' or i=='_'): 
            p+=1           
if (l>=1 and u>=1  and d>=1 and l+p+u+d==len(s)): 
    print("Valid Password") 
else: 
    print("Invalid Password")
 