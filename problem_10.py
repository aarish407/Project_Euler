# Question: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# Answer: 142913828922

sum= 0
for i in range(2, 2000001):
	flag= True
	for j in range(2, i//2):
		if i % j == 0:
			flag= False
			break
	if flag == True and i != 4:
		print(i)
		sum+= i

print(sum)	
