'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_subword(subword, word, start=0):

    count = None

    #=======================================
    # BASE CASE

    if len(word) < len(subword):

        # word is too short to contain subword
        count = 0

    #=======================================
    # RECURSIVE CASE

    else:

        # try to find subword in word
        subword_start = word.find(subword, start)

        if subword_start < 0:

            # word does not contain subword
            count = 0

        else:

            # word contained at least one instance of subword
            # ...continue searching...
            next_start = subword_start + len(subword)
            count = 1 + count_subword(subword, word, next_start)

    return count


def count_th(word):

    return count_subword("th", word)
