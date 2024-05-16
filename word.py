# Question 1 
# To change a word to uppercase you can use upper()

def print_upper_words(words, must_start_with=None):
    """Print each word in uppercase on a separate line.

    If must_start_with is provided, only words that start with
    one of the letters in must_start_with are printed.
    """
    for word in words:
        if must_start_with is None or any(word.startswith(letter) for letter in must_start_with):
            print(word.upper())

# Test with given example
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})