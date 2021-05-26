def distance(strand_a, strand_b):
    len_a = len(strand_a)
    len_b = len(strand_b)
    if len_a > len_b:
        raise ValueError(".+")
    if len_a < len_b:
        raise ValueError("+.")

    return sum([a != b for a, b in zip(strand_a, strand_b)])
