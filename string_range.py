
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
    
    initial_lst = [i.strip() for i in s.split(",")] 
    #['4:5', '1:3'] O(n)
    tup_lst = [tuple(i.split(":"))for i in initial_lst]
    #[("4", "5"), ("1", "3")] O(n)
    clean_tup = [(int(i), int(j))for i, j in tup_lst]
    #[(4,5),(1,3)] O(n)
    clean_tup.sort()
    #[(1,3),(4,5)] O(n log n)

    working_range = [clean_tup[0]]
    current_st = clean_tup[0][0]
    current_en = clean_tup[0][1]

    for st, en in clean_tup[1:]: 
        if st - current_en > 1:
            working_range.append((st, en))
            current_st, current_en = st, en
        else:
            current_en = max(current_en, en)
            working_range[-1] = (current_st, current_en)    

    #[(1: 6), (9: 30)] O(n)
    result = [str(i) for i in working_range]
    #["(1: 6)", "(9: 30)"] O(n)
    semi_result = [i.replace(", ", ":").strip("()") for i in result]
    #["1:6", "9:30"] O(n)
    final_result = ",".join(semi_result) 
    # O(n)

    return final_result

   

###################################################################################################################################
# DOCTESTS

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED!"
    print