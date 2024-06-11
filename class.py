class manusia :
    def _init_(self,nama,nim,umur,hoby,tinggi_badan):
        self.nama = nama
        self.nim = nim
        self.umur = umur
        self.hoby = hoby
        self.tinggi_badan = tinggi_badan

    def sayhallo(self):
        print("hallo saya " + self.nama, "umur ", self.umur, "nim ", self.nim, "hoby", self.hoby, "tinggi_badan", self.tinggi_badan)

nama = input("masukan nama: ")
umur = input("masukan umur: ")
nim = input("masukan nim: ")
hoby = input("masukan hoby: ")
tinggi_badan=("masukan tinggi_badan: ")


