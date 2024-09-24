def add():
    a = float(input('enter 1st value: '))
    b = float(input('enter 2nd value: '))
    c = a+b
    return a,b,c

a,b,c = add()
print('sum of {} and {} is {}'.format(a,b,c))

