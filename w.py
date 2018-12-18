n = 8
m = n
for i in range(n):
    for j in range(m):
        if j == 0 or j == m-1:
            print('*', end='')
        else:
            print(' ', end='')
    m = m-1
    print()


