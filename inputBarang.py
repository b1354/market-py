import json
from module import clear_console, list_barang, cariId

def editMenu():
  print("---masukan barang---")
  print("==template==")
  print("kode : (angka)")
  print("produk : (huruf)")
  print("harga : (angka)")
  print("--------------------")

def masukanBarang(data):
  if cariId(data["kode"]):
    print("kode barang sudah digunakan")
    return False
  
  list_barang.append(data)
  json_object = json.dumps(list_barang, indent=2)

  try:
    with open('menu.json', "w") as outfile:
      outfile.write(json_object)
      print("data berhasil dimasukan")
      return True
  except:
    return False


def main():
  while(True):
    clear_console()
    editMenu()

    kode = int(input("Kode(masukan 0 untuk keluar): "))

    if not kode:
      break

    kode = str(kode)
    produk = str(input("Produk: "))
    harga = int(input("Harga: "))

    data = {
      "kode": kode,
      "produk": produk,
      "harga": harga
    }

    write_data = masukanBarang(data)

    if not write_data :
      print("data gagal di masukan")
      ulang = str(input("tekan (ENTER) untuk melanjutkan atau (n) untuk keluar: "))
      if (ulang == "n" or ulang == "N"):
        break
      continue

    ulang = str(input("masukan barang lagi?(y, n): "))

    if (ulang == "y" or ulang == "Y"):
      continue
    
    break
if __name__ == "__main__":
  main()