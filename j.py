n = 7
for i in range(n):
    for j in range(n):
        if i == 0:
            print('*', end='')
        elif j == int(n/2):
            print('*', end='')
        elif i > int(n/2) and j == 0:
            print('*', end='')
        elif i == n-1 and j < int(n/2):
            print('*', end='')
        else:
            print(' ', end='')
    print()


