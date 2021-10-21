
def PatternCount(Text, Pattern):
    """Count all the (possibly overlapping) substrings in a string.
    The Python built-in "count" function is not suitable, because it does
    not count overlapping substrings.

    Args:
        Text (str): The string
        Pattern (str): The substring to count 

    Raises:
        ValueError: Pattern string must be less than or equal to the length of the string

    Returns:
        int: The number of occurrences of Pattern in Text
    """

    tlen = len(Text)
    plen = len(Pattern)

    if plen > tlen:
        raise ValueError("Pattern length must not exceed text length")

    count = 0

    # Naive search: loop over the text string and check each slice of the array for the pattern
    for i in range(tlen-plen+1):
        slice = Text[i:(i+plen)]

        # string comparison
        if slice == Pattern:
            count = count + 1

    return count 
    

def FrequencyMap(Text, k):

    """Returns a frequency map of a string. 
    A frequency map associates substrings of a string to its number of occurrences in the string.

    Args:
        Text (str): A string whose frequency map will be generated
        k ([int]): The length of k-mer to search for

    Returns:
        [dict]: A set of key, value pairs where 
        the keys are the set of unique substrings of length k in Text, 
        and the values are the number of times this substring occurs in the Text.
    """

    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0

    for pattern in freq.keys():
        freq[pattern] = PatternCount(Text, pattern)
    return freq

def FrequentWords(Text, k):
    """Return the most frequently-occurring word(s) of length k in a string

    Args:
        Text (str): The text to search
        k (int): The length of words to search for

    Returns:
        [list(str)]: The most frequently occurring words. 
        The length of this list will either be 1 in the case of a unique most frequent word,
        or more than 1 in the case of multiple words that occur with the same frequency.
    """
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        # add each key to words whose corresponding frequency value is equal to m
        if freq[key] == m:
            words.append(key)
    return words


def validNucleotide(Pattern):

    full_nucleotide_set = {'A','C','G','T'}
    pattern_dictionary = set(Pattern.upper())

    if pattern_dictionary.issubset(full_nucleotide_set):
        return True 
    else:
        return False 

def Reverse(Pattern):
    return Pattern[::-1]

def Complement(Pattern):
    """Computes a complementary nucleotide.
    Nucleotides A and T are complements of each other,
    as are C and G. 

    Args:
        Pattern (str): A nucleotide string

    Raises:
        ValueError: The nucleotide string is invalid (is not composed of {A,C,G,T})

    Returns:
        [str]: The complementary nucleotide
    """
    Pattern = Pattern.upper()
    if not validNucleotide(Pattern):
        raise ValueError("Pattern is not a valid nucleotide string. A nucleotide string may only contain {A,C,G,T}")

    comp_table = {"A":"T","T":"A","C":"G","G":"C"}
    complement = ""
    for i in range(len(Pattern)):
        complement = complement + comp_table[Pattern[i]]
    return complement

def ReverseComplement(Pattern):
    """Compute the reverse complement of a nucleotide string

    Args:
        Pattern (str): A nucleotide string with the following alphabet: {A,C,G,T}

    Returns:
        str: The reverse complement of the string
    """

    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern

