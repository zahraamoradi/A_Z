# def f(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return f(n-1)+f(n-2)
# x=int(input('enter the number'))
# print(f(x))
n = int(input('enter your number:'))
print('*')
for i in range(-1, n):
    print('*' + ' ' * (i + 2) + '*')
for i in range(n, -1, -1):
    print('*' + ' ' * (i + 1) + '*')
print('*')
