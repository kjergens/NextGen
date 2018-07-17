import re


def get_quotes_by(person, text):
    """
    Returns a list of quotes by a specified person.
    Searches for groups of words with quotes around them, followed by any words and/or spaces
    (this is for "said", "asked", "murmured") followed by person's name,
    followed by any words/spaces (this is for "quietly", "loudly", etc).
    :param person: a string
    :param text: a string, the full text to search
    :return: a list of strings
    """
    quotes = re.findall('“.*”[\s\w]*'+person+'[\s\w]*', text)  # Handle all kinds of quotes
    quotes.extend(re.findall('".*"[\s\w]*' + person + '[\s\w]*', text))
    quotes.extend(re.findall('‟.*”[\s\w]*' + person + '[\s\w]*', text))
    quotes.extend(re.findall("'.*'[\s\w]*" + person + "[\s\w]*", text))
    quotes.extend(re.findall("‘.*’[\s\w]*" + person + "[\s\w]*", text))

    # Remove when talking at, to or about person.
    for q in quotes:
        if 'at '+person in q or 'told '+person in q or 'to '+person in q or 'about '+person in q:
            quotes.remove(q)
    return quotes


# Read Harry Potter into a string variable
with open('/Users/kjergens/Desktop/harrypotter.txt') as file_in:
    text = file_in.read()

if __name__ == '__main__':
    harry_quotes = get_quotes_by('Harry', text)
    ron_quotes = get_quotes_by('Ron', text)
    hermione_quotes = get_quotes_by('Hermione', text)

    print("Harry speaks", len(harry_quotes), "times.")
    print("Ron speaks", len(ron_quotes), "times.")
    print("Hermione speaks", len(hermione_quotes), "times.")