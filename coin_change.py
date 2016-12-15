"""give amount, and a list of denominations, write
    a function that computes the number of ways to
    make amount of money using coins in available denominations"""

# example:
# a = 15
# coins = [1,3,5]

# pseudo code:
# 1. create a list: [0,0,0,0...0] - index=amount, value=ways
# 2. iterate starting with first coin and first value - see how many ways can 1cent make up 1c,
# all the way up to how many ways can 1cent make up 15cents
# 3. then go to next coin, and reiterate through the values start at the value that's equal to or greater than
# coin
# 4. look for the difference between value and coin: look up value at [coin] from previous plus value at [difference],
# add them together to get new value for [coin]. if we are looking ways_1_3[15], we already know populated list for
# ways_1[5], and ways_1_3[up to 15]. The only way to add a new combination is if once new coin is used once, the remainder
# is divisible by the other denominations.

def ways_coin(a, coins):
    """write a function that outputs number of ways coins can be combined to make
    up the a

        >>> ways_coin(15,[2,6,9])
        2

        >>> ways_coin(50,[1,5,25])
        18

        >>> ways_coin(15,[1,3,5])
        13

    """

    ways = [0] * (a + 1) #creating value-ways list
    ways[0] = 1

    for coin in coins:
        for value in xrange(coin, a+1): #iterate through values, starting at coin value and go up to last value set by a
            extra = value - coin
            ways[value] = ways[value] + ways[extra]

    return ways[a]






#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED."
    print
