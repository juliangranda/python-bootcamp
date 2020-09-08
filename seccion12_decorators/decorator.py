#los decoradores permiten "decorar a una funcion"
#el decorator permite agregar rapidamente funcionalidad adicional a una funcion


#importante para recordar de las funciones
def hello1(name='Jose'):
    return 'Hello '+name
hello1()
greet = hello1
print(greet)
greet()

def hello(name='Jose'):
    print('The hello() function has been executed')
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    
    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")



hello()
#welcome()  #marca error

#como trabar con una funcion dentro de otra funcion
def hello2(name='Jose'):
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    
    if name == 'Jose':
        return greet
    else:
        return welcome

x = hello2()
print(x)
print(x())
my_new_func = hello('Jose')
print(my_new_func)


def cool():
    def super_cool():
        return 'i am very cool'
    return super_cool

some_func = cool()
print(some_func)
some_func()


#importante: pasar una funcion como argumento

def hello3():
    return 'Hi Jose!'

def other(func):
    print('Other code would go here')
    print(func())

other(hello3) #aqui la funcion hello3 se esta pasando como un argumento para la funcion other



#creacion de un decorador manualmente
def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")


func_needs_decorator()
# Reassign func_needs_decorator
func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()


#con decorador normal asignado por python

@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")


func_needs_decorator()