# Question: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Answer: 31875000

for a in range(1, 333):       
	for b in range(a+1, 666):
		for c in range(b+1, 999):
			if a+b+c == 1000 and c*c == a*a + b*b:
				product= a*b*c
				print(product)
				break

# Since it is given that a < b < c, in order to get the summation equal to 1000, the maximum value of a such that this condition is satisfied is 332. Similarly, b can have a value of 333 and c a value of 335. 			