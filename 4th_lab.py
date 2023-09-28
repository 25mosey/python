def count_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)
text = "Это текст с несколькими словами."
unique_word_count = count_unique_words(text)
print("Количество различных слов:", unique_word_count)