# Question: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# Answer: 906609

def palindrome(num):
	x= num
	prod=0
	while num > 0:
		d= num%10
		num//= 10
		prod= prod*10 + d

	if prod == x: 
		palindrome_array.append(prod)

def find_maximum():
	maximum= palindrome_array[0]
	for i in range(1, len(palindrome_array)):
		if palindrome_array[i] > maximum:
			maximum= palindrome_array[i]
	return maximum		

palindrome_array= []
for i in range(101,1000):
	for j in range(i,1000):	
		palindrome(i*j)
maximum= find_maximum()
print(maximum)