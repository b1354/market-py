# import module
from kasir import *
from inputBarang import main as inputProduk

# Program main()
while(True):
  showMenu()
  input_id_barang = str(input("Masukan ID barang(kosongkan jika sudah tidak ingin membeli): "))

  if (not input_id_barang):
    break
  elif (input_id_barang == "inputmenu"):
    inputProduk()
    continue
  elif (not cariId(input_id_barang)):
    input("kode barang tidak tersedia")
    continue

  input_jumlah = str(input("masukan jumlah barang(jika 1, kosongkan saja): "))

  if (not input_jumlah ):
    tambahKeTroli(input_id_barang)
  else:
    input_jumlah = int(input_jumlah)
    tambahKeTroli(input_id_barang, input_jumlah)

  clear_console()

cetakNota()
print("jumlah:")
print("Rp.", hitungJumlah())
