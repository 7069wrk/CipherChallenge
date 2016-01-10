import string
import itertools

alphabet = string.ascii_lowercase
alphabet = [letter for letter in alphabet]

file1 = open('message.txt','r')
message = str(file1.read()).lower()

def standarddeck():
    return([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54])

bigrams1 = ['th', 'he', 'in', 'an', 'er', 'nd', 'to', 'ed', 're', 'ou', 'ng',
            'at', 'ea', 'st', 'es', 'hi', 'nt', 'ha', 'on', 'it', 'en', 'as']

bigrams2 = ['et', 'le', 'll', 'or', 'al', 'dt', 'ar', 'se', 'te', 'sa', 'is',
            'ti', 've', 'ra', 'tt', 'of', 'wa', 'el', 'ad', 'me', 'ta', 'ro',
            'sh', 'ow', 'so', 'ne', 'ly', 'da', 'ot', 'ri', 'li', 'ho', 'em',
            'ew', 'de', 'ee', 'yo', 'do', 'no', 'ts', 'om', 'wh', 'im', 'oo',
            'ut', 'si', 'rt', 'lo', 'ai', 'la', 'ss', 'be', 'di', 'ur', 'rs',
            'gh', 'ma', 'ds', 'wi', 'id', 'co', 'ch', 'mo', 'us', 'ce', 'ge']

bigrams3 = ['fo', 'oa', 'we', 'na', 'ol', 'ec', 'ni', 'il', 'un', 'eh', 'ei',
            'eo', 'ic', 'ga', 'dh', 'ul', 'ke', 'ht', 'tr', 'ft', 'ac', 'tl',
            'ry', 'ca', 'ey', 'ld', 'pe', 'ef', 'go', 'tw', 'pa', 'ir', 'ns',
            'eb', 'ay', 'ep', 'os', 'ie', 'ev', 'ya', 'fa', 'fi', 'ab', 'wo',
            'yt', 'am', 'ig', 'nc', 'mi', 'dw', 'pl', 'su', 'rd', 'up', 'ba',
            'sp', 'bo', 'ck', 'sw', 'po', 'gt', 'eg', 'ys', 'od', 'dr', 'ug',
            'ag', 'fr', 'fe', 'ap', 'bl', 'io', 'gr', 'bu', 'gi', 'dg', 'tu',
            'ki', 'av', 'lt', 'dd', 'db', 'ok', 'ls', 'gs', 'dl', 'iv', 'pr',
            'nh', 'op', 'rn', 'ty', 'oi', 'sl', 'pi', 'fu', 'lf', 'sc', 'rr',
            'wn', 'yw', 'if', 'qu', 'ff', 'aw', 'yi', 'pp', 'rm', 'uc', 'df',
            'rh', 'mp', 'sm', 'dn', 'ak', 'ov', 'oh', 'sf', 'rw', 'ny', 'tc',
            'mu', 'sn', 'cr', 'ob', 'ms', 'by', 'dc', 'af', 'ye', 'ct', 'rl',
            'yh', 'sb', 'ru', 'ui', 'du', 'tb', 'tf', 'br', 'rc', 'nl', 'gl',
            'nk', 'mt', 'oc', 'kn', 'vi', 'my', 'cl', 'tm', 'yb', 'dy', 'nw',
            'hr', 'um', 'ue', 'dp', 'dm', 'fl', 'pt', 'ua', 'au', 'ka', 'td',
            'rg', 'ex', 'rf', 'yf', 'og', 'hu', 'lu', 'wt', 'mb', 'rb', 'fh']

bigrams4 = ['ud', 'bi', 'cu', 'ik', 'gu', 'lw', 'ci', 'yc', 'nf', 'nn', 'rk',
            'rp', 'ju', 'ws', 'ps', 'yl', 'gw', 'ym', 'lk', 'sg', 'pu', 'sy',
            'yd', 'ek', 'ip', 'nu', 'hh', 'ks', 'nb', 'sk', 'gg', 'oy', 'tn',
            'ia', 'lb', 'kt', 'fs', 'tp', 'hy', 'ub', 'ah', 'fc', 'lh', 'yp',
            'sd', 'gb', 'eu', 'yr', 'hs', 'sr', 'fw', 'oe', 'bb', 'gf', 'vo',
            'yn', 'mm', 'lp', 'ib', 'lm', 'yg', 'hw', 'fy', 'va', 'iw', 'ko',
            'tg', 'mh', 'dv', 'rv', 'mw', 'nm', 'fm', 'lv', 'eq', 'gn', 'mf',
            'np', 'lr', 'cc', 'nv', 'lc', 'hm', 'ww', 'jo', 'wl', 'uf', 'gm',
            'gd', 'mr', 'xp', 'ih', 'kh', 'gp', 'gc', 'yy', 'mn', 'nr', 'gy',
            'uw', 'ky', 'sq', 'kw', 'ze', 'sv', 'ln', 'hf', 'ej', 'ph', 'xc',
            'nq', 'wr', 'hl', 'hb', 'bs', 'py', 'kl', 'uk', 'xt', 'kf', 'fb',
            'wm', 'iz', 'fd', 'tv', 'lg', 'pw', 'uv', 'yu', 'tk', 'mc', 'xi',
            'fp', 'dk', 'ml', 'wf', 'je', 'hc', 'sj', 'dq', 'dj', 'yv', 'uh',
            'xa', 'ix', 'wy', 'fg', 'wc', 'kb', 'wd', 'hd', 'mg', 'wb', 'pb',
            'hp', 'hn', 'hg', 'aa', 'tj', 'yk', 'uo', 'gv', 'nx', 'md', 'aj',
            'az', 'bt', 'wu', 'tq', 'ox', 'iu', 'fn', 'xe', 'ao', 'ku', 'pf']

