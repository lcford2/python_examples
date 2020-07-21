
def half_adder(a, b):
    """Representation of half adder ALU logic

    Args:
        a (binary integer): Either 0 or 1
        b (binary integer): Either 0 or 1

    Returns:
        tuple: (sum, carry)
    """
    return (a^b, a and b)

def full_adder(a, b, c):
    """Representation of full adder ALU logic. Uses half_adder function.

    Args:
        a (binary integer): Either 0 or 1, from the numbers being summed
        b (binary integer): Either 0 or 1, from the numbers being summed
        c (binary integer): Either 0 or 1, the carry from the half adder on the first two bits of the numbers

    Returns:
        tuple: (sum, carry)
    """
    s1, c1 = half_adder(a, b)
    s2, c2 = half_adder(s1, c)
    return (s2, c1 or c2)

def alu(x, y):
    x, y = x[::-1], y[::-1]
    s, c = half_adder(int(x[0]), int(y[0]))
    answer = [str(s)]
    for i in range(1, len(x)):
        s, c = full_adder(int(x[i]), int(y[i]), c)
        answer.append(str(s))
    if c:
        answer.append("1")
    return "".join(answer)[::-1]

if __name__ == "__main__":
    x = "110101011"
    y = "001101101"
    x_dec = int(x, 2)
    y_dec = int(y, 2)
    sum_dec = x_dec + y_dec
    sum_bin = alu(x, y)
    dec_sum_bin = int(sum_bin, 2)
    print(f"Adding {x_dec} ({x}) to {y_dec} ({y})")
    print(f"Answer should be {sum_dec}")
    print(f"Answer is {dec_sum_bin} ({sum_bin})")