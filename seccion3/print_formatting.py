#formatting with the .format() method

#'string here{} then also {}'.format('something1','something2')

print('this is a string {}'.format('INSERTED'))

#asignacion en base al orden de las palabras
print('the {} {} {} '.format('fox', 'brown', 'quick'))

#asignacion en base a el indice de las palabras
print('the {2} {1} {0} '.format('fox', 'brown', 'quick'))
print('the {0} {0} {0} '.format('fox', 'brown', 'quick'))

#asignacion en base a palabras clave o key
print('the {q} {b} {f} '.format(f='fox', b='brown', q='quick'))



#cambiar el nivel de precision
#float formatting follow "{value:width.precision f}"

result = 100/777
print(result)
print("the result was {r:1.3f}".format(r=result))
print("the result was {r:1.5f}".format(r=result))


#f-strings format
name = "jose"
print(f'hello , his name is {name}')
#nota: usa la "f" antes del comentario y usa directamente la variable


name = "same"
age = 3
print(f'{name} is {age} years old')