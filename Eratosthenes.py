def is_inside(x,L):
	flag = False
	k=0
	while(not(flag) and k<len(L)):
		if x==L[k]:
			flag=True
		k=k+1
	return(flag)

def Eratosthenes(N):
	L=[]
	for k in range(2,N+1):
		L.append(k)

	i = L[0]
	while(i**2<N+1):
		L.remove(i)
		L.remove(i**2)
		j = i+1
		while(i*j < N+1):
			if is_inside(i*j,L):
				L.remove(i*j)
			j=j+1
		i = L[0]

	return(L)