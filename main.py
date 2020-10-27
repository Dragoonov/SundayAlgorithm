import random
import matplotlib.pyplot as plt

# Predefined constants
A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']
lastp = {'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1, 'f': -1, 'g': -1, 'h': -1, 'i': -1,
         'j': -1, 'k': -1, 'l': -1, 'm': -1, 'n': -1, 'o': -1, 'p': -1, 'r': -1, 's': -1,
         't': -1, 'u': -1, 'w': -1, 'x': -1, 'y': -1, 'z': -1}
Tsize = 20
Wsize = 3
TminSize = 30
TmaxSize = 50
WminSize = 1
WmaxSize = 9
minAlphabetSize = 5
data_amount = 50

#####################
# Global variables
comparison_amount = 0


def matches_at(t, p, w):
    global comparison_amount
    if len(t) < len(w):
        return False
    for i in range(len(w)):
        comparison_amount = comparison_amount + 1
        if w[i] != t[p + i]:
            return False
    return True


def report(p):
    print(f"Znaleziono na {p}")


def prepare_data(var):
    final_alphabets = []
    final_texts = []
    final_patterns = []
    final_lastp = []
    if var == 'A':
        for i in range(data_amount):
            alphabet = generate_random_alphabet()
            text = generate_text_from_alphabet(alphabet, False, False)
            pattern = generate_text_from_alphabet(alphabet, False, True)
            last = generate_lastp(pattern)
            final_alphabets.append(alphabet)
            final_texts.append(text)
            final_patterns.append(pattern)
            final_lastp.append(last)
    if var == 'T':
        for i in range(data_amount):
            alphabet = A.copy()
            text = generate_text_from_alphabet(alphabet, True, False)
            pattern = generate_text_from_alphabet(alphabet, False, True)
            last = generate_lastp(pattern)
            final_alphabets.append(alphabet)
            final_texts.append(text)
            final_patterns.append(pattern)
            final_lastp.append(last)
    if var == 'W':
        for i in range(data_amount):
            alphabet = A.copy()
            text = generate_text_from_alphabet(alphabet, False, False)
            pattern = generate_text_from_alphabet(alphabet, True, True)
            last = generate_lastp(pattern)
            final_alphabets.append(alphabet)
            final_texts.append(text)
            final_patterns.append(pattern)
            final_lastp.append(last)
    return [final_alphabets, final_texts, final_patterns, final_lastp]


def generate_random_alphabet():
    alphabet = A.copy()
    result_alphabet_size = random.randrange(1, len(alphabet)-minAlphabetSize)
    for i in range(result_alphabet_size):
        index = random.randrange(0, len(alphabet))
        alphabet.remove(alphabet[index])
    return alphabet


def generate_text_from_alphabet(alphabet, rand, pattern):
    text = ''
    size = Tsize
    if pattern:
        size = Wsize
    if rand:
        if pattern:
            size = random.randint(WminSize, WmaxSize)
        else:
            size = random.randint(TminSize, TmaxSize)
    for i in range(size):
        index = random.randrange(0, len(alphabet))
        text = text + alphabet[index]
    return text


def generate_lastp(pattern):
    last = lastp.copy()
    for i in range(len(pattern)):
        last[pattern[i]] = i
    return last


def sunday_algorithm(text, pattern, last):
    global comparison_amount
    comparison_amount = 0
    p = 0
    while p <= len(text) - len(pattern):
        if matches_at(text, p, pattern):
            report(p)
        p = p + len(pattern)
        if p < len(text):
            p = p - last[text[p]]
    return comparison_amount


def naive_algorithm(text, pattern):
    global comparison_amount
    comparison_amount = 0
    for i in range(len(text)-len(pattern)):
        if matches_at(text, i, pattern):
            report(i)
    return comparison_amount


def get_algorithm_data(data, var, algorithm):
    total_comp = []
    text_size = []
    for i in range(data_amount):
        if algorithm == 'S':
            total_comp.append(sunday_algorithm(data[1][i], data[2][i], data[3][i]))
        else:
            total_comp.append(naive_algorithm(data[1][i], data[2][i]))
        if var == 'A':
            text_size.append(len(data[0][i]))
        elif var == 'T':
            text_size.append(len(data[1][i]))
        elif var == 'W':
            text_size.append(len(data[2][i]))
    #text_size.sort()
    #total_comp.sort()
    return [text_size, total_comp]


def show_data(var):
    datas = prepare_data(var)
    naive = get_algorithm_data(datas, var, 'N')
    sunday = get_algorithm_data(datas, var, 'S')
    plt.scatter(naive[0], naive[1], label="Naiwny")
    plt.scatter(sunday[0], sunday[1], label="Sundaya")
    if var == 'A':
        plt.xlabel("Dlugosc alfabetu")
    elif var == 'T':
        plt.xlabel("Dlugosc tekstu")
    elif var == 'W':
        plt.xlabel('Dlugosc wzorca')
    plt.ylabel('Liczba porownan')
    plt.title('Porownanie naiwnego i sundaya')
    plt.legend()
    plt.show()


show_data('A')
show_data('T')
show_data('W')
