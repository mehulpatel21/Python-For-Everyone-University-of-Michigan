def compute_pay(hours, rate):
    if float(hours) > 160:
        payment = float(rate) * 160 + (float(hours) - 160) * float(rate) * 1.5
    elif float(hours) < 60:
        payment = float(rate) * 0.80 * float(hours)
    else:
        payment = float(rate) * float(hours)

    return payment


def score_card(score):
        if score >= 0.90:
            return "A"
        elif 0.80 <= score < 0.90:
            return "B"
        elif 0.70 <= score < 0.80:
            return "C"
        elif 0.60 <= score < 0.70:
            return "D"
        else:
            return "F"

try:
    h = raw_input("Enter monthly worked hours: ")
    r = raw_input("Enter your hourly rate: ")
    sc = raw_input("Enter the score: ")
    sc = float(sc)

    if h < 0 or r < 0 or sc > 1.0:
        raise ValueError
    else:
        print "Payment is:", compute_pay(h, r), "$"
        print "Score is:", score_card(sc)

except ValueError:
    print "BAD!!!! Enter valid arguments!!!!"

