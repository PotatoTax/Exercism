verses = [
    "a Partridge in a Pear Tree.",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming"
]

days = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth"
]


def verse(i):
    output = f"On the {days[i]} day of Christmas my true love gave to me: "
    for j in range(i, 0, -1):
        output += verses[j] + ", "

    if i > 0:
        output += "and "

    return output + verses[0]


def recite(start_verse, end_verse):
    return [verse(v-1) for v in range(start_verse, end_verse+1)]
