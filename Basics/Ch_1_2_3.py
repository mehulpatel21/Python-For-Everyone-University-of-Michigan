# Payroll function with try and except


def payroll():
    # User input
    hours = input("Enter your monthly hours: ")
    rate = input("Enter your hourly rate: ")

    # Try and Except
    try:
        # Conditional statements
        if float(hours) <= 0 or float(rate) <= 0:  # Type conversion
            raise ValueError  # raising exception
        elif float(hours) > 160:
            payment = float(rate) * 160 + (float(hours) - 160) * float(rate) * 1.5
        elif float(hours) < 60:
            payment = float(rate) * 0.80 * float(hours)
        else:
            payment = float(rate) * float(hours)
        print ("Your monthly payment is: $", payment)

    except ValueError:
        print ("Error, please enter valid arguments.")


payroll()
exit(0)