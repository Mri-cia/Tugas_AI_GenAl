import case_domain as dom

def decode_cromosome(c):
    undressed_cromosome = c[2:]

    first_part = dom.MIN_VALUE
    second_part = dom.MAX_VALUE - dom.MIN_VALUE
    third_part = denominator_summation(len(undressed_cromosome))
    fourth_part = bit_summation(dom.CROMOSOME_NUM, undressed_cromosome)

    result = first_part + (second_part / third_part * fourth_part)

    print(result)

def denominator_summation(length):
    num = 0
    for p in range (1, length+1):
        num += 2**(-p)

    return num

def bit_summation(length,bits):
    num = 0
    for p in range (1, length+1):
        num += int(bits[p-1], 2)*(2**(-p))

    return num