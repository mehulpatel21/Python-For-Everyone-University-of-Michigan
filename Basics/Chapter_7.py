def ch7_exe1():
    fname = input("Enter the file name: ")
    try:
        fhand = open(fname)
    except IOError:
        print ("File can't be opened", fname)
        exit()

    for line in fhand:
        line = line.rstrip().upper()
        print (line)


def ch7_exe2():
    fname = input("Enter the file name: ")
    linecount = 0
    spamconfidence = 0
    try:
        fhand = open(fname)
    except IOError:
        print ("File can't be opened", fname)
        exit()
    for line in fhand:
        if not line.startswith('X-DSPAM-Confidence:'):
            continue
        colonposition = line.find(':')
        confstring = line[colonposition+1:]
        confstring = float(confstring)
        linecount = linecount + 1
        spamconfidence = spamconfidence + confstring

    print ("Average Spam Confidence: ", spamconfidence/linecount)


def ch7_exe3():
    fname = input("Enter the file name: ")
    count = 0
    try:
        if fname == 'na na boo boo':
            print ("NA NA BOO BOO TO YOU - You've been punk'd!")
            exit()

        fhand = open(fname)

    except IOError:
        print ("File can't be opened", fname)
        exit()

    for line in fhand:
        if line.startswith('Subject:'):
            count = count+1

    print ("There were", count, " Subject lines in", fname)



ch7_exe1()
ch7_exe2()
ch7_exe3()