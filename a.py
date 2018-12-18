n = 10
s = n
for i in range(0, n):
    for j in range(s-1, 0, -1):
        print(' ', end='')
    for k in range(i):
        if k == 0 or k == i-1:
            print(' *', end='')
        elif i == n/2+1:
            print(' *', end='')
        else:
            print('  ', end='')
    s = s-1
    print()
