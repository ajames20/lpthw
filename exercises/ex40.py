class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics


    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
            print('_') * 10


happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there",])

bulls_on_parade = Song(["They rally around tha family",
                        "With pickets full of shells"])

used_to = Song(["Yeah, when you get to where I'm at",
                "You gotta remind 'em where the fuck you at",
                "Every time they talkin' it's behind your back",
                "Gotta learn to line 'em up and then attack",
                "They gon' say your name on them airwaves",
                "They gon' hit you up right after like it's only rap",
                "Jewels look like I found a motherfuckin' treasure map"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

used_to.sing_me_a_song()
