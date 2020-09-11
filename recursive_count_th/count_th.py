"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""


def count_th(word):
    th = 0
    x = word.find('th')

    if x > -1:
        th += 1
        th += count_th(word[x+2:])

    return th
