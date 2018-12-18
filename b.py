n = int(input('enter your number:'))
print('*')
for i in range(-1, n):
    print('*' + ' ' * (i + 2) + '*')
for i in range(n, -1, -1):
    print('*' + ' ' * (i + 1) + '*')
print('*')
n += 4
for i in range(0, n):
    print('*' + ' ' * (i + 2) + '*')
    if i == n-1:
        print('*' + ' ' * (i + 2) + '*')
        pass
for i in range(n, -1, -1):
    print('*' + ' ' * (i + 1) + '*')
print('*')



