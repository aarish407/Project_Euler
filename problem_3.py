# Question: The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# Answer: 

def check_prime(num):
	for i in range(2,num//2):
		if num % i == 0:
			return 0
			break		

	return 1	

lpf= 1
for i in range(2, 600851475143//2):
	if 600851475143 % i == 0:
		status= check_prime(i)
		if status == 1:
				lpf= i

print(lpf)
																			