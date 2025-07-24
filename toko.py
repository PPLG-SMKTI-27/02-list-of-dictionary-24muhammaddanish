items = [
    {"nama": "Buku", "stok": 20, "harga": 12000},
    {"nama": "Pensil", "stok": 15, "harga": 11000},
    {"nama": "Pulpen", "stok": 10, "harga": 14000},
    {"nama": "Penggaris", "stok": 30, "harga": 23000},
    {"nama": "Handuk", "stok": 25, "harga": 17000}
]

angka = 1
for i in items:
    print(f"{angka}.\tNama : {i['nama']}\n\tStok : {i['stok']}\n\tHarga : {i['harga']}\n\n")
    angka = angka + 1
    

def tambah_item():
    nama = input("Masukkan nama barang: ")
    stok = int(input("Masukkan jumlah stok: "))
    harga = int(input("Masukkan harga barang: "))
    
    item_baru = {
        "nama": nama,
        "stok": stok,
        "harga": harga
    }

    items.append(item_baru)
    print("Item berhasil ditambahkan!")

tambah_item()

angka = 1
for i in items:
    print(f"{angka}.\tNama : {i['nama']}\n\tStok : {i['stok']}\n\tHarga : {i['harga']}rp\n\n")
    angka = angka + 1