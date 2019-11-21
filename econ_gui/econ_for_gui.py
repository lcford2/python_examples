from __future__ import division

# Single Payment Compound Amount


def foverp(p, i, n):
    f = p * (1 + i)**n
    return round(f, 2)

# Single Payment Present Worth


def poverf(f, i, n):
    p = f * (1 + i)**(-n)
    return round(p, 2)

# Uniform Series Sinking Fund


def aoverf(f, i, n):
    a = (f * i) / ((1 + i)**n - 1)
    return round(a, 2)

# capital recovery


def aoverp(p, i, n):
    a = p * ((i * (1 + i)**n) / ((1 + i)**n - 1))
    return round(a, 2)

# uniform series compound amount


def fovera(a, i, n):
    f = a * (((1 + i)**n - 1) / i)
    return round(f, 2)

# uniform series present worth


def povera(a, i, n):
    p = a * (((1 + i)**n - 1) / (i * (1 + i)**n))
    return round(p, 2)

# uniform gradient present worth


def poverg(g, i, n):
    factor = ((1 + i)**n - 1) / ((i**2) * (1 + i)**n) - (n / (i * (1 + i)**n))
    p = factor * g
    return round(p, 2)

# uniform gradient future worth


def foverg(g, i, n):
    factor = (((1 + i)**n - 1) / i**2) - (n / i)
    f = g * factor
    return round(f, 2)

# uniform gradient uniform series


def aoverg(g, i, n):
    factor = (1 / i) - (n / ((1 + i)**n - 1))
    a = g * factor
    return round(a, 2)

# non annual compounding


def effectivei(r, m):
    i = (1 + r / m)**m - 1
    return round(i, 4)

# capital costs


def capcosts(choice, amount, i):
    if choice == 'P':
        p = amount / i
        return round(p, 2)
    elif choice == 'A':
        a = amount * i
        return round(a, 2)


def gui_run(find, have, amount, n, i):
    """Main control structure for the gui.
    Not very robust and should definitely be 
    updated but who has time for that?

    Arguments:
        find {str} -- ID for what the user is trying to find
        have {str} -- ID for what the user already has 
        amount {float} -- value for the ID specified with 'have'
        n {int} -- compounding periods
        i {float} -- interest rate 

    Returns:
        float -- calculated value corresponding to the id of 'find'
    """
    if find == 'C':
        if have == 'P':
            return(capcosts('A', amount, i))
        elif have == 'A':
            return(capcosts('P', amount, i))
    else:
        if find == 'P' and have == 'A':
            return povera(amount, i, n)
        elif find == 'P' and have == 'F':
            return poverf(amount, i, n)
        elif find == 'P' and have == 'G':
            return poverg(amount, i, n)
        elif find == 'F' and have == 'A':
            return fovera(amount, i, n)
        elif find == 'F' and have == 'P':
            return foverp(amount, i, n)
        elif find == 'F' and have == 'G':
            return foverg(amount, i, n)
        elif find == 'A' and have == 'F':
            return aoverf(amount, i, n)
        elif find == 'A' and have == 'P':
            return aoverp(amount, i, n)
        elif find == 'A' and have == 'G':
            return aoverg(amount, i, n)
        elif find == 'G' and have == 'P':
            x = (poverg(amount, i, n))
            x = x / amount
            x = x**(-1)
            x = round(x * amount, 2)
            return x
        elif find == 'G' and have == 'F':
            x = (foverg(amount, i, n))
            x = x / amount
            x = x**(-1)
            x = round(x * amount, 2)
            return x
        elif find == 'G' and have == 'A':
            x = (aoverg(amount, i, n))
            x = x / amount
            x = x**(-1)
            x = round(x * amount, 2)
            return x


if __name__ == '__main__':
    pass
