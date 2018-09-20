def average_of_list():
    numlist = list()
    while True:
        inp = input("Enter a number: ")
        if inp == 'done':
            break
        value = float(inp)
        numlist.append(value)

    average = sum(numlist)/len(numlist)
    print ("Average: ", average)


def extract_day_of_the_week():
    fhand = open('mbox-short.txt')
    for line in fhand:
        line = line.rstrip()
        if not line.startswith('From '):
            continue
        line = line.split()
        print (line[2])


def extract_email_domain():
    fhand = open('mbox-short.txt')
    for line in fhand:
        line = line.rstrip()
        if not line.startswith('From '):
            continue
        line = line.split()
        email = line[1]
        email_domain = email.split('@')
        print (email_domain[1])


#extract_email_domain()


def chop(mylist):
    last_index = len(mylist) - 1
    del mylist[last_index]
    del mylist[0]
    return None

#print chop([1,2,3,4,5])


def middle(mylist):
    return mylist[1:len(mylist)-1]


#print middle([1,2,3,4,5])


def ch8_exe4():
    fname = input("Enter file: ")
    fhand = open(fname)
    list_of_words = []
    for line in fhand:
        line = line.strip('\n').split(' ')
        for word in line:
            if word in list_of_words:
                pass
            else:
                list_of_words.append(word)
    print (sorted(list_of_words))


def ch8_exe5():
    fhand = open('mbox-short.txt')
    count = 0
    for line in fhand:
        line = line.rstrip()
        if not line.startswith('From '):
            continue
        line = line.split()
        email = line[1]
        count = count + 1
        print (email)
    print ("There were", count, "lines in the file with From as the first word.")


def ch8_exe6():
    list_of_numbers = []
    while True:
        user_input = input("Enter a number: ")
        user_input = float(user_input)
        if user_input == 'done':
            print("Exception should be raised")
            break
        list_of_numbers.append(user_input)
    print(min(list_of_numbers), max(list_of_numbers))


#ch8_exe4()
#ch8_exe5()
ch8_exe6()
