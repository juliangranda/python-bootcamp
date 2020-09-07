
#lambda functions: son funciones anonimas de un SOLO uso

def square(num):
    return num**2
my_nums = [1,2,3,4,5]
for item in map(square, my_nums):
    print(item)

print(list(map(square,my_nums)))


def splicer(mystring):
    if len(mystring)%2==0:
        return 'EVEN'
    else: 
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']
print(list(map(splicer,names)))

def check_even(num):
    return num%2 == 0
mynums = [1,2,3,4,5,6]
print(list(filter(check_even,my_nums)))

for n in filter(check_even,mynums):
    print(n)

#lambda

#funcion normal
def square2(num):
    return num**2

print(square2(3))
#la convertirmos a lambda
lambda num:num**2

print(list(map(lambda num:num**2,mynums)))

#convertimos otra a lambda
print(list(filter(lambda num:num%2 == 0,mynums)))
