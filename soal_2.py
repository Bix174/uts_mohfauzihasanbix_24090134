masukan_tahun = int(input('masukan tahun :'))
if masukan_tahun % 400 == 0 or (masukan_tahun % 4 == 0 and masukan_tahun % 100 != 0):
    print(f"Tahun {masukan_tahun} merupakan tahun kabisat")
else:
    print(f"Tahun {masukan_tahun} bukan merupakan tahun kabisat")