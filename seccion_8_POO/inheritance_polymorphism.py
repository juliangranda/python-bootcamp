#herencia -> inheritance

class Animal():

    def __init__(self):
        print("animal create")

    def who_am_i(self):
        print("i am an animal")

    def eat(self):
        print("i am eating")

class Dog(Animal):
    
    def __init__(self):
        #instancia de la clase padre heredada
        Animal.__init__(self)
        print("dog created")

    def bark(self):
        print("woof")


my_dog = Dog()
#metodo heredado de la clase padre
my_dog.eat()
#metodo de la clase perro
my_dog.bark()



##############################################

#polimorfismo
#polimorfismo se refiere a la forma en que diferentes clases de objetos pueden compartir el mismo nombre de metodo




