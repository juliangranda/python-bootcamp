'''
try: this is the block of code to be attemped
except: block of code will execute in case there is an error in try block
finally: a final block of code to be executed, regardless of an error
'''

def add(num1,num2):
    print(num1+num2)

add(10,20)

number1= 10
number2= input("ingrese un numero. ")
#genera un error por que un es int y el otro string
#add(number1,number2)

try:#si el codigo esta bien

    #want to attemp this code
    #may have and error
    result = 10 + '10'

except: #si hay un error en el codigo

    print("hey it looks like you aren't adding corretly")
else:
    print("add went well")
    print(result)


try:
    f = open('testfile', 'r')#'w'
    f.write("write a test line")
except:
    print('all other exceptions')
finally:
    print("i always run")


def ask_for_int():
    while True:
        try: 
            int(input("please provide a number: "))
        except:
            print("whoops that is not a number")
            continue
        else:
            print("yes thank you")
            break
        finally:
            print("end of try/except/finally")

ask_for_int()

