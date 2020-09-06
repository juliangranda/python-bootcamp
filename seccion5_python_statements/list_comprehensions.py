#list comprehension are a unique way of quickly creating a list with python
#if you find yourself using a for loop along with .append() to create a list, list comprehensions are a good alternative


#forma con ciclo for
mystring = 'hello'
mylist = []

for letter in mystring:
    mylist.append(letter)

print(mylist)



mylist = [letter for letter in mystring]
print(mylist)

mylist = [x for x in 'word']
print(mylist)

mylist = [x for x in range(0,11)]
print(mylist)

#operaciones en una list comprehension
mylist = [x**2 for x in range(0,11)]
print(mylist)

mylist = [x**2 for x in range(0,11) if x%2 == 0]
print(mylist)


#interesante su uso
celcius = [0, 10, 20, 34.5]

fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)
#lo mismo anterior pero normal
fahrenheit = []

for temp in celcius:
    fahrenheit.append(((9/5)*temp + 32))
print(fahrenheit)



#####################################
#no hacer esto

results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)

mylist = []
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)

print(mylist)
