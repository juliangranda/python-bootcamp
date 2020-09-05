#los diccionarios son mapeos no ordenados para almacenar objetos
#dictionary sintax: {'key1':'value1, 'key2':'value2'}
#los diccionarios tienen la ventaja de llamar algo rapidamente usando las keys pero la desventaja que no pueden ser ordenados y son desordenados
#dictionaries: objects retrieved by key name, unordered and can not be sorted
#list: objects retrieved by location. ordered sequence can be indexed or sliced

my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict)
print(my_dict['key1'])

prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
print(prices_lookup['apple'])

#los diccionarios son muy flexibles permitiendo tener diversos datos en ellos incluso otras listas o diccionarios
d = {'k1':123, 'k2':[1,1,2], 'k3':{'insideKey':100 }}
print(d['k2'][2])
print(d['k3']['insideKey'])

d = {'key1':['a','b','c']}
print(d)
mylist = d['key1']
print(mylist)
letter = mylist[2]
print(letter)


#añadir nuevo valor a un diccionario
d = {'k1':100, 'k2':200}
print(d)
d['k3'] = 300
print(d)

#asiganar o modificar valor de un diccionario
d['k1']= 'NEW VALUE'
print(d)


#importante
#para ver todas las keys y valores
d = {'k1':100, 'k2':200, 'k3':300}
print(d.keys())
print(d.values())
print(d.items())