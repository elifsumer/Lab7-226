from string_package import (
    reverse_string,
    capitalize_words,
    remove_punctuation,
    count_characters,
    count_words,
    average_word_length
)

def main():
    sentence = input("Please enter a sentence: ")

    print("\n--- Processed Results ---")
    print("Reverse:", reverse_string(sentence))
    print("Initials uppercase:", capitalize_words(sentence))

    cleaned = remove_punctuation(sentence)
    print("Cleaned up punctuation marks:", cleaned)
    print("The number of character:", count_characters(cleaned))
    print("The number of word:", count_words(cleaned))
    print("Average word count:", average_word_length(cleaned))

if __name__ == "__main__":
    main()
