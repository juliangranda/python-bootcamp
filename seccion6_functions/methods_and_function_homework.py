'''
Write a function that computes the volume of a sphere given its radius.

The volume of a sphere is given as (4/3)*pi*r^3
'''
def vol(rad):
    pi=3.1416
    v = (4/3)*pi*(rad**3)
    return v

print(vol(2))

'''
Write a function that checks whether a number is in a given range (inclusive of high and low)
'''
def ran_check(num,low,high):
    if num in range(low,high+1):
        print(f'{num} is in the range between {low} and {high}')
    else:
        print('the number is outside the range')
    '''
    if low < num < high:
        return print(f'{num} is in the range between {low} and {high}')
    '''
ran_check(5,2,7)
#5 is in the range between 2 and 7

'''

Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33
HINT: Two string methods that might prove useful: .isupper() and .islower()

'''
def up_low(s):
    #lower = 0
    d= {"upper":0, "lower":0}
    for x in s:
        if x.islower():
            #lower += 1
            d["lower"]+=1
        elif x.isupper():
            d["upper"]+=1
        else:
            pass
    return d

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))

'''
Write a Python function that takes a list and returns a new list with unique elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
'''
def unique_list(lst):
    return set(lst)
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

'''
def unique_list(lst):
    # Also possible to use list(set())
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x
    '''





'''Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24
'''
def multiply(numbers):  
    mul=1
    for x in numbers:
        mul *= x
    return mul
print(multiply([1,2,3,-4]))


'''
Write a Python function that checks whether a word or phrase is palindrome or not.

Note: A palindrome is word, phrase, or sequence that reads the same backward as forward,
 e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace() 
 method in a string to help out with dealing with spaces. Also google search how to reverse a string in Python, 
 there are some clever ways to do it with slicing notation.
'''

def palindrome(s):
    s = s.replace(' ','') # remplace los espacios en blanco por NO spacios en blanco
    return s[::-1]

print(palindrome('helleh'))
print(palindrome('nurses run'))
print(palindrome('abcba'))