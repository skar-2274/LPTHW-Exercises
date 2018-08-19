# Dict Style
mystuff = {'apple': "I AM APPLE!"}
print(mystuff['apple'])

# Module Style
import mystuff

mystuff.apple()
print(mystuff.tangerine)

# Class Style
class mystuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM A CLASSY APPLE!")

thing = mystuff()
thing.apple()
print(thing.tangerine)

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
