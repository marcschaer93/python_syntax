# this should print "HELLO", "HEY", "YO", and "YES"
# def print_upper_words(words):
#     for word in words:
#         if word.startswith('h'):
#           print(word.upper())
    


# print_upper_words(['heLlo', 'heyy'])


def print_upper_words(words, must_start_with):
    """print each word to uppercased if the word starts with the given letters of the argument must_start_with"""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
    




print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})