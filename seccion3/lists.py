#es una lista de elementos sin importar su tipo
my_list = [1,2,3]
my_list = ['STRING',100,23.2]
print(len(my_list))

#sliding en listas
mylist = ['one', 'two', 'three']
print(mylist[0])
print(mylist[1:])

#concatenacion de listas
another_list = ['four', 'five']
new_list = mylist + another_list
print(new_list)

#las listas si se pueden modificar en comparacion a los strings o cadenas
new_list[0] = "ONE ALL CAPS"
print(new_list)

#agregar un elemento al final de la lista
new_list.append('six')
print(new_list)
new_list.append('seven')
print(new_list)

#elimina el ultimo elemento de la lista
new_list.pop()
print(new_list)
popped_item = new_list.pop()
print(popped_item)

#eliminar un elemento de la lista por el indice
new_list.pop(0)
print(new_list)


#metodo ordenar en listas
new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4,1,8,3]
new_list.sort()
print(new_list)
#nota: una lista ordenada no se puede asignar
my_sorted_list = new_list.sort()
print(type(my_sorted_list)) #esta diciendo que es nonetype, es decir, no devuelve nada
#nota:forma de hacer la asignacion de una lista ordenada
new_list.sort()
my_sorted_list = new_list
print(my_sorted_list)

num_list.sort()
print(num_list)


#metodo inverso para listas
num_list.reverse()
print(num_list)

#how do i index a nested list?
nested_list = [1,1,[1,2]]
print(nested_list[2])
print(nested_list[2][1])
