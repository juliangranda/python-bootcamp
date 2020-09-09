
def func_one(n):
    '''
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    '''
    return [str(num) for num in range(n)]

print(func_one(10))

def func_two(n):
    '''
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    '''
    return list(map(str,range(n)))



print(func_two(10))

import time
# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = func_one(1000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time
print(end_time)



#Timeit Module

import timeit


setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
stmt = 'func_one(100)'
timeit.timeit(stmt,setup,number=100000)

setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''

stmt2 = 'func_two(100)'
timeit.timeit(stmt2,setup2,number=100000)


timeit.timeit(stmt,setup,number=1000000)

timeit.timeit(stmt,setup,number=1000000)