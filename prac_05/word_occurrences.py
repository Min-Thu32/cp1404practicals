"""Word Occurrences
Estimate: 19 minutes
Actual: 30 minutes
"""

word_count = {}
user_input = input("Text: ")
words = user_input.split()

for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

longest_word_length = max(len(word) for word in word_count.keys())

for word, count in sorted(word_count.items()):
    print(f"{word:{longest_word_length}} : {count}")
