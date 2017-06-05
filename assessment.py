"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    #initialize a dict
    counts_words_dict = {}
    #split the string by space into a list
    phrase_list = phrase.split(" ")
    #iterate over the list
    for word in phrase_list:
        #if word in list is not in the dict, add it as a key and set the value (here count) as 1
        if word not in counts_words_dict:
            counts_words_dict[word] = 1
        #else if word in list is in the dict, increment the value by 1
        else:
            counts_words_dict[word] += 1

    #return dict
    return counts_words_dict

#I have added an alternate solution for the count_words function below using sets.
#I thought the solution above was with lists was simpler as it did not need multiple for loops.

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    counts_words_dict = {}
    phrase_list = phrase.split(" ")
    phrase_set = set(phrase_list)
    for word in phrase_set:
        counts_words_dict[word] = 0
    for word in phrase_list:
        counts_words_dict[word] += 1

    return counts_words_dict


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    #create a dict with melon names as key and prices as the values
    lists_melons_dict = {
    "Watermelon": 2.95,
    "Cantaloupe": 2.50,
    "Musk": 3.25,
    "Christmas": 14.25,
    }

    #The .get() method takes in the key as the first argument and will return the value associated with a key
    #in this case price of the melon
    #if the melon name is not found in the dict, we can set the second argument in .get() as 'No price found'
    return lists_melons_dict.get(melon_name, "No price found")


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>>     
        [(2, ['ok']), (9, ['porcupine'])]
    """
    #initialize a dict 
    word_length_dict = {}
    #iterate over the list
    for word in words:
        #calculate the length of each word
        word_length = len(word)
        #if the word length does not exist as a key in dict, add it as a key and add the word as a the value in a list
        if word_length not in word_length_dict:
            word_length_dict[word_length] = [word]
            
        #else add the word to the existing list corresponding to the respective word length key
        else:
            word_length_dict[word_length] += [word]

    #loop over the keys in the dict to sort each the list associated with a key
    for key in word_length_dict:
        word_length_dict[key] = sorted(word_length_dict[key])

    
    
    #ordering the dictionary by word length
    #using .items() to get a list of tuples with keys and values
    return sorted(word_length_dict.items())

#I have added an alternate solution for the word_length_sorted function using sets below. 
#I preferred the solution above as I thought lists are simpler to use in this case.

def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>>     
        [(2, ['ok']), (9, ['porcupine'])]
    """    
    
    word_length_dict = {}
    word_length_set = set()

    for word in words:
        word_length_set.add(len(word))
    for num in word_length_set:
        word_length_dict[num] = []
    for word in words:
        word_length_dict[len(word)].append(word)
    for key in word_length_dict:
        word_length_dict[key] = sorted(word_length_dict[key])
    return sorted(word_length_dict.items())


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """


    #create a dict with the English words as key and the Pirate translations as values
    english_to_pirate_dict = {
    "sir": "matey",
    "hotel": "fleabag inn",
    "student": "swabbie",
    "man": "matey",
    "professor": "foul blaggart",
    "restaurant": "galley",
    "your": "yer",
    "excuse": "arr",
    "students": "swabbies",
    "are": "be",
    "restroom": "head",
    "my": "me",
    "is": "be",
    }

    #split phrase into a list
    phrase_list = phrase.split(" ")

    #initialize a list where traslated words can be added
    translations_list = []

    #iterate over the phrase 
    for word in phrase_list:
        #if word in phrase is in the dict as a key, add the value corresponding to the key to the translations_list
        if word in english_to_pirate_dict:
            translations_list.append(english_to_pirate_dict[word])
        #else add the word, unchanged to the dict
        else:
            translations_list.append(word)
    #return the list as a string 
    return " ".join(translations_list)
    #do not consider word with punctuation the same as the word itself


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    #initialize a results list
    results = []
    #separate the list provided into a dict with the first letter of each word as a key and the list of words starting with the letter as values
    names_dict = {}
    for name in names:
        if name[0] not in names_dict:
            names_dict[name[0]] = [name]
        else:
            names_dict[name[0]] += [name]
    #add the first word in the names list to the results list and remove it from the list of values in the dict
    #set the key as the last letter of the first word in the results list
    results.append(names[0])
    names_dict[names[0][0]].pop(0)
    key = results[0][-1]

    #looping over the list, check to see if the last index of each word in the list exists as a key in the dict and 
    #that the list of values associtaed with that key is not empty
    #if true, add the first value in the list associated with the key to the results list
    #rebind the key to the last letter of the new last word in the results list
    #the while loop stops when the last letter of the last word in the results list does not match any key in the dict
    #or if the key has an empty list associated with it
    while True:    
        if key in names_dict and names_dict[key] != []:
            results.append(names_dict[key].pop(0))
            key = results[-1][-1]
            
        else:
            break
    return results





#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
