def abbreviate(words):
    words = words.replace("-", " ").replace("_", " ")

    return ''.join([a[0].upper() for a in words.split()])
