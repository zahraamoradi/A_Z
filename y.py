n = 5
for i in range(n+1, 2, -1):
    for j in range(n-i+2):
        print(' ', end='')
    for k in range(i-2):
        if k == 0 or k == i-3:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
for i in range(n):
    for j in range(n):
        if j == n-1:
            print('*', end='')
        else:
            print(' ', end='')





    print()


