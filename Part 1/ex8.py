formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False,False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Now this is a story all about how",
    "my life got flipped turned upside down",
    "and I'd like to take a minute, just sitting right there",
    "I'll tell you how I became the prince of a town called Bel-Air"
))
