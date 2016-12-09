"""Given two strings, are they, at most, one edit away?

    >>> one_away("make", "make")
    True

    >>> one_away("make", "fake")
    True

    >>> one_away("task", "take")
    False

    >>> one_away("ask" ,"asks")
    True

    >>> one_away("asks", "ask")
    True

    >>> one_away("act", "tact")
    True

    >>> one_away("fat", "fact")
    True

    >>> one_away("yes", "no")
    False

    >>> one_away("happy", "happier")
    False

"""


def one_away(w1, w2):
    """Given two strings, are they, at most, one edit away?"""

    if abs(len(w1) - len(w2) > 1):
        return False

    # i = 0
    # w1_d = {}
    # w2_d = {}

    # for i in w1:
    #     w1_d[i] = w1.count(i)

    # for j in w2:
    #     w2_d[j] = w2.count(j)

    # unmatched = set(w1_d.items())^set(w2_d.items())
        
    # if len(unmatched) > 2:
    #     return False
    # return True
    
    if len(w2) > len(w1):
        w1, w2 = w2, w1

    # Keep track of number of wrong letters
    diff = 0

    # Loop over w1 with i and over w2 with j
    i = j = 0

    # while j < len(w2):

    #     if w1[i] != w2[j]:

    #         # We found a wrong letter
    #         wrong += 1
    #         # We'll move to the next char in the longer string.
    #         i += 1
    #         if wrong > 1:
    #             return False

    #         # If same length, move the next char in shorter.
    #         # Otherwise, don't move in shorter string --- this
    #         # will cover the case of a added letter.
    #         if len(w1) == len(w2):
    #             j += 1

    #     else:
    #         # Both letters match; move to next letter in both
    #         i += 1
    #         j += 1

    # return True

    # iterate over 1 word - shorter of the two, so there is no index out of range error
    # as i, j increments
    while j < len(w2):
        # if letter are different, add to diff variable
        if w1[i] != w2[j]:
            diff += 1
            # as soon as diff is more than 1, than it's fast fail
            if diff > 1:
                return False
            # two scenarios: if same length for both words, both go on check next 
            # word
            if len(w1) == len(w2):
                i += 1
                j += 1
                
            else: #if one word is longer than the other, go on to next letter in 
            # longer word, and see if it matches previous letter in shorter word
            # because this is a case where extra letter is added in the middle of long
            # word, but the rest should be the same as the shorter
                i += 1
        else:
            i += 1
            j += 1
    return True












if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; NICE JOB! ***\n"
