#las validaciones del input se estan haciendo para validar si el numero de entrada del input
#es un entero, no esta recibiendo cadenas como two,three u otros y si es un digito

def user_choice():
    choice = 'wrong'

    while choice.isdigit() == False:
        choice = input("please enter a number (0-10)")

        if choice.isdigit() == False:
            print("sorry is not a digit")
    return int(choice)


print(user_choice())


result = 'wrong value'
acceptable_values = [0,1,2]

print(result in acceptable_values)
print(result not in acceptable_values)


#validaciones para una input(*)
def user_choice2():
    #variables

    #initial
    choice = 'wrong'
    acceptable_range = range(0,10)
    within_range = False
    
    #two conditions to check
    #digit or within_range == false
    while choice.isdigit() == False or within_range == False:
        choice = input("please enter a number (0-10)")

        #digit check
        if choice.isdigit() == False:
            print("sorry is not a digit")
        
        #range check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("sorry out of acceptable range(0-10)")
                within_range = False
    return int(choice)

print(user_choice2())