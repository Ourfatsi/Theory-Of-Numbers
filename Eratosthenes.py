def Eratosthenes(N):
	L=[]
	for k in range(2,N+1):
		L.append(k)

	print(L)
	counter = 0
	while (counter < len(L)):
		i = L[counter]
		j=i
		while (i*j <= N):
			if (i*j in L):
				L.remove(i*j)
			j=j+1
		counter = counter + 1
	return(L)


print(Eratosthenes(100))

