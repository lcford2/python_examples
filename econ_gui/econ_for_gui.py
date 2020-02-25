from __future__ import division


class EconCalcs(object):
    def __init__(self, find, have, amount, n, i):
        self.find = find
        self.have = have
        self.amount = amount
        self.n = n
        self.i = i

    def update_input(self, find, have, amount, n, i):
        self.find = find
        self.have = have
        self.amount = amount
        self.n = n
        self.i = i

    # Single Payment Compound Amount

    def foverp(self):
        p, i, n = self.amount, self.i, self.n
        f = p * (1 + i)**n
        return f

    # Single Payment Present Worth

    def poverf(self):
        f, i, n = self.amount, self.i, self.n
        p = f * (1 + i)**(-n)
        return p

    # Uniform Series Sinking Fund

    def aoverf(self):
        f, i, n = self.amount, self.i, self.n
        a = (f * i) / ((1 + i)**n - 1)
        return a

    # capital recovery

    def aoverp(self):
        p, i, n = self.amount, self.i, self.n
        a = p * ((i * (1 + i)**n) / ((1 + i)**n - 1))
        return a

    # uniform series compound amount

    def fovera(self):
        a, i, n = self.amount, self.i, self.n
        f = a * (((1 + i)**n - 1) / i)
        return f

    # uniform series present worth

    def povera(self):
        a, i, n = self.amount, self.i, self.n
        p = a * (((1 + i)**n - 1) / (i * (1 + i)**n))
        return p

    # uniform gradient present worth

    def poverg(self):
        g, i, n = self.amount, self.i, self.n
        factor = ((1 + i)**n - 1) / ((i**2) * (1 + i)**n) - \
            (n / (i * (1 + i)**n))
        p = factor * g
        return p

    # uniform gradient future worth

    def foverg(self):
        g, i, n = self.amount, self.i, self.n
        factor = (((1 + i)**n - 1) / i**2) - (n / i)
        f = g * factor
        return f

    # uniform gradient uniform series

    def aoverg(self):
        g, i, n = self.amount, self.i, self.n
        factor = (1 / i) - (n / ((1 + i)**n - 1))
        a = g * factor
        return a

    def goverp(self):
        amount = self.amount
        x = self.poverg()
        x = x / amount
        x = x**(-1)
        x = x * amount
        return x

    def goverf(self):
        amount = self.amount
        x = self.foverg()
        x = x / amount
        x = x**(-1)
        x = x * amount
        return x

    def govera(self):
        amount = self.amount
        x = self.aoverg()
        x = x / amount
        x = x**(-1)
        x = x * amount
        return x

    # capital costs

    def capcosts(self, choice):
        amount = self.amount
        i = self.i
        if choice == 'P':
            p = amount / i
            return p
        elif choice == 'A':
            a = amount * i
            return a

    @property
    def get_solution(self):
        func_map = {
            ("P", "A"): self.povera,
            ("P", "F"): self.poverf,
            ("P", "G"): self.poverg,
            ("F", "A"): self.fovera,
            ("F", "P"): self.foverp,
            ("F", "G"): self.foverg,
            ("A", "F"): self.aoverf,
            ("A", "P"): self.aoverp,
            ("A", "G"): self.aoverg,
            ("G", "P"): self.goverp,
            ("G", "F"): self.goverf,
            ("G", "A"): self.govera,
        }

        if self.find == "C":
            if self.have == 'P':
                return self.capcosts('A')
            elif self.have == 'A':
                return self.capcosts('P')
        return func_map[(self.find, self.have)]()


# non annual compounding


def effectivei(r, m):
    i = (1 + r / m)**m - 1
    return i


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