def deck_rotation(deck):
    # Move Joker A
    indexa = deck.index(53)
    deck.pop(indexa)
    if indexa == 53:
        deck.insert(1, 53)
    else:
        deck.insert(indexa + 1, 53)


    # Move Joker B
    indexb = deck.index(54)
    deck.pop(indexb)
    if indexb == 53:
        deck.insert(2, 54)
    elif indexb == 52:
        deck.insert(1, 54)
    else:
        deck.insert(indexb + 2, 54)

    indexa = deck.index(53)
    indexb = deck.index(54)


    # Triple Cut
    beginning = []
    end = []
    if indexa < indexb:
        for i in range(0, indexa):
            beginning.append(deck[i])
        for i in range(indexb + 1, 54):
            end.append(deck[i])
        for i in range(0, indexa):
            deck.pop(0)
        for i in range((indexb - indexa) + 1, 54 - indexa):
            deck.pop((indexb - indexa) + 1)
    else:
        for i in range(0, indexb):
            beginning.append(deck[i])
        for i in range(indexa + 1, 54):
            end.append(deck[i])
        for i in range(0, indexb):
            deck.pop(0)
        for i in range((indexa - indexb) + 1, 54 - indexb):
            deck.pop((indexa - indexb) + 1)
    deck = end + deck + beginning


    # Count Cut
    beginning = []
    lastcard = deck[53]
    if lastcard < 53:
        count = lastcard
        deck.pop(53)
        for i in range(0, count):
            beginning.append(deck[i])
        for i in range(0, count):
            deck.pop(0)
        l = []
        l.append(lastcard)
        deck = deck + beginning + l
    return(deck)


def encrypt(message, deck):
    deckrotation = deck_rotation(deck)
    cipher = ""
    for letter in message:
        if letter not in alphabet:
            cipher += letter
        else:
            tf = True
            while tf:
                firstcard = deckrotation[0]
                if firstcard == 54:
                    firstcard = 53
                outputcard = deckrotation[firstcard]
                if outputcard < 53:
                    tf = False
                deckrotation = deck_rotation(deckrotation)
            newindex = alphabet.index(letter) + outputcard
            if newindex > 25:
                newindex -= 26
            if newindex > 25:
                newindex -= 26
            cipher += alphabet[newindex]
    return(cipher)


def decrypt(message, deck):
    deckrotation = deck_rotation(deck)
    cipher = ""
    for letter in message:
        if letter not in alphabet:
            cipher += letter
        else:
            tf = True
            while tf:
                firstcard = deckrotation[0]
                if firstcard == 54:
                    firstcard = 53
                outputcard = deckrotation[firstcard]
                if outputcard < 53:
                    tf = False
                deckrotation = deck_rotation(deckrotation)
            newindex = alphabet.index(letter) - outputcard
            if newindex < 0:
                newindex += 26
            cipher += alphabet[newindex]
    return(cipher)


def encrypt_key_word(message, deck, keyword):
    for letter in keyword.lower().replace(' ', ''):
        deck = deck_rotation(deck)
        count = alphabet.index(letter) + 1
        beginning = []
        lastcard = deck[53]
        deck.pop(53)
        for i in range(0, count):
            beginning.append(deck[i])
        for i in range(0, count):
            deck.pop(0)
        l = []
        l.append(lastcard)
        deck = deck + beginning + l
    return(encrypt(message, deck))


def decrypt_key_word(message, deck, keyword):
    for letter in keyword.lower().replace(' ', ''):
        deck = deck_rotation(deck)
        count = alphabet.index(letter) + 1
        beginning = []
        lastcard = deck[53]
        deck.pop(53)
        for i in range(0, count):
            beginning.append(deck[i])
        for i in range(0, count):
            deck.pop(0)
        l = []
        l.append(lastcard)
        deck = deck + beginning + l
    return(decrypt(message, deck))


def e_ratio(message):
    count = 0
    for letter in message:
        if letter == "e":
            count += 1
    return((count * 100) / len(message.replace(" ", "")))


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


def vowel_shortage(message):
    eight = n_gram_analysis(7, message)
    vowels = ['a', 'e', 'i', 'o', 'u']
    for l in eight:
        count = 0
        for v in vowels:
            if v not in l:
                count += 1
        if count == 5:
            return(True)
    return(False)


def english_rating(message): # Above 100 is definitely English
    if e_ratio(message) < 7:
        return(0)
    if vowel_shortage(message):
        return(0)
    bigrams = n_gram_analysis(2, message)
    rating = 0
    for bigram in bigrams:
        if bigram in bigrams1:
            rating += 2
        elif bigram in bigrams2:
            rating += 1
        elif bigram in bigrams3:
            rating += 0
        elif bigram in bigrams4:
            rating -= 1
        else:
            rating -= 2
    rating = (rating * 170)/ len(message.replace(" ", ""))
    return(rating)


def search(rating):
    count = 0
    for line in file2:
        count += 1
        if count % 1000 == 0:
            print(line)
        cipher = (decrypt_key_word(message, standarddeck(), str(line.strip().replace("'", "").replace('"', "").replace("/", ""))))
        if english_rating(cipher) > rating:
            print(line)
            print(english_rating(cipher))
            print(cipher)
            choice = raw_input("Stop or Continue? ")
            if choice.lower() == "s":
                break


file2 = open('wordsall.txt','r')

#search(100)

#print(english_rating(message))

#print(encrypt_key_word(message, standarddeck(), "keyword"))
#print(decrypt_key_word(message, standarddeck(), "keyword"))

#print(encrypt(message, standarddeck()))
#print(decrypt(message, standarddeck()))
