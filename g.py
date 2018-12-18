n = 9
for i in range(n):
    for j in range(n):
        if j == 0:
            print('*', end=' ')
        if j < int(n / 2) and i == int(n / 2):
            print(' ', end=' ')
        if j > int(n / 2) and i == int(n / 2):
            print('*', end=' ')
        if i > int(n/2) and i != n-1:
            print(' ', end='')
        if i > int(n/2) and j == n-1 and i != n-1:
            print('     *', end='')
    for k in range(int(n/2)):
        if i == 0:
            print('*', end=' ')
    for m in range(n-1):
        if i == n-1:
            print('*', end=' ')
    print()
