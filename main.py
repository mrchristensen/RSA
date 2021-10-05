e = 65537  # conventionally set to 65537 because it's cheap to compute as a modular exponent
length = 512

p = 12093052508411209097137915789819456285402849253990473693861406374161032085910240216876530688622125584156261168803170224163678192030681090010204179363074503  # openssl prime -safe -generate -bits 512
q = 10419152536405217741305777404841087847972037022527422018041014833672355482405341949557563632047176193138573405085128791001810176446786464028966205183108803  # openssl prime -safe -generate -bits 512


def mod_exp(x, y, n):  # returns: x^y % n
    if y == 0:
        return 1

    z = mod_exp(x, y // 2, n)
    if y % 2 == 0:  # If y is even
        return (z ** 2) % n
    else:  # If y is odd
        return (x * (z ** 2)) % n


def gcd(a, b):  # Euclid's algorithm
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def check_prime_numbers(num_1, num_2):
    mask = 1 << (length - 1)

    if mask & num_1 == 0:
        print(f'The leading bit on num_1 was not set: \n{hex(num_1)}')
        return False

    if mask & num_2 == 0:
        print(f'The leading bit on num_2 was not set: {num_2}')
        return False

    if gcd((num_1 - 1) * (num_2 - 1), e) > 1:
        print(f'(p−1)(q−1) and e were not relatively prime, gcd is: {gcd((num_1 - 1) * (num_2 - 1), e)}')
        return False


if __name__ == '__main__':
    if check_prime_numbers(p, q):
        print("p and q passed prime checks")

    n = p * q
    # TODO: find d
