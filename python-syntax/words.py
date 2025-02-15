def print_upper_words(words, must_start_with):
    """
    Prints each word in uppercase, but only if it starts with one of the specified letters.
    
    :param words: List of words to process.
    :param must_start_with: Set of letters the words must start with.
    """
    for word in words:
        if word[0].lower() in must_start_with:
            print(word.upper())

# Example usage
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
