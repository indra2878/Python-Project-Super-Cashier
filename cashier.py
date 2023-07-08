import pandas as pd # untuk pembuatan dataframe tabel transaksi
import sys # untuk melakukan exit program

def create_id():
  
  # function untuk membuat id transaksi
  print("Selamat datang di Supermarket Andi!")
  transaction_id = "transaction_" + input("Masukkan id Anda: ")
  print(f"id transaksi Anda adalah {transaction_id}")
  print("Selamat berbelanja!")


list_name = [] # untuk menampung inputan nama item pesanan
list_qty = [] # untuk menampung inputan jumlah item pesanan
list_price = [] # untuk input menampung inputan harga item pesanan
list_subtotal = [] # untuk menampung hitungan jumlah * harga pesanan


class Transaction(object): # Class dari transaksi menampung method-method untuk digunakan pada transaksi


    def add_item(self):
        """" Method ini untuk membeli/menambah item pesanan mencakup input nama, jumlah dan 
        harga item pesanan, sesuai petunjuk/ ketentuan penginputan yang tersedia 
        sehingga didapat data yang sesuai dan valid. jika kode yang dimasukan salah maka user 
        diminta validasi kode hingga benar dan jika tidak ingin menambah item dapat pilih "no" 
        lalu proses berhenti. Inputan dimasukan ke dalam list yang sudah disediakan, lalu
        list tersebut dibuat ke dalam dictionary dan mengubahnya ke dalam bentuk dataframe."""

        while True:
            try:
                opsi_add = input("Apakah Anda ingin beli/menambah item pesanan?: (yes/no)").lower()

                if opsi_add == "yes":
                    while True:
                        try:
                            jumlah_tambahan = int(input("Anda mau beli/menambah pesanan berapa item?: "))
                            break
                        except ValueError:
                            print("Tuliskan jumlah pesanan dalam angka!")
        
                    for i in range(jumlah_tambahan):
                        self.item_name = input("Masukkan nama item pesanan: ")

                        # validasi type data int untuk qty item
                        while True:
                            try:
                                self.item_qty = int(input("Masukkan jumlah item pesanan: "))
                                break
                            except ValueError:
                                print("Tuliskan jumlah item pesanan dalam angka!")

                        # validasi type data int untuk harga item
                        while True:
                            try:
                                self.item_price = int(input("Masukkan harga item pesanan: "))
                                break
                            except ValueError:
                                print("Tuliskan harga item pesanan dalam angka!")
                   
                        self.subtotal = self.item_qty*self.item_price
                        list_name.append(self.item_name)
                        list_qty.append(self.item_qty)
                        list_price.append(self.item_price)
                        list_subtotal.append(self.subtotal)
            
                    print("Daftar pesanan yang telah dibeli/ditambahkan:")
                    dict_transaksi = {'Item Name' : list_name,
                                        'Item Qty': list_qty,
                                        'Item Price': list_price,
                                        'subtotal' : list_subtotal}
                    tabel_transaksi = pd.DataFrame(dict_transaksi)
                    print (tabel_transaksi)
                    break;
                
                elif opsi_add == "no":
                    break;

                else :
                    print("Inputan Salah, silahkan input ulang!")
                   
            except ValueError:
                continue
                

    def check_order(self):
        """" Method ini untuk memeriksa pesanan pelanggan, berupa tabel sehingga pelanggan 
        bisa memeriksa nama, jumlah, harga item pesanannya dan menentukan opsi proses selanjutnya.
        Didalamnya terdapat opsi "yes" untuk memeriksa dan menampilkan tabel pesanan yang diinput 
        sebelumnya, "no" untuk tdak melakukan apa-apa dan melakukan proses selanjutnya, 
        "cancel" untuk membatalkan proses transaksi dan keluar dari program."""

        dict_transaksi = {'Item Name' : list_name,
                          'Item Qty': list_qty,
                          'Item Price': list_price,
                          'subtotal' : list_subtotal}
        tabel_transaksi = pd.DataFrame(dict_transaksi)
        
        while True:
            try :
                kode_check = str(input("Apakah Anda ingin memeriksa pesanan anda ? (yes/no/cancel)")).lower()
                if kode_check == "yes":
                    print("Daftar pesanan terbaru Anda:")
                    print (tabel_transaksi)
                                        
                    while True:
                        try:
                            hasil_check = str(input("Apakah pesanan Anda sudah benar?: (yes/no)")).lower()
                            if hasil_check == "yes":
                                print("Pesanan anda sudah benar silahkan lakukan pembayaran!.")
                                break;
                            elif hasil_check == "no":
                                print("Terdapat kesalahan input, silahkan ubah pesanan anda!.")
                                break;
                            else:
                                print("Kode yang Anda masukkan salah, silahkan input ulang!.")
                                continue  
                        except ValueError:
                            continue
                    break;    

                elif kode_check == "no":
                    break;
                    
                elif kode_check == "cancel":
                    sys.exit("Pembatalan Proses...")
                    
                else :
                    print("Kode yang diinput salah, silahkan input ulang!")
                    
            except ValueError:
                continue


    def update_item(self):
        """" Method ini untuk mengubah data pesanan hasil inputan sebelumnya, sehingga pelanggan
        bisa mengubah nama, jumlah, harga item pesanannya sesuai opsi yang tersedia beserta data 
        validasinya sampai didapat data yang sesuai dan valid. Di awal disediakan opsi "yes" 
        untuk mengubah data pesanan, "no" untuk tidak melakukan perubahan lalu ke proses selanjutnya.
        customer bisa memilih opsi 1: untuk mengubah nama item, opsi 2: untuk mengubah jumlah item 
        dan opsi 3: untuk mengubah harga item. Pada masing opsi di uji validitas datanya, bila ada 
        kesalahan pada nama item yang akan diubah, maka muncul warning dan diminta input ulang 
        sampai valid, untuk jumlah dan harga item data yang dimasukkan harus berupa angka bila salah
        maka muncul warning dan diminta input ulang sampai valid"""
        
        while True:
            try:
                opsi_update = input("Apakah Anda ingin mengubah item pesanan?: (yes/no)").lower()

                if opsi_update == "yes":
                                     
                    print("1. mengganti nama item saja")
                    print("2. mengganti jumlah item saja")
                    print("3. mengganti harga item saja")
                    opsi_update_item = int(input("Tuliskan opsi mengubah item: (1/2/3)"))

                    if opsi_update_item == 1:
                        #validasi nama item yang akan diupdate
                        for item in list_name:
                            while True:
                                try:
                                    items_update_name = input("masukkan nama item yang diganti:")
                                    list_name.index(items_update_name)
                                    break;
                                except:
                                    print("Nama item tidak ada dalam pesanan")
                                    continue
                                      
                            item_name_update = input("masukkan nama item pengganti: ")
                            indeks_name = list_name.index(items_update_name)
                            list_name[indeks_name] = item_name_update

                            dict_transaksi = {'Item Name' : list_name,
                                                'Item Qty': list_qty,
                                                'Item Price': list_price,
                                                'subtotal' : list_subtotal}
                            tabel_transaksi = pd.DataFrame(dict_transaksi)

                            print("Daftar pesanan yang telah diubah:")
                            print(tabel_transaksi)
                            break;
                        break;

                    elif opsi_update_item == 2:
                        #validasi nama item yang akan diupdate
                        for item in list_name:
                            while True:
                                try:
                                    items_update_name = input("masukkan nama item yang diganti:")
                                    list_name.index(items_update_name)
                                    break;
                                except:
                                    print("Nama item tidak ada dalam pesanan")
                                    continue
                            break;

                        indeks_name = list_name.index(items_update_name)
                        
                        # validasi type data int untuk jumlah item
                        for item in list_name:
                            while True:
                                try:
                                    item_qty_update = int(input("masukkan jumlah item pengganti: "))
                                    break;
                                except ValueError:
                                    print("Tuliskan jumlah item dalam angka!")
                            
            
                            list_qty[indeks_name] = item_qty_update
                            list_subtotal[indeks_name] = list_price[indeks_name]*item_qty_update

                            dict_transaksi = {'Item Name' : list_name,
                                            'Item Qty': list_qty,
                                            'Item Price': list_price,
                                            'subtotal' : list_subtotal}
                            tabel_transaksi = pd.DataFrame(dict_transaksi)

                            print("Daftar pesanan yang telah diubah:")
                            print(tabel_transaksi)
                            break;
                        break;

                    elif opsi_update_item == 3:
                        #validasi nama item yang akan diupdate
                        for item in list_name:
                            while True:
                                try:
                                    items_update_name = input("masukkan nama item yang diganti:")
                                    list_name.index(items_update_name)
                                    break;
                                except:
                                    print("Nama item tidak ada dalam pesanan")
                                    continue
                            break;
                        indeks_name = list_name.index(items_update_name)
                        
                         # validasi type data int untuk harga item
                        for item in list_name:
                            while True:
                                try:
                                    item_price_update = int(input("masukkan harga item pengganti: "))
                                    break;
                                except ValueError:
                                    print("Tuliskan harga item dalam angka!")
                                            
                            list_price[indeks_name] = item_price_update
                            list_subtotal[indeks_name] = item_price_update*list_qty[indeks_name]

                            dict_transaksi = {'Item Name' : list_name,
                                            'Item Qty': list_qty,
                                            'Item Price': list_price,
                                            'subtotal' : list_subtotal}
                            tabel_transaksi = pd.DataFrame(dict_transaksi)

                            print("Daftar pesanan yang telah diubah:")
                            print(tabel_transaksi)
                            break;
                        break;

                elif opsi_update == "no":
                    break;
                break;
            
            except ValueError:
                continue       
 
    def update_item_name(self):
        """"Merupakan method opsional perubahan item yang lebih spesifik dibandingkan 
        update_item(). Method ini khusus untuk mengubah nama item pesanan, sesuai petunjuk/
        ketentuan penginputan yang tersedia sehingga didapat data yang sesuai dan valid. 
        Di awal disediakan opsi "yes" untuk mengubah data pesanan, dan "no" untuk tidak
        mengubah item dan lanjut ke proses selanjutnya. Bila ada kesalahan pada nama item 
        yang akan diubah, maka muncul warning dan diminta input ulang sampai valid, 
        untuk jumlah dan harga item data yang dimasukkan harus berupa angka bila salah maka
        muncul warning dan diminta input ulang sampai valid."""
       
        while True:
            try:
                opsi_update = input("Apakah Anda ingin mengubah nama item pesanan?: (yes/no)").lower()

                if opsi_update == "yes":
                    #validasi nama item yang akan diupdate
                    for item in list_name:
                        while True:
                            try:
                                items_update_name = input("masukkan nama item yang diganti:")
                                list_name.index(items_update_name)
                                break;
                            except:
                                print("Nama item tidak ada dalam pesanan")
                                continue
                         
                        
                        item_name_update = input("masukkan nama item pengganti: ")
                        
                        indeks_name = list_name.index(items_update_name)
                        list_name[indeks_name] = item_name_update                                            
                        dict_transaksi = {'Item Name' : list_name,
                                            'Item Qty': list_qty,
                                            'Item Price': list_price,
                                            'subtotal' : list_subtotal}
                        tabel_transaksi = pd.DataFrame(dict_transaksi)

                        print("Daftar pesanan yang telah diubah:")
                        print(tabel_transaksi) # menampilkan tabel pesanan setelah diupdate
                        break;
                
                    else:
                        print("Tidak ada Nama itu dalam pesanan")
                    break;
                    
                elif opsi_update == "no":
                    break;
                break;
                
            except ValueError:
                continue               
              
    def update_item_qty(self): 
        """"Merupakan method opsional perubahan item yang lebih spesifik dibandingkan
        update_item(). Method ini khusus untuk mengubah jumlah item pesanan, sesuai petunjuk/
        ketentuan penginputan yang tersedia sehingga didapat data yang sesuai dan valid. 
        Di awal disediakan opsi "yes" untuk mengubah data pesanan, dan "no" untuk tidak mengubah
        item dan lanjut ke proses selanjutnya. Bila ada kesalahan pada nama item yang akan diubah,
        maka muncul warning dan diminta input ulang sampai valid, untuk jumlah dan harga item data 
        yang dimasukkan harus berupa angka bila salah maka muncul warning dan diminta input ulang 
        sampai valid."""
        
        while True:
            try:
                opsi_update = input("Apakah Anda ingin mengubah jumlah item pesanan?: (yes/no)").lower()

                if opsi_update == "yes":

                     #validasi nama item yang akan diupdate
                    for item in list_name:
                        while True:
                            try:
                                items_update_name = input("masukkan nama item yang diganti:")
                                list_name.index(items_update_name)
                                break;
                            except:
                                print("Nama item tidak ada dalam pesanan")
                                continue
                        break;
                    indeks_name = list_name.index(items_update_name)
                
                    # validasi type data int untuk jumlah item
                    for item in list_name:
                        while True:
                            try:
                                item_qty_update = int(input("masukkan jumlah item pengganti: "))
                                break;
                            except ValueError:
                                print("Tuliskan jumlah item dalam angka!")
            
                        list_qty[indeks_name] = item_qty_update
                        list_subtotal[indeks_name] = list_price[indeks_name]*item_qty_update

                        dict_transaksi = {'Item Name' : list_name,
                                        'Item Qty': list_qty,
                                        'Item Price': list_price,
                                        'subtotal' : list_subtotal}
                        tabel_transaksi = pd.DataFrame(dict_transaksi)

                        print("Daftar pesanan yang telah diubah:")
                        print(tabel_transaksi) # menampilkan tabel pesanan setelah diupdate
                        break;
                    break;

                elif opsi_update == "no":
                    break;
                break;
            
            except ValueError:
                continue

    
    def update_item_price(self):
        """"Merupakan method opsional perubahan item yang lebih spesifik dibandingkan
        update_item(). Method ini khusus untuk mengubah harga item pesanan, sesuai 
        petunjuk/ ketentuan penginputan yang tersedia sehingga didapat data yang sesuai
        dan valid.Di awal disediakan opsi "yes" untuk mengubah data pesanan, dan "no" 
        untuk tidak mengubah item dan lanjut ke proses selanjutnya. Bila ada kesalahan 
        pada nama item yang akan diubah, maka muncul warning dan diminta input ulang 
        sampai valid, untuk jumlah dan harga item data yang dimasukkan harus berupa angka
        bila salah maka muncul warning dan diminta input ulang sampai valid."""
        
        while True:
            try:
                opsi_update = input("Apakah Anda ingin mengubah harga item pesanan?: (yes/no)").lower()

                if opsi_update == "yes":
        
                    #validasi nama item yang akan diupdate
                    for item in list_name:
                            while True:
                                try:
                                    items_update_name = input("masukkan nama item yang diganti:")
                                    list_name.index(items_update_name)
                                    break;
                                except:
                                    print("Nama item tidak ada dalam pesanan")
                                    continue
                            break;

                    indeks_name = list_name.index(items_update_name)
                        
                    # validasi type data int untuk harga item
                    for item in list_name:
                        while True:
                            try:
                                item_price_update = int(input("masukkan harga item pengganti: "))
                                break;
                            except ValueError:
                                print("Tuliskan harga item dalam angka!")
                                            
                        list_price[indeks_name] = item_price_update
                        list_subtotal[indeks_name] = item_price_update*list_qty[indeks_name]

                        dict_transaksi = {'Item Name' : list_name,
                                         'Item Qty': list_qty,
                                         'Item Price': list_price,
                                         'subtotal' : list_subtotal}
                        tabel_transaksi = pd.DataFrame(dict_transaksi)

                        print("Daftar pesanan yang telah diubah:")
                        print(tabel_transaksi) # menampilkan tabel pesanan setelah diupdate
                        break;
                    break;

                elif opsi_update == "no":
                    break;
                break;
                
            except ValueError:
                continue

       
    def delete_reset(self):
        """Method ini untuk menghapus pesanan dari daftar belanja  (1 baris belanjaan).
        Di awal disediakan opsi "yes" untuk menghapus pesanan, dan "no" untuk tidak 
        menghapus pesanan dan lanjut ke proses selanjutnya. Ada 2 opsi penghapusan: 
        1. menghapus sebagian  pesanan, 2. menghapus seluruh pesanan (mengosongkan list pesanan),
        nama item dijadikan data acuan untuk melakukan proses penghapusan bila ada kesalahan 
        pada nama item yang akan dihapus, maka muncul "warning" dan diminta input ulang 
        sampai valid, untuk jumlah dan harga item data yang dimasukkan harus berupa angka 
        bila salah maka muncul "warning" dan diminta input ulang sampai valid."""

        while True:
            try:
                opsi_delete = input("Apakah Anda ingin menghapus pesanan?: (yes/no)").lower()

                if opsi_delete == "yes":
                    print("1. menghapus sebagian pesanan")
                    print("2. menghapus seluruh pesanan/ reset")
                    opsi_delete_reset = (int(input("Pilih opsi menghapus pesanan: (1/2)")))

                    if opsi_delete_reset == 1:
                        for item in list_name:
                            while True:
                                try:
                                    items_delete_name = input("masukkan nama item yang akan dihapus:")
                                    list_name.index(items_delete_name)
                                    break;
                                except:
                                    print("Nama item tidak ada dalam pesanan")
                                    continue

                            indeks_delete_item = list_name.index(items_delete_name)
                            list_name.pop(indeks_delete_item)
                            list_qty.pop(indeks_delete_item)
                            list_price.pop(indeks_delete_item)
                            list_subtotal.pop(indeks_delete_item)

                            dict_transaksi = {'Item Name' : list_name,
                                        'Item Qty': list_qty,
                                        'Item Price': list_price,
                                        'subtotal' : list_subtotal}
                            tabel_transaksi = pd.DataFrame(dict_transaksi)

                            print(tabel_transaksi) # menampilkan tabel pesanan setelah dihapus sebagian
                            print("Sebagian pesanan Anda telah dihapus.")
                            break;
                        break;

                    elif opsi_delete_reset == 2:
                        list_name.clear()
                        list_qty.clear()
                        list_price.clear()
                        list_subtotal.clear()

                        dict_transaksi = {'Item Name' : list_name,
                                    'Item Qty': list_qty,
                                    'Item Price': list_price,
                                    'subtotal' : list_subtotal}
                        tabel_transaksi = pd.DataFrame(dict_transaksi)

                        print(tabel_transaksi) # menampilkan tabel pesanan setelah direset
                        print("Pesanan Anda telah dihapus semua silahkan belanja kembali!.")
                        break;
                        
                elif opsi_delete == "no":
                    print("Silahkan ke proses selanjutnya.")
                    break;
               
                else :
                    print("kode yang anda masukkan salah.")
                    continue
                break;
            
            except ValueError:
                continue


    def delete_item(self):
        """" Method ini untuk penghapusan pesanan yang lebih spesifik dibandingkan 
        delete_reset(), yaitu untuk menghapus sebagian pesanan (1 baris dalam tabel pesanan),
        sesuai petunjuk dan validasi data yang tersedia sehingga didapat data yang sesuai 
        dan valid."""
        
        while True:
            try:
                opsi_delete = input("Apakah Anda ingin menghapus sebagian pesanan?: (yes/no)").lower()

                if opsi_delete == "yes":

                    #validasi nama item yang akan dihapus
                    for item in list_name:
                        while True:
                            try:
                                items_delete_name = input("masukkan nama item yang akan dihapus:")
                                list_name.index(items_delete_name)
                                break;
                            except:
                                print("Nama item tidak ada dalam pesanan")
                                continue

                        indeks_delete_item = list_name.index(items_delete_name)
                        list_name.pop(indeks_delete_item)
                        list_qty.pop(indeks_delete_item)
                        list_price.pop(indeks_delete_item)
                        list_subtotal.pop(indeks_delete_item)

                        dict_transaksi = {'Item Name' : list_name,
                                         'Item Qty': list_qty,
                                        'Item Price': list_price,
                                        'subtotal' : list_subtotal}
                        tabel_transaksi = pd.DataFrame(dict_transaksi)

                        print(tabel_transaksi) # menampilkan tabel pesanan setelah penghapusan item
                        print("item pesanan Anda telah dihapus.")
                        break;
                    break;

                elif opsi_delete == "no":
                    break;
               
                else :
                    print("kode yang anda masukkan salah.")
                break;

            except ValueError:
                continue


    def reset_order(self):
        """" Method ini untuk penghapusan pesanan yang lebih spesifik dibandingkan 
        delete_reset(), yaitu untuk menghapus seluruh pesanan (mengosongkan list pesanan),
        dengan cara mengosongkan list nama, list pesanan, list harga dan 
        list subtotal item pesanan, sesuai petunjuk dan validasi data yang tersedia 
        sehingga didapat data yang sesuai dan valid."""

        print("Pesanan anda saat ini:")
        dict_transaksi = {'Item Name' : list_name,
                          'Item Qty': list_qty,
                          'Item Price': list_price,
                          'subtotal' : list_subtotal}
        
        tabel_transaksi = pd.DataFrame(dict_transaksi)
        print(tabel_transaksi)

        while True:
            try : 
                cek_reset = (input("Apakah Anda ingin menghapus semua pesanan ? (yes/no)")).lower()
                if cek_reset == "yes":
                    list_name.clear()
                    list_qty.clear()
                    list_price.clear()
                    list_subtotal.clear()

                    dict_transaksi = {'Item Name' : list_name,
                                    'Item Qty': list_qty,
                                    'Item Price': list_price,
                                    'subtotal' : list_subtotal}
                    tabel_transaksi = pd.DataFrame(dict_transaksi)

                    print(tabel_transaksi) # menampilkan tabel pesanan setelah direset
                    print("Pesanan Anda telah dihapus silahkan belanja kembali!.")
                    break;

                elif cek_reset == "no":
                    print("silahkan lakukan pembayaran atau proses lainnya!.")
                    break;

                else :
                    print("Inputan Salah, silahkan input ulang!")
                   
            except ValueError:
                continue

         
    def check_discount(self):
        """" Method ini untuk mengecek diskon, sehingga pelanggan bisa memeriksa 
        dapat diskon atau tidak, mengetahui berapa dapat diskonnya, mempertimbangkan 
        menambah pesanan untuk mendapatkan diskon sebelum check out pesanan"""
        
        
        while True:
            try :
                kode_check = input("Apakah Anda ingin memeriksa diskon ? (yes/no/cancel)")
                if kode_check == "yes":
                    print("Ketentuan diskon:")
                    print("bila belanja > Rp 200.000 mendapat diskon sebesar 5%")
                    print("bila belanja > Rp 300.000 mendapat diskon sebesar 8%")
                    print("bila belanja > Rp. 500000 mendapat diskon sebesar 10%")
                    print("==========================================")
                    payment = sum(list_subtotal)

                    if payment > 500_000:
                        discount1 = int(payment*0.1)
                        print(f"Total harga pesanan Anda adalah: Rp {payment}.\nAnda mendapatkan diskon sebesar 10% = Rp {discount1}")
                        break
                    
                    elif payment > 300_000:
                        discount2 = int(payment*0.08)
                        print(f"Total harga pesanan Anda adalah: Rp {payment}.\nAnda mendapatkan diskon sebesar 8% = Rp {discount2}")
                        break
                    
                    elif payment > 200_000:
                        discount3 = int(payment*0.05)
                        print(f"Total harga pesanan Anda adalah: Rp {payment}.\nAnda mendapatkan diskon sebesar 5% = Rp {discount3}")
                        break

                    else:
                        print(f"Total harga pesanan Anda adalah: Rp {payment}.\nAnda tidak mendapatkan diskon.")
                        break

                elif kode_check == "no":
                    break
                    
                elif kode_check == "cancel":
                    sys.exit("Pembatalan Proses...")  
                    
                else :
                    print("Kode yang diinput salah, silahkan input ulang!")
                break;
                
            except ValueError:
                continue


    def check_out(self):
        """" Method ini untuk melakukan check out atau pembayaran, selain itu tersedia opsi 
        cancel bila mau membatalkan pesanan dan no sebagai opsi untuk ke proses selanjutnya,
        bila salah input data muncul warning dan diminta input ulang sampai datanya valid,
        dalam resi pembayaran ditampilkan nama, jumlah, harga, subtotal harga item pesanan, 
        total harga pesanan, diskon dan total harga setelah diskon."""    
        
         
        while True:
            try :
                kode_check = input("Apakah Anda ingin membayar pesanan anda ? (yes/no/cancel)")

                if kode_check == "yes":
                    dict_transaksi = {'Item Name' : list_name,
                                        'Item Qty': list_qty,
                                     'Item Price': list_price,
                                        'subtotal' : list_subtotal}
        
                    tabel_transaksi = pd.DataFrame(dict_transaksi)
                    print(tabel_transaksi)

                    payment = sum(list_subtotal)

                    if payment > 500_000:
                        discount = int(payment*0.1)

                    elif payment > 300_000:
                        discount = int(payment*0.08)

                    elif payment > 200_000:
                        discount = int(payment*0.05)

                    else:
                        discount = 0

                    total_payment = int(payment - discount)
                    persen_discount = round((discount/payment)*100)

                    print(f"Total harga pesanan anda adalah: Rp {payment}")

                    if discount > 0:
                        print (f"Anda mendapatkan diskon sebesar {persen_discount}% = Rp {discount}")
                    
                    else:
                        print ("Anda tidak mendapatkan diskon.")
                    
                    print (f"Total pembayaran adalah: Rp {total_payment}")
                    print ("Terima Kasih sudah berbelanja di Supermarket kami.")
                    break;

                elif kode_check == "no":
                    break
                    
                elif kode_check == "cancel":
                    sys.exit("Pembatalan Proses...")  
                    
                else :
                    print("Kode yang diinput salah, silahkan input ulang!")

            except ValueError:
                continue




