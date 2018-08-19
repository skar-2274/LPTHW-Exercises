directions = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verbs = ('go', 'stop', 'kill', 'eat', 'open')
stop_words = ('the', 'in', 'of', 'from', 'at', 'it')
nouns = ('door', 'bear', 'princess', 'cabinet')

def lexicon_tuple(word):
    test_word = word.lower()

    if test_word in directions:
        return ('direction', test_word)

    elif test_word in verbs:
        return ('verb', test_word)

    elif test_word in stop_words:
        return ('stop', test_word)

    elif test_word in nouns:
        return ('noun', test_word)

    elif test_word.isdigit():
        return ('number', int(test_word))

    else:
        return ('stop', word)

def scan(sentence):
    words = sentence.split()
    return [lexicon_tuple(word) for word in words]
