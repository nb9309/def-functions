def sorting(lst):
    print(lst)
    x = sorted(lst)
    y = sorted(lst,reverse=True)
    return x,y

lst = []
while 9:
    val = int(input('enter value: '))
    if val == 99:
        break
    lst.append(val)
x,y = sorting(lst)
print('assending list is {}'.format(x))
print('desending list is {}'.format(y))