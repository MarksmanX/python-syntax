def print_upper_words(words):
    """Print each word on sep line, uppercased."""

    for word in words:
        print(word.upper())

def print_upper_words2(words):
    """Print each word on sep line, uppercased, if starts with E or e."""

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words3(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of letters given"""
    for starter in must_start_with:
        for word in words:
            if word.startswith(starter):
                print(word.upper())
                break