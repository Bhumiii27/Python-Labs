# a. 
def reverse_string(s):
    return s[::-1]

# b. 
def is_palindrome(s):
    return s == s[::-1]

# c. 
def is_digits_only(s):
    return s.isdigit()

# d. 
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# e. 
def length_of_last_word(sentence):
    words = sentence.strip().split()
    return len(words[-1]) if words else 0


if _name_ == "_main_":
    text = input("Enter a string: ")
    sentence = input("Enter a sentence: ")

    # a
    print("\n(a) Reversed String:", reverse_string(text))

    # b
    print("(b) Is Palindrome?:", is_palindrome(text))

    # c
    print("(c) Contains Only Digits?:", is_digits_only(text))

    # d
    print("(d) Longest Word in Sentence:", longest_word(sentence))

    # e
    print("(e) Length of Last Word in Sentence:", length_of_last_word(sentence))
