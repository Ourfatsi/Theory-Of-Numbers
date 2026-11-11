import time
import Eratosthenes

def couples(N):
    Primes = Eratosthenes.Eratosthenes(N)
    Couples =[]
    k=0

    while (k < len(Primes)):
        if (Primes[k]+2 in Primes):
            Couples.append([Primes[k],Primes[k]+2])
        k=k+1

    return(Couples)

#N=100000
N=1000000 #Consirable time for N=10^6, but it works.

# Main code to be timed

start = time.perf_counter()
List_of_Couples = couples(N)
end = time.perf_counter()

time1 = end - start

counter=0

start = time.perf_counter()
with open("Results/Couples.txt", "w") as f:
    f.write(f"Running time of listing the couples : {time1:.4f} seconds\n")
    f.write(f"Number of couples found : {len(List_of_Couples)}\n")

for c in List_of_Couples:
    with open("Results/Couples.txt", "a") as f:
        f.write(str(counter+1)+"-"+str(List_of_Couples[counter]))
        f.write("\n")
        counter=counter+1
end = time.perf_counter()
time2 = end - start

print(f"Running time for file writing : {time2:.4f} seconds")





