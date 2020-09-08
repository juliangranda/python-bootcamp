class dog():
    #constructor o instancia de la clase
    #self representa la instancia de la clase
    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog  = dog(breed = 'lab', name = 'julian', spots = 'no spots')
print(my_dog)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)