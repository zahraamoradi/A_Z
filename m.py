n = 0
j = 0
for i in range(7):
    print('*', end='')
    for j in range(i):
        print(' ', end='')
    print('*', end='')
    for n in range(j, 11-j):
        print(' ', end='')
    print('*', end='')
    for m in range(0, 11-n):
        print(' ', end='')
    print('*', end='')
    print()












