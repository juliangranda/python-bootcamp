#las tuplas son parecidas a las listas , la diferencia es que las tuplas tienen inmutabilidad , es decir, no se pueden modificar

t = (1,2,3)
mylist = [1,2,3]

print(type(t))
print(type(mylist))

#en tuplas tambien se usan strings
t =  ('one', 2)
print(t)
#tuplas pueden usar indexacion
print(t[0])
print(t[-1])

#cuando queremos contar cuantas veces esta algo en la tupla
t = ('a','a','b')
print(t.count('a'))

#devuelve el indice de la primeza vez que se encuentra el valor asignado a la funcion
print(t.index('a'))
print(t.index('b'))