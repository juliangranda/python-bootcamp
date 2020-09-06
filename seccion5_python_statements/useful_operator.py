
#funcion rango
for num in range(10):
    print(num)

for num in range(3,10):
    print(num)

for num in range(0,11,2):
    print(num)

#listas con funcion rango
print(list(range(0,11,2)))


#function enumerate: esta funcion devuelve los valores en forma de TUPLAS y usamos desembalaje o desempaquetado de tuplas

word = 'abcde'
#tuplas
for items in enumerate(word):
    print(items)
#desempaquetado tuplas
for index, letters in enumerate(word):
    print(letters)
    print(index)
    print('\n')


#funcion zip: lo que hace es comprimir o juntar varias listas y al combinar ambos elementos devolvera TUPLAS

mylist1 = [1,2,3]
mylist2 = ['a','b','c']

    #a,b se puede usar desempaquetado
for items in zip(mylist1,mylist2):
    print(items)

print(list(zip(mylist1,mylist2)))

# uso de la palabra clave de for IN para comprobar cosas en listas, tuplas o diccionarios
#IN con listas
print((1 in [1,2,3]))
print(('x' in ['a','b','c']))
print(('a' in 'a world'))

#IN con diccionarios
print(('mykey' in {'mykey':345}))
d = {'mykey':345}
print((345 in d.values()))

#valores min and max
mylist = [10,20,30,40,80]
print(min(mylist))
print(max(mylist))

#importacion libreria aleatoria
from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)

#valor aleatorio basado en un rango
from random import randint
print(randint(0,100))

mynum = randint(0,100)
print(mynum)


#input function
result = input('enter a number here: ')
print(type(result))
print(result)

#importante
#convertir string a float o int
print(float(result))
print(int(result))

#uso adecuado
result = int(input('enter a number here: '))
print(type(result))