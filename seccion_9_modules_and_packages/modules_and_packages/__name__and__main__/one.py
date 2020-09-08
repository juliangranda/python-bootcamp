#one.py

def func():
    print("FUNC() in ONE.py")

print("top LEVEL IN ONE.PY")

if __name__ == '__main__':
    print('one.py is being run directly')
else:
    print('one.py has been imported')