fname = raw_input("Enter the file name: ")
try:
    fhand = open(fname)
except IOError:
    print "File can't be opened", fname
    exit()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print line

