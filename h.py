n = 7
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1:
            print('*', end=' ')
        elif i == int(n/2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

