import util

# --- Konfigurasi ---
POP_SIZE = 20 #Jumlah populasi
BITS_PER_VAR = 16 #Jumlah bit yang digunakan pada satu variabel
TOTAL_BITS = BITS_PER_VAR * 2 #Total bit
DOMAIN = [-10, 10]  #Batasan
MUTATION_RATE = 0.02 #Tingkat Mutasi
GENERATIONS = 200
TOURNAMENT_SIZE = 2

# Inisiasi populasi awal
populasiAwal = [
    (-10, 5), (8, -2), (0, 0), (-5, -5), (3, 9), (-2, 1), (10, -10), (4, -4), (1, -8), (9, -10),
    (-8, 8), (1, -1), (6, 6), (-3, -3), (7, -9), (-1, 0), (9, 2), (-4, 4), (-9, 10), (4, 1)
]



