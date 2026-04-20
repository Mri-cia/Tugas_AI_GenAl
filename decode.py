import case_domain as dom
import util

# Membagi rumus menjadi 4 bagian 
def decode_cromosome(c):
    undressed_cromosome = c[2:]

    first_part = dom.MIN_VALUE
    second_part = dom.MAX_VALUE - dom.MIN_VALUE
    third_part = denominator_summation(dom.CROMOSOME_NUM)
    fourth_part = bit_summation(dom.CROMOSOME_NUM, undressed_cromosome)

    result = first_part + (second_part / third_part * fourth_part)

    return result


# Untuk penghitungan bagian notasi sigma yang menjumlahkan pangkat negatif dari 2 
# sejumlah dengan jumlah maksimal bit
def denominator_summation(length):
    num = 0
    for p in range (1, length+1):
        num += 2**(-p)

    return num

# Untuk penghitungan bagian notasi sigma yang menjumlahkan pangkat negatif dari 2
# sejumlah dengan jumlah maksimal bit, namun dikalikan dengan setiap bit
def bit_summation(length,bits):
    num = 0
    for p in range (1, length):
        # print(bits)
        num += int(bits[p-1], 2)*(2**(-p))
    
    return num