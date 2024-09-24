def area():
    l,b = float(input('enter length: ')), float(input('enter breadh: '))
    a = l*b
    print('area of rectangle =',a)
area()

def perimeter(l,b):
    p = 2*(l+b)
    return p
l = float(input('enter length = '))
b = float(input('enter breadh: '))
z = perimeter(l,b)
print('perimeter of recangle is ',z)
