import sys
sys.setrecursionlimit(1500)

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


def gcd_extended(num_1, num_2):
    if num_1 == 0:
        return num_2, 0, 1

    gcd, ret_1, ret_2 = gcd_extended(num_2 % num_1, num_1)

    temp_1 = ret_2 - (num_2 // num_1) * ret_1
    temp_2 = ret_1

    return gcd, temp_1, temp_2


# Driver code
# a, b = 35, 15
# g, x, y = gcd_extended(a, b)
# print("gcd(", a, ",", b, ") = ", g)


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

    return True


if __name__ == '__main__':
    phi = (p - 1) * (q - 1)

    if check_prime_numbers(p, q):
        print("p and q passed prime checks")

    print(f'p = {p}')
    print(f'q = {q}')
    print(f'phi = {phi}')

    n = p * q
    print(f'n = {n}')

    d = gcd_extended(e, phi)[1] + phi
    # d = gcd_extended(7, 40)[1]
    print(f'd = {d}')

    # print(f'mod_exp(e, d, phi) = {mod_exp(e, d, phi)}')

    plaintext = 63105876973776576013118303308612607892692110113866747753315393911113655406245183447806969185803131285735180363300314902062378950382445004919252498510156526251793553107461199184029830268059609007873897268593557258700290649029242792612388288069346285666035920160012591308639730475265335076590943800176010223678

    ciphertext = mod_exp(plaintext, e, n)

    print(f'ciphertext = {ciphertext}')

    ciphertext = 96549809174105142736868460849034701155905981775351207755276414668106989173601980746794630862878289420684995869856126233547264799918453886205220441141723350160700245587633201167240634066879266006853224048938734018907053136849265099653669408475271763035996365050309362651740414136085372447658649420009253911963

    plaintext = mod_exp(ciphertext, d, n)

    print(f'plaintext = {plaintext}')



