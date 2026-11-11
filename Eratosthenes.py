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
			if i*j in L:
				L.remove(i*j)
			j=j+1
		i = L[0]

	return(L)


List1 = Eratosthenes(200)
List2 =[]

for p in List1:
	List2.append(p%3-1)

print(List1)
print(List2)

