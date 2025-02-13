def anagrams_of(string):
    # Base case: if the string has only one character,
    # return a list containing just that single-character string.
    if len(string) == 1:
        return [string]
    
    # Create a list to hold all the anagrams.
    collection = []
    
    # Find all anagrams of the substring from the second character until the end.
    substring_anagrams = anagrams_of(string[1:])
    
    # Iterate over each substring anagram.
    for substring_anagram in substring_anagrams:
        # Iterate over each index of the substring, from 0 until one index past the end of the string.
        for index in range(len(substring_anagram) + 1):
            # Create a copy of the substring anagram and insert the first character.
            copy = substring_anagram[:index] + string[0] + substring_anagram[index:]
            
            # Add the new anagram to our collection.
            collection.append(copy)
    
    return collection

# This algorithm is O(n!) because it has to generate all possible permutations of the string.

# For example, if the string is "abc", the algorithm will generate all possible permutations of "abc", which are "abc", "acb", "bac", "bca", "cab", and "cba".
# The number of permutations is n! (n factorial), which is 3! = 3 * 2 * 1 = 6.  

# O(N!) is one of the slowest categories of Big O.
