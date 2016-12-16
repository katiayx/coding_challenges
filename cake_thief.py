""" input: (weight, value) of cake, bag capacity
    output: max value

    write a function that takes a list of cake type
    tuples and a weight capacity, and returns the maximum
    monetary value the duffel bag can hold.

    example:
    cake_tuples = [(7, 160), (3, 90), (2, 15)]
    capacity    = 20

    function(cake_tuples, capacity)
    returns 555 (6 of the middle type of cake and 1 of the last type of cake)

    """

########################################
#Brute force, using weight/value ratio #
#it's a good solution, but doesn't work#
#for some edge cases                   #
########################################

def max_duffel_bag_value_ratio(cake_tuples, capacity):
    """
        >>> max_duffel_bag_value_ratio([(1, 30), (50, 200)], 100)
        3000

        >>> max_duffel_bag_value_ratio([(3, 40), (5, 70)], 9)
        120
        this is the failure because max_value should be 3 3lb cakes

        >>> max_duffel_bag_value_ratio([(3, 40), (5, 70)], 8)
        110

     """

    #track largest ratio:
    max_per_pound = 0
    #track max_per_pound tuple
    max_tup = ()
    #iterate through cake_tuples, and find largest value per pound
    for weight, value in cake_tuples:
        if value/weight > max_per_pound:
            max_per_pound = value/weight
            max_tup = (weight, value)
    #unpack max_tup
    optimal_weight = max_tup[0]
    optimal_value = max_tup[1]
    #calcuate max_value
    #if optimal_weight fits evenly into capacity
    if capacity % optimal_weight == 0:
        max_value = capacity / optimal_weight * optimal_value
    else:
        #if optimal_weight doesn't fit evenly into capacity
        remainder_weight = capacity % optimal_weight
        #go through cake_tuples to see whether other remainder_weight is divisible
        #by remaining tuple weights -- no need to worry about duplicating effort, because
        #remainder_weight will not divide evenly by optimal_weight, already checked above
        for weight, value in cake_tuples:
            #in case remainder weight can be evenly divided into one of other cakes
            if weight % remainder_weight == 0:
                remainder_value = remainder_weight / weight * value
                max_value = capacity / optimal_weight * optimal_value + remainder_value
            #another scenario where weight is less than remainder weight
            elif weight < remainder_weight:
                remainder_value = remainder_weight / weight * value
                max_value = capacity / optimal_weight * optimal_value + remainder_value


    return max_value

    #O(n) runtime


    def max_duffel_bag_value_bp(cake_tuples, capacity):
        """
            >>> max_duffel_bag_value_bp([(1, 30), (50, 200)], 100)
            3000

            >>> max_duffel_bag_value_bp([(3, 40), (5, 70)], 9)
            120

            >>> max_duffel_bag_value_bp([(3, 40), (5, 70)], 8)
            110
        """

        #similar to coin change problem, building a list where index is capacity,
        #and value is the max_value at that capacity. This list will track
        #capacity:max_value relationships.
        max_value_at_capacity = [0] * (capacity + 1)
        #iterate through each cake
        for cake_weight, cake_value in cake_tuples:
            #iterate through each capacity from 0 - input capacity
            for current_capacity in xrange(capacity + 1):
                #keep track of current max
                current_max_value = 0
                #only cake less than or equal to current_capacity can be used
                if cake_weight <= current_capacity:
                    #what value will we get using this cake? we already know
                    #max_value_at_capacity for all smaller capacity than current_capacity
                    max_value_using_cake = cake_weight + max_value_at_capacity[current_capacity - cake_weight]
                    #compare max_value_using_cake vs. current_max_value to get the higher value
                    current_max_value = max(current_max_value, max_value_using_cake)
            #update list value for current_capacity
            max_value_at_capacity[current_capacity] = current_max_value

        return max_value_at_capacity[capacity]









#####################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED."
    print
