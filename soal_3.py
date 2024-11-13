jumlah_barang = int(input('masukan jumlah barang:'))
stor_barang = 0 

for i in range (1, jumlah_barang +1):
    harga_barang = int(input('masukan harga barang :'))
    stor_barang += harga_barang
    penggabungan = stor_barang + harga_barang

print(f'total belanja : rp {penggabungan}' )