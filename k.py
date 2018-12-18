n = 5
m = n
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1:
            print('*', end='')
        else:
            print(' ', end='')
    n = n-1
    print()
p = 1
for m in range(n):
    for p in range(m):
        if j == 0 or j == m - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
