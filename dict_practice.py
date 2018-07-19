import pandas as pd
import matplotlib.pyplot as plt
import urllib.request

text = urllib.request.urlopen('https://raw.githubusercontent.com/kjergens/datasets/master/bttf.txt').read().decode()

print(text[:1000])


need_to = False

if need_to:
    #df = tdf.filter(['created_at', 'text', 'favorite_count', 'retweet_count', 'is_quote', 'is_retweet', 'hashtags', 'quoted_favorite_count', 'quoted_retweet_count', 'retweet_text'], axis=1)

    # set the date to the index
    df['created_at'] = pd.to_datetime(df['created_at'])
    df.index = df['created_at']
    del df['created_at']

    #text_out = df.to_csv('/Users/kjergens/Desktop/ttweets.csv')

    print(list(df))

    print(df['2018'])
    #df.groupby(level=0).plot()
    df['2018'].plot()
    #plt.show()
    # print(df['favorite_count', 'retweet_count'])

    #df[['favorite_count', 'retweet_count']].plot()
    #
    plt.close('all')

debug = False

if debug:
    # Save second half:
    text = text[-(round(len(text) / 2)):]

    with open('/Users/kjergens/Desktop/trump.txt', 'w') as fo:
        fo.write(text)
#else:
    # remove the punctuation
    text = text.replace(',', '').replace('.', '').replace('"', ',').replace(')', '').replace('(', '').replace(',', '') \
        .replace('?', '').replace(';', '').replace('!', '')

    # split into words
    tlist = text.split()

    # make lowercase (so upper and lower are not counted as different words)
    tlist = list(map(str.lower, tlist))

    # get unique set of words
    ulist = list(set(tlist))

    print("Total words:", len(tlist))
    print("Unique words:", len(ulist))

    word_counts = {}  # start with an empty dictionary

    print('Starting word counts....')
    for u in ulist:
        word_counts[u] = tlist.count(u)
    print('Finished!')

    answer = input("what word do you want to look up? (q to quit)")

    while answer != 'q':
        try:
            print(answer, 'appears', word_counts[answer], 'time(s)')
        except KeyError:
            print('Not found.')

        answer = input("what word do you want to look up? (q to quit)")
