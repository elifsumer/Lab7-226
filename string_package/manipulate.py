def reverse_string(s):
    return s[::-1]


def capitalize_words(s):
    return s.title()


def remove_punctuation(s):
    import string
    return ''.join(char for char in s if char not in string.punctuation)


if __name__ == "__main__":
    print(reverse_string("hello!"))
    print(capitalize_words("hello world"))
    print(remove_punctuation("hello, world!"))
