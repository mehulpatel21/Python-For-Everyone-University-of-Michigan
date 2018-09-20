import string

"""
counts = dict()
print "Enter a line of text: "
line = raw_input()

words = line.split()
print "Words: ", words

for word in words:
    counts[word] = counts.get(word, 0) + 1

print "Counts: ", counts
print counts.keys()
print counts.values()
print counts.items()

for key, value in counts.items():
    print key, value

"""


def count_most_common_words():
    fname = input("Enter file name: ")
    fhand = open(fname, 'r')
    lines = fhand.read()
    texts = lines.split()

    counter = dict()
    for text in texts:
        counter[text] = counter.get(text, 0) + 1

    most_common_word = None
    most_common_word_count = None

    for Word, Count in counter.items():
        if most_common_word_count is None or Count > most_common_word_count:
            most_common_word = Word
            most_common_word_count = Count

    print(most_common_word, most_common_word_count)


def count_words_from_original_romeo():
    fname = input("Enter file name: ")
    try:
        fhand = open(fname)
    except IOError:
        print("File ", fname, " doesn't exist.")
        exit()

    counts = dict()
    for line in fhand:
        line = line.translate(None, string.punctuation)
        line = line.lower()
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

    print(counts)


#count_words_from_original_romeo()


def ch9_exe2():
    fname = input("Enter file name: ")
    try:
        fhand = open(fname)
    except IOError:
        print("File is not valid...", fname)
        exit()

    counts = dict()
    for line in fhand:
        line.rstrip()
        if not line.startswith('From '):
            continue
        line = line.split()
        counts[line[2]] = counts.get(line[2], 0) + 1
    print(counts)


#ch9_exe2()


def ch9_exe3():
    fname = input("Enter file name: ")
    try:
        fhand = open(fname)
    except IOError:
        print("File is not valid...", fname)
        exit()

    counts = dict()
    for line in fhand:
        line.rstrip()
        if not line.startswith('From '):
            continue
        line = line.split()
        counts[line[1]] = counts.get(line[1], 0) + 1
    print(counts)


#ch9_exe3()


def ch9_exe4():
    fname = input("Enter file name: ")
    try:
        fhand = open(fname)
    except IOError:
        print("File is not valid...", fname)
        exit()

    counts = dict()
    for line in fhand:
        line.rstrip()
        if not line.startswith('From '):
            continue
        line = line.split()
        counts[line[1]] = counts.get(line[1], 0) + 1
        max_value = None
        max_key = None
        for key, value in counts.items():
            if max_value is None or value > max_value:
                max_value = value
                max_key = key
    print(max_key, max_value)


#ch9_exe4()


def ch9_exe5():
    fname = input("Enter file name: ")
    try:
        fhand = open(fname)
    except IOError:
        print("File is not valid...", fname)
        exit()

    counts = dict()
    for line in fhand:
        line.rstrip()
        if not line.startswith('From '):
            continue
        line = line.split()
        email = line[1]
        email_domain = email.split('@')
        counts[email_domain[1]] = counts.get(email_domain[1], 0) + 1
    print(counts)


ch9_exe5()
