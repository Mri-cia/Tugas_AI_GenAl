import util

import case_domain as dom

# Inisialisasi data asli menjadi biner
def initialize_from_fixed(data):
    population = []
    for x1, x2 in data:
        bits_x1 = util.encode_to_bits(x1, dom.DOMAIN[0], dom.DOMAIN[1], dom.BITS_PER_VAR)
        bits_x2 = util.encode_to_bits(x2, dom.DOMAIN[0], dom.DOMAIN[1], dom.BITS_PER_VAR)
        population.append(bits_x1 + bits_x2)
    return population