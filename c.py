n = 10
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