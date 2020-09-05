#set are unordered collections of unique elements
#los sets no pueden tener un mismo elemento repetido

myset = set()
print(myset)
myset.add(1)
print(myset)
myset.add(2)
print(myset)

#añade el 2 por segunda vez
myset.add(2)
print(myset)
#nota:no lo muestra por que un set nunca tendra un valor repetido





#su verdadera utilidad es en el uso de listas u otros
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3,3]
print(set(mylist)) #colecciones de elementos unicos