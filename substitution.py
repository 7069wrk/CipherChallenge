import string

alphabet = string.ascii_lowercase
alphabet = [letter for letter in alphabet]

file = open('message.txt','r')
message = str(file.read()).lower()


def n_gram_analysis(n, message):
    ngrams = []
    listmessage = []
    for letter in message:
        if letter in alphabet:
            listmessage.append(letter)
    for l in range(0, len(listmessage) - (n - 1)):
        ngram = []
        for i in range(0, n):
            ngram.append(listmessage[l + i])
        ngram = ''.join(ngram)
        ngrams.append(ngram)
    return(ngrams)


def frequency_analysis(message):
    frequencies = [0] * 26
    for letter in message:
        if letter in alphabet:
            frequencies[alphabet.index(letter)] += 1
    return(frequencies)


def display_frequency_analysis(message):
    frequencies = frequency_analysis(message)
    combos = zip(frequencies, alphabet)
    combos = sorted(combos,key=lambda x: x[0])[::-1]
    for combo in combos:
        combo = combo[::-1]
        combo = list(combo)
        combo[1] = str(combo[1])
        combo = ' '.join(combo)
        print(combo)


def english_rating(message): # Above 400 is possibly English
    trigrams = n_gram_analysis(3, message)
    commontrigrams = ['the', 'and', 'tha', 'ent', 'ing', 'ion', 'tio', 'for', 'nde', 'has', 'nce', 'edt', 'tis', 'oft', 'sth', 'men']
    rating = 0
    for trigram in trigrams:
        if trigram in commontrigrams:
            rating += 1
    return((rating * 10000) / len(message))


def solve_ceasar(message):
    frequencies = frequency_analysis(message)
    ciphers = []
    for i in range(0, 26):
        cipher = ''
        for letter in message:
            if letter in alphabet:
                newindex = (alphabet.index(letter) + i)
                if newindex > 25:
                    newindex -= 26
                cipher += alphabet[newindex]
            else:
                cipher += letter
        ciphers.append(cipher)
    for cipher in ciphers:
        if english_rating(cipher) > 400:
            print(cipher)


def manual_solve_substitution(message):
    taken = []
    used = []
    display_frequency_analysis(frequency_analysis(message))
    print(message)

    while True:
        choice1 = raw_input('Letter to replace (COMMAND): ') #Change
        choice2 = raw_input('Letter to replace with: ') #Change
        message = message.replace(str(choice1), str(choice2))

        if str(choice1) == str(choice1).lower() and len(str(choice1)) == 1:
            taken.append(str(choice1))
        if str(choice2) == str(choice2).upper() and len(str(choice2)) == 1:
            used.append(str(choice2))
        if str(choice1) == str(choice1).upper() and str(choice1) in used:
            used.remove(str(choice1))
        if str(choice2) == str(choice2).lower() and str(choice2) in taken:
            taken.remove(str(choice2))

        if str(choice1).upper() == 'SPACES':
            print('\n')
            print(message.replace(' ', ''))
        elif str(choice1).upper() == 'LETTERS':
            print('\n')
            print(message.translate(string.maketrans(string.lowercase, '*'*26)))
        elif str(choice1).upper() == 'BOTH':
            print('\n')
            print(message.translate(string.maketrans(string.lowercase, '*'*26))).replace(' ', '')

        else:
            print('\n')
            display_frequency_analysis(frequency_analysis(message))
            print('\n')
            print(''.join(taken))
            print(''.join(used))
            print('\n')
            print(message)


#display_frequency_analysis(message)
#solve_ceasar(message)
#manual_solve_substitution(message)
