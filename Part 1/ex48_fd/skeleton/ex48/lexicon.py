directions = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verbs = ('go', 'stop', 'kill', 'eat', 'open')
stop_words = ('the', 'in', 'of', 'from', 'at', 'it')
nouns = ('door', 'bear', 'princess', 'cabinet')

def lexicon_tuple(word):
    lowercase = word.lower()

    if lowercase in directions:
        return ('direction', lowercase)

    elif lowercase in verbs:
        return ('verb', lowercase)

    elif lowercase in stop_words:
        return ('stop', lowercase)

    elif lowercase in nouns:
        return ('noun', lowercase)

    elif lowercase.isdigit():
        return ('number', int(lowercase))

    else:
        return ('error', word)

def scan(sentence):
    words = sentence.split()
    return [lexicon_tuple(word) for word in words]
