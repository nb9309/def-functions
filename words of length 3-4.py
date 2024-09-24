def findwords():
    lst1 = []
    lst = []
    while 9:
        val = input('enter word: ')
        if val == '!':
            break
        else:
            lst.append(val)
    d = {}
    for i in lst:
        d[i] = len(i)
    else:
        for w,wl in d.items():
            if wl == 3 or wl == 4:
                lst1.append(w)
    print('{} are words in length of 3,4'.format(lst1))

findwords()
