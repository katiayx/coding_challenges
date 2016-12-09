"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""
    

    #getting the numbers of times a letter appears in a word into a dictionary
    letter_counts = {} 
    for letter in word: 
        letter_counts[letter] = letter_counts.get(letter, 0) + 1 

    #grabbing only dictionary values = letter appearance
    letter_v = letter_counts.values() 
    #sort these values and binding to a new variable
    l_v = sorted(letter_v)
    #set odd_counter, because it's possible for a non-anagram-of-palindrome to have more than 1 
    #letter that appear only once, e.g. "arceaceb" -- r and b both appear only once
    odd_count = 0
    #loop through each value in list
    for c in l_v:
        #if value is not divisible by 2, meaning count value is odd
        if c % 2 != 0:
            #increment odd_counter by 1
            odd_count += 1
    #if odd count is greater than 1
    if odd_count > 1:
        #the word is not an anagram of a palindrome
        return False
    else:
        #otherwise, it is
        return True        
        




if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
