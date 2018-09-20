largest_so_far = -1
print ("Before", largest_so_far)

for number in [100,200,300,400,500]:
    if number > largest_so_far:
        largest_so_far = number
    print ("largest right now", largest_so_far, "current number", number)

print ("After", largest_so_far)


found = False
print ("Before", found)
for number in [10,3,40,2,21]:
    if number == 100:
        found = True
    print (found, number)

print ("After", found)


smallest = None
print ("Before")
for number in [9,41,10,12,45]:
    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number
    print (smallest, number)
print ("After", smallest)


# Book exercises

def ch5_exe1():
    count = 0
    total = 0
    while True:
        user_input = input("Enter a number: ")

        if user_input == 'done':
            break
        if len(user_input) < 1:
            break

        try:
            value = float(user_input)
        except ValueError:
            print ("Non numeric value entered!")
            continue

        count = count + 1
        total = value + total
        print (value, total, count)

    print ("Average:", total/count)


def ch5_exe2():
    minimum = None
    maximum = -1
    while True:

        user_input = input("Enter a number: ")

        if user_input == 'done':
            break
        if len(user_input) < 1:
            break

        try:
            value = float(user_input)
        except ValueError:
            print ("Non numeric value entered!")
            continue

        if minimum is None:
            minimum = value
        elif value < minimum:
            minimum = value
        elif value > maximum:
            maximum = value

    print (minimum, maximum)


ch5_exe1()
ch5_exe2()

