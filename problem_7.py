# Question: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

# Answer: 104743

primes= []
i= 2
while True :
	flag= True
	for j in range(2, i//2):
		if i % j == 0:
			flag= False
			break
	if flag == True and i != 4:
		primes.append(i)
	i+= 1

	if len(primes) == 10001:
		break

print(primes[10000])	