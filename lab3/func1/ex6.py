def text_reversed(text):
    words = text.split()
    i = len(words) - 1
    while i >= 0:
        print(words[i], end=' ')
        i -= 1

text = input()
text_reversed(text)
