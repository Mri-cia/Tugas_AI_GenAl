import random

import case_domain as dom

# Bagian ini untuk beberapa utilitas dalam perubahan bentuk bilangan atau tipe data
# Bisa juga diletakkan beberapa operasi pengecekan umum

def to_bin(n):
    return f"{n+10:#0{dom.CROMOSOME_PAD}b}"[2:]

def to_num(b):
    return int(b, 2) - 10

def is_in_value(n):
    if n <= -10 and n >= 10:
        return True
    else:
        return False
    
def combined_parents(x1, x2):
    parent1 = x1[0] + x1[1]
    return parent1    

def encode_to_bits(value, low, high, bits):
    range_size = high - low
    decimal_val = int(round(((value - low) * (2**bits - 1)) / range_size))
    bin_str = bin(decimal_val)[2:].zfill(bits)
    return [int(b) for b in bin_str]

