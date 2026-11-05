#Program 9.1 List

data_angka = [1, 5, 3, 2]
print (data_angka)

data_string = ["ucup", "didit", "siti"]
print (data_string)

data_boolean = [True, False, True, False]
print (data_boolean)

data_campuran = [1, "bakwan",2, "cireng","ucup",True,"adit",False]
print (data_campuran)

data_range = range (0,10,2)
print (data_range)
data_list = list(data_range)
print (data_list)

list_for = [i **2 for i in range (0,10)]
print (list_for)

list_for_if = [i for i in range (0,10) if i != 5]
print (list_for_if)

list_for_if = [i for i in range (0,10) if i % 2 == 0]
print (list_for_if)

list_for_if = [ i for i in range (0,10) if i % 2 != 0]
print (list_for_if)

#Pogram 9.2 manipulasi list
data = ["ucup", "adit", "dadang"]
data_0 = data[0]
print (f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print (f"data terakhir adalah = {data_terakhir}")

panjang_data = len(data)
print (f"panjang data = {panjang_data}")

#manipulasi data list
#menambahkan item pada list sesuai posisi
print (f"data sebelum ditambahkan = \n{data}")

data.insert(1, "asep")
print (f"data sesudah ditambahkan = \n{data}")

#menambahkan item pada list di akhir
data.append("ririn")
print (f"data ditambah lagi = \n{data}")

#menambah list dengan lsit
data_baru = ["luffy", "zoro", "nami"]
data.extend(data_baru)
print (f"data gabungan = \n{data}")

#ubah data
data[2] = "jarwo"
print (f"data dirubah = \n{data}")

#menghapus data 
data.remove("ucup")
print (f"data dihapus = \n{data}")

#hapus data terakhir
data.pop()
print (f"data terakhir = \n{data}")


#Pogram 9.3 operasi list
data_angka = [1, 5,1,4,3,2,4,3,2,3,7,8,9,0]
print (f"data angka = \n{data_angka}")

jumlah_data_4 = data_angka.count (4)
jumlah_data_3 = data_angka.count (3)

print (f"jumlah data 4 = {jumlah_data_4}")
print (f"jumlah data 3 = {jumlah_data_3}")

data = ["rendi", "iqbal", "gana", "khairul"]
print (f"data = \n{data}")

index_iqbal = data.index("iqbal")
print (f"index si iqbal = {index_iqbal}")
index_gana = data.index("gana")
print (f"index si gana = {index_gana}")

#mengurutkan list
print (f"data angka sebelum disort" = \n{data_angka})
data_angka.sort()
print (f"data angka sort" = \N{data_angka})

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

data_angka.reverse()
data.reverse()
print(f"data sort = {data}")
print(f"data sort = {data_angka}")

#pogram 9.3 nested list
data_1 = [1,2]
data_2 = [3,4]

data_list_biasa = [1,2,3,4]
print (f"list biasa = {data_list_biasa}")

list_2D=[data_1, data_2]
print (f"list 2D = {list_2D}")

#contoh penggunaan

peserta_0 = ["rendi", 25, "laki-laki"]
peserta_1 = ["Jons", 10, "laki-laki"]
peserta_2 = ["eka", 50, "perempuan"]
list_peserta = [peserta_0, peserta_1, peserta_2]
print (f"list peserta = {list_peserta}")

for peserta in list_peserta:
    print (f"nama\t : {peserta[0]}")
    print (f"umur\t : {peserta[1]}")
    print (f"jenis kelamin\t : {peserta[2]}")