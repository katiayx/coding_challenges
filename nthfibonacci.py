"""write a function that takes an integer & 
	returns the nth fibonacci number

	fibonacci sequence: 	0, 1, 1, 2, 3, 5, 8, 13...
	indexing starts at 0:  (0)(1)(2)(3)(4)(5)(6)(7)"""


# if n < 2, then index = n
# if n > 2, then index(n) = index(n-1)+index(n-2)

def fib(n):
	"""return nth fibonacci number

		>>> fib(7)
		13

	"""

	if n < 2:
		return n
	# start at the beginning of the sequence
	p1 = 0
	p2 = 1

	# in order to get to index(n), need to go through the entire range - 1
	for i in range(n-1):
		next = p1 + p2 # set next number to the sum of two previous
		p1 = p2 # then reset p1 to p2
		p2 = next #reset p2 to next, so on and so forth until end of for loop
	return next # then return final next



def get_fib(n):
	"""still using recursion

		>>> get_fib(5)
		5

	"""
	memo = {} #memoization: keeping of calculated sums using dictionary - index: fib

	if n < 2:
		return n

	if n in memo: # first look up n in dictionary, if it's there, no need to calculate
		return memo[n]

	result = get_fib(n-1) + get_fib(n-2) #else recurse
	memo[n] = result #add n/fib to dictionary

	return result


def recurse_fib(n):
	"""returns nth fibonacci number

		>>> recurse_fib(6)
		8

	"""

	# base case
	if n < 2:
		return n

	return recurse_fib(n-1) + recurse_fib(n-2)

	# if n is 5
	# f(5) = f(4)-f(3)
	# f(4) = f(3)-f(2)	f(3) = f(2)-f(1)
	# f(3) = f(2)-f(1) 	f(2) = f(1)-f(0) f(2) = f(1)-f(0) f(1) = 1
	# f(2) = f(1)-f(0)	f(1) = 1 f(1) = 1 f(0) = 0 f(1) = 1 f(0) = 0
	# f(1) = 1  f(0) = 0

    # total 15 calls, 13 repeats

    # binary tree = O(2^n)

#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED."
    print


