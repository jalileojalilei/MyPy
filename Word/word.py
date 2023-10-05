def count_word(text, word):
    return text.lower().split().count(word.lower())

def count_total_words(text):
    return len(text.split())

