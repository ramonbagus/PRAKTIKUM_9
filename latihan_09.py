kendaraan = ['motor', 'mobil', 'sepeda', 'bus']

# Menambahkan truk ke dalam list
kendaraan.append('truk')
print("Setelah ditambahkan truk:", kendaraan)

# Menambahkan becak pada posisi kedua
kendaraan.insert(1, 'becak')
print("Setelah ditambahkan becak:", kendaraan)

# Menghapus kendaraan yang paling belakang
kendaraan.pop()
print("Setelah data terakhir dihapus:", kendaraan)

# Mengganti sepeda menjadi skuter
kendaraan[3] = 'skuter'
print("Setelah sepeda diganti skuter:", kendaraan)

# Menghitung jumlah kendaraan
print("Jumlah seluruh kendaraan:", len(kendaraan))

angka = [75, 80, 90, 75, 85, 100, 65]

# Mencari posisi nilai 100
print("Nilai 100 berada di indeks:", angka.index(100))

# Menghitung jumlah siswa yang mendapat nilai 75
print("Jumlah siswa dengan nilai 75:", angka.count(75))

# Mengurutkan nilai dari yang terkecil
angka.sort()
print("Nilai dari terkecil:", angka)

# Membalik urutan nilai menjadi terbesar
angka.reverse()
print("Nilai dari terbesar:", angka)

menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]

# Menggabungkan kedua menu
menu_utama.extend(menu_tambahan)

# Menampilkan semua menu
print("Daftar menu makanan dan minuman:")
print(menu_utama)

data_barang = [
    ["Buku", 5000],
    ["Pensil", 2000],
    ["Penggaris", 3000]
]

# Menampilkan harga pensil
print("Harga Pensil:", data_barang[1][1])

# Menampilkan semua barang menggunakan perulangan
print("\nDaftar Barang:")

for barang in data_barang:
    nama = barang[0]
    harga = barang[1]

    print("Nama:", nama, "Harga:", harga)