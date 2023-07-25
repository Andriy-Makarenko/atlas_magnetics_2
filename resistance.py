# u_in - input voltage, V
# u_out - output voltage, V
# i - current in the circuit, mA
# r_tot - total resistance, Ohm
# r_1, r_2 - resistance of first and second resistors respectively

def resistance(u_in, u_out, i):
    delta_u = u_in - u_out
    r_tot = u_in / (i / 1000)
    r_1 = delta_u / (i / 1000)
    r_2 = r_tot - r_1
    return f"First: {r_1} Ohm\nSecond: {r_2} Ohm"


if __name__ == '__main__':
    u_in = 12
    u_out = 3
    i = 5

    print(resistance(u_in, u_out, i))

    # for E24 Nominal values of resistances table
    # first - 1800 ohm (1.8 * 1 kOhm)
    # second - 600 ohm [2 * (3.0 * 100 Ohm) or (6.2 * 100 Ohm)]
