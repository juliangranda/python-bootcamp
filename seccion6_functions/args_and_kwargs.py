# *args: nos permite tomar una cantidad arbitraria de argumentos devuelve una tupla
#lo que representa que es un args es el *

#kwargs: son argumentos claves que devuelven un diccionario

#argumentos posicionales
def myfunc(a,b):
    #returns 5% of the sum of a and b
    return sum((a,b)) * 0.05



print(myfunc(40,60))

#usando args : recordar retorna tuplas
def myfunc2(*args):
    #retorna una tupla
    return sum(args)*0.05

print(myfunc2(40,60,100,1))

#usando kwargs : recordar retorna diccionario

def myfunc3(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('i did not find any fruit here')

myfunc3(fruit='apple',veggie = 'lettuce')

#combinacion de ambos
def myfunc4(*args,**kwargs):
    print(args)
    print(kwargs)
    print('i would like {} {}'.format(args[0],kwargs['food']))

myfunc4(10,20,30,fruit='orange,',food='eggs',animal='dog')
