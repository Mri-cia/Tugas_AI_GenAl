# Menyisakan ruang untuk sign "0b"
BINARY_SIGN_SPACE = 2

# Atribut untuk operasi genetic algoritm
MIN_VALUE = 0 #
MAX_VALUE = 5 #
CROMOSOME_NUM = 3 #
CROMOSOME_PAD = BINARY_SIGN_SPACE + CROMOSOME_NUM

# Inisiasi populasi awal
populasiAwal = [[10, 4],
                [-1, -8],
                [4, 7],
                [-4, 2]]

# Menentukan standar panjang bit
def max_cromosome():
    max_c = 0
    for x in populasiAwal:
        for v in x:
            cr = len(bin(v)[2:])
            if max_c <= cr:
                max_c = cr
    return max_c

