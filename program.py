def spin_words(sentence):
     words = [w[::-1] if len(w) >= 5 else w for w in sentence.split()]
     return ' '.join(words)
