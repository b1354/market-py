import json
from os import system, name

# deklarasi
list_barang = json.load(open('menu.json'))
troli = []

def clear_console():
  if name == "nt":
    _ = system("cls")
  else:
    _ = system("clear")

def showMenu():
  clear_console()
  print("--------List Barang-------")
  for barang in list_barang:
    for key, value in barang.items():
      print(key, ":",value)
    print("\n")
  print("--------------------------")

def cariId(id_barang):
  for i in list_barang:
    if i["kode"] == id_barang:
      return i
      break
  return False

def tambahKeTroli(id_barang, jumlah=1):
  barang = cariId(id_barang)
  barang["jumlah"] = jumlah
  barang["total"] = barang["harga"]*jumlah
  troli.append(barang)

def cetakNota():
  clear_console()
  print("terimakasih telah berbelanja")
  print("-------------")
  print("daftar belanjaan anda:")
  
  for i in troli:
    for key, value in i.items():
      print(key, value)
    print("\n")

  print("-------------")

def hitungJumlah():
  jumlah = 0
  for i in troli:
    jumlah+=i["total"]
  
  return jumlah