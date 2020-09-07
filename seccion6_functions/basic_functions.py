def say_hello():
    print("hello")

say_hello()


def say_hello2(name):
    print(f'hello {name}')

say_hello2('jose')

def add_num(num1, num2):
    print(num1+num2)
    return num1+num2

result = add_num(10,20)
print(result)


def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

print(lesser_of_two_evens(2,4))