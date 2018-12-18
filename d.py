n = 5
print('*')
for i in range(-1, n):
    print('*' + ' ' * (i + 2) + '*')
for i in range(n, -1, -1):
    print('*' + ' ' * (i + 1) + '*')
print('*')
