def get_farheniet(temp=0):
    return "{} degree farheniet".format(((float(9)/5)*temp + 32))


def get_celsius(temp=0):
    return "{} degree celsius".format((float(5)/9)*(temp-32))