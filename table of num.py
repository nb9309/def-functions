def table():
    num = int(input('enter value: '))
    for i in range(1,11):
        print('{} * {} = {}'.format(num,i,num*i))

table()
