import random

import case_domain as dom

# Bagian ini untuk beberapa utilitas dalam perubahan bentuk bilangan atau tipe data.
# Bisa juga diletakkan beberapa operasi pengecekan umum.

# Function untuk encode bilangan untuk mendekati dengan penggunaan binary atau digital.
# Memiliki beberapa tahapan agar dapat menjadi biner yang dapat digunakan kemudian untuk 
# algoritma genetika.
def encode_to_bits(value, low, high, bits):

    # Menghitung batas
    range_size = high - low

    # Melakukan normalisasi untuk melihat bilangan relatif terhadap titik terendah,
    # serta memposisikan bilangan agar dapat tepat masuk dalam bilangan biner
    decimal_val = int(round(((value - low) * (2**bits - 1)) / range_size))

    # Melakukan konversi
    bin_str = bin(decimal_val)[2:].zfill(bits)
    return [int(b) for b in bin_str]

