def divide(divisor, dividend):
    if divisor == 0:
        raise Exception("undefined divisor")
    if divisor < 0:
        raise Exception("negative divisor")
    return dividend/divisor


def give_me_divide():
    try:
        divide(0, 9)
    except Exception, e:
        if e.message == "undefined divisor":
            print "Ayyo"
        elif e.message == "negative divisor":
            print "this is ok"


give_me_divide()

