import case_domain as dom

def to_bin(n):
    return f"{n:#0{dom.CROMOSOME_PAD}b}"

def to_num(b):
    return (int(b, 2) - 10)

def is_in_value(n):
    if n <= -10 and n >= 10:
        return True
    else:
        return False
    
