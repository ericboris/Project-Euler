import math
import emath
import timeit


def problem_1(n, m, end):
	## Return the sum of the arithmetic progression of n to end and m to end.
	## c removes the LCM of n and m from the total as it has been counted twice.
	arithmetic_progression = emath.arithmetic_progression
	a = arithmetic_progression(n, end)
	b = arithmetic_progression(m, end)
	c = arithmetic_progression(n*m, end)
	return int(a + b - c)
	## 34.572 micro-seconds/pass for end = 1000.


def problem_2(n):
	## Return the sum even numbers in the fibonacci sequence to n.
	## i increments by 3 because in the sequence every third number is even.
	fibonacci = emath.fibonacci
	sumTotal = 0
	i = 0
	while fibonacci(i) < n:
		sumTotal += fibonacci(i)
		i += 3
	return sumTotal
	## 378.050 micro-seconds/pass for n = 4000000.


def problem_3(number):
	## Return the largest prime factor of a number.
	prime_factorization = emath.prime_factorization
	return (prime_factorization(number)[-1])
	## 201.912 micro-seconds/pass for number = 72.


def problem_4(n):
	## Return largest palindrome number from product of 2 numbers both <= n.
	palindrome_product = emath.palindrome_product
	return palindrome_product(n)
	## Runtime < 0.14 seconds for n = 100.


def problem_5(n): ## Breaks for n > 996.
	## Return product total of list(lcm) from n to 1.
	return emath.product_of_list(emath.filter_lcm(n))
	## 4715.513 micro-seconds/pass for n = 20.


def problem_6(n):
	## Return difference of square of sums - sum of squares of n.
	return (emath.summation(n) ** 2) - emath.sum_of_squares(n)
	## 13.627 micro-seconds/pass for n = 100.



def problem_7(n):
	primes = [2]
	num = 3
	while len(primes) < n:
		for i in range(2, int(num**0.5) + 1):
			if num % i == 0:
				num += 2
				break
		else:
			primes.append(num)
			num += 2
	return (primes[n - 1])

    
def problem_8(n, v):
	place = 0
	biggest = None
	while place+v <= len(n):
		mult = None
		for i in n[place:place+v]:
			if mult == None:
				mult = int(i)
			else:
				mult *= int(i)
		if biggest == None:
			biggest = mult
		elif biggest < mult:
			biggest = mult
		else:
			place += 1
	return (biggest)


def problem_9(n):
	for x in range(1, n+1):
		y = x + 1
		z = y + 1
		while z <= n:
			while z * z < x * x + y * y:
				z += 1
			if z * z == x * x + y * y and x + y + z == n:
				print(x, y, z, x * y * z)
			y += 1


def problem_10(n):
	#Identical to problem_7 save for 2 changes.
	primes = 2   #Change to int from list.
	num = 3
	while num < n:
		for i in range(2, int(num ** 0.5) + 1):
			if num % i == 0:
				num += 2
				break
		else:
			primes += num   #Increments rather than append.
			num += 2
	return primes


def problem_11(grid):
	total = 0
	for a in range(17):
		for w in range(17):
			hori = grid[w][a] * grid[w][a + 1] * grid[w][a + 2] * grid[w][a + 3]
			vert = grid[w][a] * grid[w + 1][a] * grid[w + 2][a] * grid[w + 3][a]
			rdia = grid[w][a] * grid[w + 1][a + 1] * grid[w + 2][a + 2] * grid[w + 3][a + 3]
			ldia = grid[w][a + 3] * grid[w + 1][a + 2] * grid[w + 2][a + 1] * grid[w + 3][a]
			if total < hori or vert or rdia or ldia:
				if hori > total and vert and rdia and ldia:
					total = hori
				if vert > total and hori and rdia and ldia:
					total = vert
				if rdia > total and hori and vert and ldia:
					total = rdia
				if ldia > total and hori and vert and rdia:
					total = ldia
	return total

    
def problem_12(n):
	a = 1
	while True:
		b = a * (a + 1) / 2
		c = 0
		for i in range(1, int(b ** 0.5) + 1):
			if b % i == 0:
				c += 1
		if c*2 >= n:
			print(a, b, c*2)
			return
		else:
			a += 1


def problem_13(n):
	return sum(n)


def problem_14(n): #Needs optimization.
	final = [0, 0]
	for i in range(2, n):
		k = i
		count = 0
		while True:
			if i % 2 == 0:
				i /= 2
				count += 1
				if i < k:
					break
			else:
				i = (3 * i) + 1
				count += 1
		if final[1] < count:
			final = [k, count]
	return final


def problem_15(n):
	return (math.factorial(n * 2) / (math.factorial(n) * math.factorial(n)))


def problem_16(n, v):
	num = str(n ** v)
	total = 0
	for i in num:
		total += int(i)
	return total


def problem_17(n):
## Does not work yet.
	adict = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
			7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven',12:'twelve',
			13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen',
			17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 21:'twentyone',
			30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy',
			80:'eighty', 90:'ninety', 100:'hundred', 111:'and'}
	count = 0
	for i in range(1, n+1):
		if i > 0 & i < 20:
			count += len(adict[i])
			print(adict[i], count)
		if i > 20:
			a = int(i / 10) * 10
			b = i % 10
			count += a & b
			print(a, b, count)


def problem_20(n):
	mult = None
	for i in range(n, 0, -1):
		if mult == None:
			mult = i
		else:
			mult *= i
	total = str(mult)
	final = 0
	for i in total:
		final += int(i)
	return final


def problem_25(n):
	count = 0
	a, b = 0, 1
	while len(str(a)) != n:
		count += 1
		a, b = b, a + b
	return count


t = timeit.Timer('problem_6(100)', 'from __main__ import problem_6')
elapsed = (10 * t.timeit(number = 1000000))
print('function takes %0.3f micro-seconds/pass' % elapsed)

print(problem_6(100))
