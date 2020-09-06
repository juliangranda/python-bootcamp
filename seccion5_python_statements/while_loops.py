x = 0

while x < 5:
    print(f'the current values of x is {x}')
    x += 1
else:
    print("x is not less than 5")


#importante
#break, continue, pass
#break: breaks out of the current closest enclosing loop
#continue: goes to the top of the closes enclosing loop
#pass: does nothing at all

x =[1,2,3]
for item in x:
    #comment pass se utiliza cuando por el momento no se quiere lidiar con un for
    #o tambien se usa simplemente para rellenar un ciclo y no ejecute error por que no lleva ningun codigo
    pass
print("end of my script")


mystring = 'sammy'
for letter in mystring:
    if letter == 'a':
        continue
    print(letter)

for letter in mystring:
    if letter == 'a':
        break
    print(letter)

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1