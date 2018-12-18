n = 6
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1:
            print('*', end=' ')
        elif j == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    n = n-1


    print()

for k in range(6):
    print('*', end=' ')
