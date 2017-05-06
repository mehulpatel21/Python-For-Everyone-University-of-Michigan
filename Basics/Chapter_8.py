def average_of_list():
    numlist = list()
    while True:
        inp = raw_input("Enter a number: ")
        if inp == 'done':
            break
        value = float(inp)
        numlist.append(value)

    average = sum(numlist)/len(numlist)
    print "Average: ", average


def extract_dayofthe_week():
    fhand = open('mbox-short.txt')
    for line in fhand:
        line = line.rstrip()
        if not line.startswith('From '):
            continue
        line = line.split()
        print line[2]


def extract_email_domain():
    fhand = open('mbox-short.txt')
    for line in fhand:
        line = line.rstrip()
        if not line.startswith('From '):
            continue
        line = line.split()
        email = line[1]
        email_domain = email.split('@')
        print email_domain[1]


extract_email_domain()
