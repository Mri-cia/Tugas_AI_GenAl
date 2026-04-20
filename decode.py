import case_domain as dom
import util

# Melakukan decode 
def decode_cromosome(bit_list, low, high):
    bin_str = "".join(map(str, bit_list))
    bit_mult = int(bin_str, 2)
    return low +  (high - low) / (2**len(bit_list) - 1) * bit_mult 

