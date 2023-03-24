def recite(start_verse, end_verse):
    ttt = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    start = "On the "+ ttt[start_verse-1] +" day of Christmas my true love gave to me: "
    verse = [
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, "
    ]
    end = "and a Partridge in a Pear Tree."

    return start + "".join(verse[0:end_verse-1]) + end


def main():
    print(recite(4, 4))


if __name__ == "__main__":
    main()