n = 7
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1:
            print('*', end='')
        elif j == int(n/2):
            print('*', end='')
        else:
            print(' ', end='')
    print()


