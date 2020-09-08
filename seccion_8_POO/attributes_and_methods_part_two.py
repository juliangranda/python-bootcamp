class dog():

    #class atributes
    species = 'mammals'

    #constructor o instancia de la clase
    #self representa la instancia de la clase
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
        
    #methods ----> operations/actions
    def bark(self,number):
        print("woof! my name is {}, my number is {}".format(self.name,number))

my_dog  = dog(breed = 'lab', name = 'julian')
print(my_dog.species)
print(my_dog.breed)
print(my_dog.name)
my_dog.bark(10)


class Circle:
    #class attribute
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius * radius *self.pi
    def circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(5)
print(my_circle.radius)
print(my_circle.circumference())
print(my_circle.radius)
print(my_circle.area)