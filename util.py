import case_domain as dom

# Bagian ini untuk beberapa utilitas dalam perubahan bentuk bilangan atau tipe data
# Bisa juga diletakkan beberapa operasi pengecekan umum

def to_bin(n):
    return f"{n:#0{dom.CROMOSOME_PAD}b}"

def to_num(b):
    return (int(b, 2) - 10)

def is_in_value(n):
    if n <= -10 and n >= 10:
        return True
    else:
        return False
    
