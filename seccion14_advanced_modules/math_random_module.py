import math
#help(math)
#rounding numbers
value = 4.35
print(math.floor(value))
print(math.ceil(value))
print(round(value))

#mathematical constants
from math import pi
print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.nan)


#Logarithmic Values
print(math.log(math.e))
#print(math.log(0))
print(math.log(10))
print(math.e ** 2.302585092994046)

#Custom Base
print(math.log(100,10))
print(10**2)

#Trigonometrics Functions
print(math.sin(10))

print(math.degrees(pi/2))
print(math.radians(180))




#random module

import random
print(random.randint(0,100))
print(random.randint(0,100))

print(random.randint(0,100))
random.seed(101)
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))

#random integers
print(random.randint(0,100))
mylist = list(range(0,20))
print(mylist)
print(random.choice(mylist))


#sample with replacement
print(random.choices(population=mylist,k=10))
print(random.sample(population=mylist,k=10))

print(random.shuffle(mylist))
print(mylist)


#random distributions
print(random.uniform(a=0,b=100))

#normal/guissian 
print(random.gauss(mu=0,sigma=1))









