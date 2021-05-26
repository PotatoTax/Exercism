from collections import defaultdict


def count_words(sentence):
    sentence = sentence.lower()
    to_replace = ",!&@$^%:_."
    for i in to_replace:
        sentence = sentence.replace(i, " ")
    words = defaultdict(int)

    i = 0
    while i < len(sentence):
        if sentence[i] in "\t\n ":
            if i > 0:
                word = sentence[:i]
                word = word.strip("\'")
                words[word] += 1
            sentence = sentence[i+1:]
            i = 0
        else:
            i += 1

    if sentence:
        words[sentence.strip("\'")] += 1

    return {k: v for k, v in words.items()}
