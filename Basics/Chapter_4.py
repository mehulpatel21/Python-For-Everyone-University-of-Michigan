def compute_pay(hours, rate):
    if float(hours) > 160:
        payment = float(rate) * 160 + (float(hours) - 160) * float(rate) * 1.5
    elif float(hours) < 60:
        payment = float(rate) * 0.80 * float(hours)
    else:
        payment = float(rate) * float(hours)

    return payment


try:
    h = raw_input("Enter monthly worked hours: ")
    r = raw_input("Enter your hourly rate: ")
    if h < 0 or r < 0:
        raise ValueError
    else:
        print "Payment is: ", compute_pay(h, r), "$"


except ValueError:
    print "Error, enter valid arguments!"
