import random

def getWords(filename):
    with open(filename) as file:
        return tuple(line.strip() for line in file)

articles = getWords('articles.txt')
nouns = getWords('nouns.txt')
verbs = getWords('verbs.txt')
prepositions = getWords('prepositions.txt')

def sentence():
    return noun_phrase() + " " + verb_phrase()

def noun_phrase():
    return random.choice(articles) + " " + random.choice(nouns)

def verb_phrase():
    return random.choice(verbs) + " " + noun_phrase() + " " + prepositional_phrase()

def prepositional_phrase():
    return random.choice(prepositions) + " " + noun_phrase()

def main():
    num_sentences = int(input('Enter number of sentences: '))
    for i in range(num_sentences):
        print(sentence())

if __name__ == '__main__':
    main()
