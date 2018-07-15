# This program makes use of the Seive of Eratosthenes algorithm to find prime numbers, which is relatively more efficient than the traditional method.
# Answer: 142913828922
primes= []
sum= 0

for i in range(0,2000001):
	primes.append(i)
	sum+= primes[i]

primes[1]= 0

for i in range(2,1000000):
	if primes[i] == 0:
		continue

	for j in range(i+1,2000001):
		if primes[j]%primes[i] == 0:
			sum-= primes[j]
			primes[j]= 0

print(sum)			
