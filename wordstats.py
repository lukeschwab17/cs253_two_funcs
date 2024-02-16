def average_length(user_string):
    words = user_string.split()
    if words:  # Ensure the string is not empty
        avg = sum(len(word) for word in words) / len(words)
    else:
        avg = 0
    return avg

def total_word_count(user_string):
    words = user_string.split()
    return len(words)

def total_char_count(user_string):
    return len(user_string)

def total_vowels(user_string):
    VOWELS = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in user_string:
        if char.lower() in VOWELS:
            count += 1
    return count;