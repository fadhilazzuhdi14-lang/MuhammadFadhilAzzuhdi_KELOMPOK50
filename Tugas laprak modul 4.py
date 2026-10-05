# FUNCTION PERKENALAN KELOMPOK
def perkenalan_kelompok():
    print("=== Kelompok 50 ===")
    print("Anggota  :  NIM")
    print("1. ALDO ARKANANTA  :  21120126130075")
    print("2. MUHAMMAD FADHIL AZZUHDI  :  21120126130096")
    print("3. ERLITA EKLIN FEBIYANA  :  21120126120005")
    print("4. FADHIL MUHAMMAD HAFIZH  :  21120126140149")
    print("============================\n")


# FUNCTION RETURN TYPE
def hitung_diskon(subtotal, persen):
    return subtotal * persen


class SteamStore:
    def __init__(self):
        # Dictionary
        self.katalog_game = {
            "cyberpunk 2077": 700000,
            "gta v": 300000,
            "stardew valley": 115000,
            "left 4 dead 2": 90000
        }

        self.daftar_voucher = {
            "STEAMWINTER50": 0.50,
            "NEWUSER20": 0.20
        }

        # List dan String
        self.keranjang = []
        self.kode_voucher_aktif = ""

    # METHOD NON-RETURN TYPE
    def tampilkan_katalog(self):
        print("=== KATALOG GAME STEAM HARI INI ===")

        for nama_game, harga in self.katalog_game.items():
            print(f"> {nama_game.title():<20} : Rp {harga:,}")

        print("===================================\n")

    def tambah_ke_keranjang(self, nama_game):
        game_lower = nama_game.lower()

        if game_lower in self.katalog_game:
            self.keranjang.append(game_lower)
            print(f"[+] '{nama_game}' berhasil masuk keranjang.")
        else:
            print(f"[!] '{nama_game}' tidak ada di katalog kami.")

    def gunakan_voucher(self, kode):
        if kode in self.daftar_voucher:
            self.kode_voucher_aktif = kode
            print(f"[*] Voucher '{kode}' diterapkan!")
        else:
            print(f"[!] '{kode}' tidak valid.")

    # METHOD RETURN TYPE
    def hitung_harga_dan_diskon(self):
        subtotal = 0

        for item in self.keranjang:
            subtotal += self.katalog_game[item]

        total_diskon = 0.0

        if self.kode_voucher_aktif != "":
            persen = self.daftar_voucher[self.kode_voucher_aktif]

            # MEMANGGIL FUNCTION
            total_diskon = hitung_diskon(subtotal, persen)

        total_bayar = subtotal - total_diskon

        return subtotal, total_diskon, total_bayar

    # METHOD NON-RETURN TYPE
    def cetak_struk(self):
        subtotal, total_diskon, total_bayar = self.hitung_harga_dan_diskon()

        print("\n===================================")
        print("          STRUK PEMBELIAN          ")
        print("===================================")

        for game in self.keranjang:
            print(f"- {game.title():<20} : Rp {self.katalog_game[game]:,}")

        print("-----------------------------------")
        print(f"Subtotal             : Rp {subtotal:,}")
        print(f"Total Diskon         : Rp {int(total_diskon):,}")
        print("===================================")
        print(f"TOTAL BAYAR          : Rp {int(total_bayar):,}")
        print("===================================")


# PROGRAM UTAMA
perkenalan_kelompok()
toko = SteamStore()

toko.tampilkan_katalog()

toko.tambah_ke_keranjang("Cyberpunk 2077")
toko.tambah_ke_keranjang("GTA V")
toko.tambah_ke_keranjang("Left 4 Dead 2")

toko.gunakan_voucher("STEAMWINTER50")

toko.cetak_struk()