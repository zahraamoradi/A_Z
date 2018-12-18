n = 7
for i in range(n):
    for j in range(n):
        if i == 0 or i == int(n/2) or i == n-1:
            print('*', end='')
        elif j == 0 and i <= int(n/2):
            print('*', end='')
        elif j == n-1 and i >= int(n/2):
            print('*', end='')
        else:
            print(' ', end='')
    print()


