def type_input(a):
    if type(a) == int:
        print('{} is int type'.format(a))
    elif type(a) == float:
        print('{} is float type'.format(a))
    elif type(a) == complex:
        print('{} is complex type'.format(a))
    elif type(a) == bool:
        print('{} is bool type'.format(a))
    elif type(a) == str:
        print('{} is string type'.format(a))
    elif type(a) == bytes:
        print('{} is bytes type'.format(a))
    elif type(a) == bytearray:
        print('{} is bytearray type'.format(a))
    elif type(a) == range:
        print('{} is range type'.format(a))
    elif type(a) == list:
        print('{} is list type'.format(a))
    elif type(a) == tuple:
        print('{} is tuple type'.format(a))
    elif type(a) == set:
        print('{} is set type'.format(a))
    elif type(a) == frozenset:
        print('{} is frozenset type'.format(a))
    elif type(a) == dict:
        print('{} is dict type'.format(a))
    else:
        print('{} is none type'.format(a))

i = 10
type_input(i)
f = 1.2
type_input(f)
c = 9+3j
type_input(c)
b = False
type_input(b)
s = 'python lanuage'
type_input(s)
by = bytes([10,20,30])
type_input(by)
ba = bytearray((1,4,2,5))
type_input(ba)
r = range(1,10,2)
type_input(r)
l = [1,2,3,4,5]
type_input(l)
t = (1,2,3,3,4,5)
type_input(t)
st = {1,2,3,4,4,5,6}
type_input(s)
fs = frozenset({1,2,3,4,5,6})
type_input(fs)
d = {2:'hii',1:'no'}
type_input(d)
n = None
type_input(n)