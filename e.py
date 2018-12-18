n = int(input('enter your number:'))
for i in range(n):
    for j in range(n):
        if j == 0:
            print('*', end=' ')
    for k in range(int(n/2)):
        if i == 0:
            print('*', end=' ')
        elif i == int(n/2):
            print('*', end=' ')
        elif i == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

