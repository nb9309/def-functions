def sita(a,b,c):
    if a <0 or b < 0 or c < 0:
        return 'invalid'
    SI = (a*b*c)/100
    total_amount = P+SI
    return SI,total_amount


P = float(input('principle amount: '))
T = float(input('given time: '))
R = float(input('Rate of intrest: '))
z  = sita(P,T,R)
if type(z) == str:
    print(z)
else:
    print('simple interst = {}, Total amount ={}'.format(z[0],z[1]))