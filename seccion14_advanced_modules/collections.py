from collections import Counter
#counter se usa para decir cuantas veces estan repetidos ciertos numeros
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3]
print(Counter(mylist))
#counter con strings
mylist = ['a','a',10,10,10]
print(Counter(mylist))


print(Counter('aaaaaaaaaaaaaababagdfhherhb'))

sentence = "how many times does each word show up in this sentence with a word"
print(Counter(sentence.lower().split()))


letters = 'aaabbbcccccccdddddddddd'
c = Counter(letters)
print(c)
print(c.most_common(2))

#default dictionary ,se puede usar para añadir palabras claves al diccionario si antes no existian
from collections import defaultdict
d= defaultdict(lambda: 0)
d['correct'] = 100
print(d['correct'])
d['wrong key']
print(d)



mytuple = (10,20,30)
print(mytuple[0])


from collections import namedtuple

Dog = namedtuple('Dog', ['age', 'breed', 'name'])
print((Dog))
sammy = Dog(age = 5, breed='husky', name='sam')
print(type(sammy))
print(sammy)
print(sammy.age)
print(sammy.breed)
print(sammy.name)
print(sammy[0])
