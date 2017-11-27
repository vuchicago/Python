# -*- coding: utf-8 -*-
##CHANGING DIRECTORIES
import os
os.chdir(path)
os.chdir("/Users/vu/Documents/Courses/Python Class")




This is a temporary script file.
def fh_2_celcius(t): 
    return (t-32)/1.6
    
def fn(x,y,z=None,flag=False):
    if flag:
        print("Flag is True")
    else:
        print("Flag is not flying")
    if (z==None):
        return x+y+2
    else:
        return x+y+z
  
        
firstname='Christopher Hansen Arthur Brooks'.split(' ')[0]        
 ***********************************************;       
 x={"Vu":"Vu.n.1989@gmail.com","Khoa":"11nguyenk@gmail.com"}

  for name in x:
    print(x[name])
    
  for name, email in x.items():
    print(name)
    print(email)
    
sales_record={'price':3.24, 'num_items':4,'person':'chris'} 
sales_hist='{} bought {} of cheese for a total of {}'
print(sales_hist.format(sales_record['person'],
sales_record['num_items'],
sales_record['price']*sales_record['num_items']))   

*******************************************************;
import csv

%precision 2

with open('mpg.csv') as csvfile:
   mpg=list(csv.DictReader(csvfile))

len(mpg)

*****
ctympgbycyl=[]

for i in cylinders:
   cycltypecount=0
   ctympgbycyl=0
   overall=0
   for d in mpg:
      if d['cyl']==i:
         overall+=float(d['cty'])
         cycltypecount += 1
   ctympgbycyl.append((i,overall/cycltypecount))
   ctympgbycyl.sort(key=lambda x: x[0])
   
   ctympgbycyl   
 **************************************************************  
import datetime as dt
import time as tm
tm.time()
dtnow=dt.datetime.fromtimestamp(tm.time())
dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second
delta=dt.timedelta(days=100)
today=dt.date.today()


 **************************************************************  
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 
'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']
   
     #option 1
for person in people:
    print(person.split()[0]+ ' ' + person.split()[-1])

   
    #option 2
    
def firstandlastname(person):
    firstname=person.split()[1]
    lastname=person.split()[2]
    #return(firstname+" "+lastname)
    return '{} {}'.format(firstname,lastname)
list(map(firstandlastname,people))

*************lambda functions********

option 1: Using lambda functions
for person in people:
   print((lambda x: x.split()[0] + ' ' + x.split()[-1])(person))
    
option 1: Using lambda functions
list(map(lambda x:x.split()[0]+" " + x.split()[-1],people))

 ########### List comprehension##########
my_list=[]
for number in range(0,1000):
    if number % 2==0:
        my_list.append(number)
 
#List comprehensions are a condensed way to do process above that offers readability and
#faster run-time  
       
my_list=[number for number in range(0,1000) if number %2==0]

       
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst
    
    equivalent to list comprehension expression:
[number*i for number in range(10) for i in range(10)]   

mylist=[]
for i in lowercase:
   for j in lowercase:
       for a in digits:
           for b in digits:
               mylist.append(i+j+a+b)
               
             equivalent to
               
mylist=[i+j+a+b for i in lowercase for j in lowercase for a in digits for b in digits]

##############     
import pandas as pd
import numpy as np
mylist=[1,2,3]


x=np.array(mylist)
y=np.array([4,5,6])
m=np.array([[7,8,9],[10,11,12]])


mylist.shape - mylist.shape will output shape of array/matrix
mylist.mymin
mylist.mean
mylist.std
mylist.argmax
mylist.argmin
mylist.max

n=np.arange(0,30,2) #output an array from 0-30 by increments of 2
p=np.linspace(0,4,9) #Creates 9 equidistant digits from 0 to 4
p.resize(3,3) #changes shape of data
o=p.reshape(3,3) #resizes the data but only for that calculation
z=np.array([y,y**2])
np.ones(3,2) #creates a 3x2 array of 1's
np.zeros(3,2) #creates a 3x2 array of 0's
np.eye(3) #creates an identity matrix of 3x3
np.diag(y) #gets the diagonal values of y
np.repeat(p,3) #repeats array p 3 times
p=np.ones([2,3],int) #creates a 2x3 array of integers of ones
np.vstack([p,2*p]) #vertical stacks an array p with 2*p
np.hstack([p,2*p]) #horizontal stacks an array p with 2*p
s=np.arange(13)**2 #Creates consecutive array from 0 to 12
s[-5::-2] #start off at 5th from highest and go backwards by two elements each
r=np.arange(36)
r.resize((6,6))
r[3,3:6]
r[:2,:-1] #First two rows and up to but not including last column
r[r>30] #Finds all element that's >30
r[r>30]=30 # changes all elements >30 to equal 30
r[:]=0 # change all the elements =0 in array r
r.copy() #will need change r since if you create x=r and change x, then r will also change
#x=r.copy() instead of x=r

x+y
x*y
x**2
x.dot(y)
z.T
z.dtype
z.z.astype('f')
n[2::3] #starts at the 3rd element, and pulls in the next 3

test=np.random.randint(0,10,(4,3)) #create a 4x3 array of random integers between 0-9
for row in test:
    print(row)
    
for i in range(len(test)):
    print(test[i])

#enumerate option
for i, row in enumerate(test):
    print('row',i,'is',row)

#This will print out each row of the array and its corresponding row number.  
#Not the same with dataframe


