row1 = [' ',' ',' ']
row2 = [' ',' ','-']
row3 = [' ',' ',' ']

def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

display(row1,row2,row3)


#accepting user input
result = input('please enter a value: ')
print(type(result))
print(result)

result = input('enter a value: ')
result_int = int(result)
print(type(result_int))
print(result_int)



position_index = int(input("choose an index position: "))
print(type(position_index))
print(row2[position_index])