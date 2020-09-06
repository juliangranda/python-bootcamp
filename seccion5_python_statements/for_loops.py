mylist = [1,2,3,4,5,6,7,8,9,10]

#basic loop
for num in mylist:
    print(num)

#numeros pares o impares
for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f'odd number: {num}')

#
list_sum = 0

for num in mylist:
    list_sum = list_sum + num

print(list_sum)

for letters in "hello":
    print(letters)
#omite la variable por un _ debido a que no se va a usar la variable haciendolo mas legible
for _ in "hello":
    print("cool")

#tuplas tienen un trato especial en loops
tup = (1, 2, 3)
for item in tup:
    print(item)


mylist = [(1,2),(3,4),(5,6),(7,8)]
print(len(mylist))
#acceso tuplas
for item in mylist:
    print(item)

#desempaquetado de tuplas
for a,b in mylist:
    print(a)
    #print(b)

mylist = [(1,2,3),(5,6,7),(8,9,10)]
for a,b,c in mylist:
    print(b)


#loops en diccionarios
d = {'k1':'1', 'k2':2, 'k3':3}

for key,value in d.items(): #d.values(), d.keys()
    print(key)
    print(value)