# p = input('enter your text:')
# n = 10
# s=n
# if p == 'a':
#     for i in range(0, n):
#         for j in range(s-1, 0, -1):
#         	print(' ' , end='')
#         for k in range(i):

# 	        if k == 0 or k == i-1:
# 	            print(' *', end='')
# 	        elif i == n/2+1: 
# 	            print(' *' , end='')    
# 	        else:
# 	    	    print('  ', end='')
#         s = s-1
#         print()

n = int(input('enter your number'))
s = n
q = []
for i in range(n, 0, -1):
	if i >= int(s/2+1):
		a = ' ' * n + '*'
		print(a)
		q.append(a)
		b = int(n/5)
		n = n - b
for i in range(len(q)-1, -1, -1):
	print(q[i])