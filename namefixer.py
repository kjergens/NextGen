def fix_title(title):
    """
    Return a fixed version of the given title
    :param title: a string
    :return: a string
    """
    new_title = ''
    words = title.split()

    # For each word, make capital or lower
    for i in range(len(words)):
        if i == 0 or \
                words[i].lower() not in ('in', 'a', 'an', 'the', 'of', 'and'):
            new_title += words[i].capitalize()
        else:
            new_title += words[i].lower()
        new_title += ' '
    return new_title.strip()  # get rid of trailing space


titles = ["a tale of tWo cities", "about A boy", "wind in the willows", "gone With The wind", "the LAST eMperOR"]

for t in titles:
    print(fix_title(t))

