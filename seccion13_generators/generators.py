#generator function allow us to write a function that can send back a value and then later resume to pick up where it left off

#idea basica nos permite generar una secuencia de valores a lo largo del tiempo en lugar de tener que crear un secuencia y mantenerla en la memoria

#palabra clave importante en esta clase es "yield"

def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result   

print(create_cubes(10))


#ahora usando generators
def create_cubes_generator(n):
    
    for x in range(n):
        yield x**3
    
print(create_cubes_generator(10))
for x in create_cubes_generator(10):
    print(x)


#fibonnaci

def genfibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for num in genfibon(10):
    print(num)



def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()
#uso de funcion next con generators
print(next(g))
print(next(g))


s = 'hello'
for letter in s:
    print(letter)

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))