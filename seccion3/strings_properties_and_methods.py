name = "sam"
print(name)
#inmutabilidad : los strings en python no se pueden reasignar
#name[0] = "p"

#para reasignar un string tocaria hacer lo siguiente la concatenacion
last_letters = name[1:]
print(last_letters)
print("p" + last_letters)

#multiplicacion de cadenas
letter = "z"
print(letter)
letter = letter * 10
print(letter)

#propiedades y metodos
x = "Hello world"
print(x.upper())
print(x.lower())
#divide una cadena basado en un espacio en blanco o letra o simbolo
print(x.split())
x = "Hi this is a string"
print(x.split('i'))
