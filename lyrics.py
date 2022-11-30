# instantiating a class. these are like containers for functions and data
class song(object):
    # the self is creating an instance which reduces amiguity
    # this function constructs the object
    def __init__(self, lyrics):
        self.lyrics = lyrics

    # this function controls the actions
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

push_it_lyrics = ['I saw the gap again today while you were begging me to stay take care not to make me enter If I do, we both may disappear']

schism_lyrics = ['The poetry that comes from The squaring off between And the circling is worth it Finding beauty in the dissonance']

# push_it = song (['I saw the gap again today',
#                 'While you were begging me to stay',
#                 'Take care not to make me enter',
#                 'If I do, we both may disappear'])

# schism = song (['The poetry that comes from',
#                 'The squaring off between',
#                 'And the circling is worth it',
#                 'Finding beauty in the dissonance'])

# this is a variable the stores the functionality of the song class and the lyrics
push_it = song(push_it_lyrics)

schism = song(schism_lyrics)

# this calls the variable push_it, which stores the functionality and lyrics
# and then invokes the function 
push_it.sing_me_a_song()

schism.sing_me_a_song()