def sort_range(s):
    """write a function that takes in a string that's made of multiple ranges:
        - a single range element has the format of A:B, where A and B are numbers and A <= B always.
        - input string could contain multiple range elements which are not sorted
        - each element is separated by a comma, and there may be spaces between the commas.

        Return a sorted and compacted list of ranges separated by comma, and no spaces

        Examples:

            consecutive ranges
            >>> sort_range("5:14,  1:4,15:20")
            '1:20'

            overlapping ranges, non-consecutive
            >>> sort_range("1:9, 4:7, 13:14")
            '1:9,13:14'

            overlapping, consecutive
            >>> sort_range("2:6, 7:18,     1:3, 15:30")
            '1:30'
    """

    sorted_result = []
    # instantiate a new variable list to store result
    for i in s.split(','):
    # iterate over i in list created by splitting the string based on ','
        i = i.strip()
        # i (still a string) equal to i with no empty spaces 
        index = i.find(':')
        # look for index of ':' in each i

        new_start = int(i[:index])
        # slice each i, and set new_start equal to integer before ':'

        new_end = int(i[index+1:])
        # slice each i, and set new_end equal to integer after ':', and it's +1 
        # because slicing is inclusive of the start index, and we don't want to 
        # include ':'
        sort_lo = 0
        sort_hi = len(sorted_result)
        # which is also 0 for the first iteration

        # Binary insertion sort (does not hold true for first iteration)
        # sort_hi equals to 1 after first iteration, and while loop is executed:
        while sort_lo < sort_hi: #basically start at index[1]
        # while len(result) > 0 (always true after first iteration)
            mid = (sort_lo + sort_hi) / 2
            # find the mid point

            item_start, item_end = sorted_result[mid]
            # item_start, item_end equals to result element at index mid

            if item_start < new_start:
                sort_lo = mid + 1
            else:
                sort_hi = mid
        # add i to result list at index sort_lo, so after first iter, [(2,6)]
        sorted_result.insert(sort_lo, (new_start, new_end)) 




    # Compact List
    compacted_result = [sorted_result[0]]
    current_start, current_end = sorted_result[0]

    for (item_start, item_end) in sorted_result[1:]:

        if item_start - current_end > 1:
            compacted_result.append((item_start, item_end))
            current_start, current_end = item_start, item_end
        else:
            current_end = max(current_end, item_end)
            compacted_result[-1] = (current_start, current_end)

    return ",".join([str(i[0]) + ":" + str(i[1]) for i in compacted_result])
  
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED!"