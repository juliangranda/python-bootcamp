print("hello")
print('hello')
#es un enter o escriba lo siguiente en otra linea
print("hello \nworld")
#es un tab entre las palabras
print("hello \t world")

#funcion de longitud
print("la longitud de la palabra es: ",len("hello"))


#indexacion
mystring = "Hello world"
print(mystring)

print(mystring[0])
print(mystring[9])
print(mystring[-2])
print(mystring[-1])


#slicing
#subseccion de una cadena
mystring = 'abcdefghijk'

#empieza en el indice 2 y muestra hasta el final
print(mystring[2:])

#muestra desde el comienzo hasta el indice 3 pero no muestra el indice 3
print(mystring[:3])

#muestra una subseccion , empieza en indice 3 y se detiene en indice 6 para mostrar "def"
print(mystring[3:6])

# lo anterior pero con 3 parametros que es el numero de pasos
print(mystring[::2])
print(mystring[::3])
print(mystring[2:7:2])

#invertir string
print(mystring[::-1])

#importante teoria de lo anterior
#[start:stop:step]
#start is a numerical index for the slice start
#stop is the index you will go up to(but not include)
#step is the size of the jump you take



def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))