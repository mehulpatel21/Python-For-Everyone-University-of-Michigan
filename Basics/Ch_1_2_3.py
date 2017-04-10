# Payroll function with try and except


def payroll():
    hours = raw_input("Enter your monthly hours: ")
    rate = raw_input("Enter your hourly rate: ")

    try:
        if float(hours) <= 0:
            raise ValueError
        elif float(hours) > 160:
            payment = float(rate) * 160 + (float(hours) - 160) * float(rate) * 1.5
        elif float(hours) < 60:
            payment = float(rate) * 0.80 * float(hours)
        else:
            payment = float(rate) * float(hours)
        print "Your monthly payment is: $", payment

    except ValueError:
        print "Error, please enter valid arguments."


payroll()
