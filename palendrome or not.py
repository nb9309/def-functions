def palendrome(num):
    if num <= 0:
        print('{} is invalid'.format(num))
    else:
        tv = num
        revnum = 0
        while num>0:
            d = num%10
            revnum = revnum*10+d
            num = num//10

    if tv == revnum:
        return '{} is palendrome'.format(tv)
    else:
        return '{} is not a palendrome'.format(tv)



value = int(input('enter value: '))
res = palendrome(value)
print(res)