import random

def random_wheel(list_prob):
  # Ubah probabilitas ke bobot, beri indeks untuk pilihan tanpa pengembalian
  kandidat = [[i, bobot] for i, bobot in enumerate(list_prob)]
  parent_id = []
  parent_val = []

  for _ in range(2):
      # Hitung sisa total bobot parent yg belum terpilih
      total = sum(item[1] for item in kandidat)
      
      rand = random.uniform(0, total)
      
      akumulasi = 0
      for i, item in enumerate(kandidat):
          akumulasi += item[1]
          if rand <= akumulasi:
              # Simpan indeks dan value
              parent_id.append(item[0])
              parent_val.append(item[1])
              # Hapus dari kandidat
              kandidat.pop(i)
              break
              
  return [parent_id, parent_val]