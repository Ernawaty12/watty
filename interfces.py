from abc import ABC, abstractmethod

class Bentuk(ABC):
  @abstractmethod
  def hitung_luas(self):
    pass

  @abstractmethod
  def hitung_keliling(self):
    pass

class Lingkaran(Bentuk):
  def __init__(self, jari_jari):
    self.jari_jari = jari_jari

  def hitung_luas(self):
    luas =  self.jari_jari * self.jari_jari
    return luas

  def hitung_keliling(self):
    keliling = 2 * self.jari_jari
    return keliling

class PersegiPanjang(Bentuk):
  def __init__(self, panjang, lebar):
    self.panjang = panjang
    self.lebar = lebar

  def hitung_luas(self):
    luas = self.panjang * self.lebar
    return luas

  def hitung_keliling(self):
    keliling = 2 * (self.panjang + self.lebar)
    return keliling

# Menghitung luas dan keliling lingkaran
lingkaran = Lingkaran(7)
luas_lingkaran = lingkaran.hitung_luas()
keliling_lingkaran = lingkaran.hitung_keliling()
print(f"Luas lingkaran: {luas_lingkaran}")
print(f"Keliling lingkaran: {keliling_lingkaran}")

# Menghitung luas dan keliling persegi panjang
persegi_panjang = PersegiPanjang(10, 5)
luas_persegi_panjang = persegi_panjang.hitung_luas()
keliling_persegi_panjang = persegi_panjang.hitung_keliling()
print(f"Luas persegi panjang: {luas_persegi_panjang}")
print(f"Keliling persegi panjang: {keliling_persegi_panjang}")
