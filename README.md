# Python Project Super Cashier
Sebuah project pembuatan program _self services cashier_ menggunakan bahasa pemrograman python.
## 1. latar Belakang
Andi sebagai pemilik sebuah supermarket besar di salah satu kota di Indonesia ingin melakukan suatu _improvement_ 
pada supermarketnya yaitu dengan membuat suatu program _self service cashier_. 
Sehingga pelanggan yang jauh dari lokasi supermarketnya bisa belanja swalayan di rumahnya masing-masing.
Untuk merealisasikan tujuannya Andi membutuhkan program _developer_ untuk membuat 
program _**Super Cashier**_ yang mempunyai fitur-fitur belanja seperti input sendiri barang belanjaannya, 
memeriksa dan mengubah barang belanjaannya, sampai dengan melakukan pembayaran. 
## 2. Tujuan
Membuat program _self service cashier_ yang memenuhi fitur-fitur yang dibutuhkan _customer_.
Adapun _Feature Requirements_ tersebut mencakup:
1. Membuat Id Transaksi yang bisa digunakan untuk melakukan proses belanja _customer_.
2. Membuat fungsi transaksi untuk menambahkan/menginput daftar belanja _customer_.
3. Membuat fungsi memperbaiki item pesanan apabila ada kesalahan input nama/jumlah/harga.
4. Membuat fungsi menghapus sebagian item pesanan atau seluruh pesanan.
5. Membuat fungsi transaksi untuk melakukan pengecekkan pesanan.
   a. Bila pesanan sudah benar maka ada output "pesanan sudah benar".
   b. Bila pesanan masih ada yang salah maka ada output "terdapat kesalahan input data".
   c. _Customer_ bisa melihat daftar belanja yang akan dibayar
7. setelah semua benar customer bisa melakukan pengecekkan total harga, diskon 
   dan jumlah total yang harus dibayarkan.
8. fitur lain yang mendukung.
## 3.  Alur Proses Pengaplikasian Program
Alur Proses Pelaksanaan belanja menggunakan program Super Cashier adalah sebagai berikut:
![flowchart super cashier](https://github.com/indra2878/Python-Project-Super-Cashier/assets/129472057/271ebded-320e-4d75-8d54-acf126489b7c)
## 4. Penjelasan Kode
1. <b>Modul pandas</b> : untuk pembuatan dataframe 
2. <b>Modul sys</b> : untuk membuat sistem exit program.
3. <b>create_id()</b>: function untuk membuat id transaksi. 
4. <b>transaction_id = create_id</b> ; mendefinisikan <b>transaction_id</b> sebagai id transaksi yang sebelumnya dibuat
5. <b>transaction_id = Transaction()</b> ; mendefinisikan id transaksi sebagai object dari <b>Class Transaction()</b> 
6. <b>Class Transaction</b> : menampung semua method untuk menjalankan proses-proses transaksi
7. <b>add_item()</b>:
Method ini untuk membeli/menambah item pesanan mencakup input nama, jumlah dan 
harga item pesanan, sesuai petunjuk/ ketentuan penginputan yang tersedia 
sehingga didapat data yang sesuai dan valid. jika kode yang dimasukan salah maka user 
diminta validasi kode hingga benar dan jika tidak ingin menambah item dapat pilih "no" 
lalu proses berhenti. Inputan dimasukan ke dalam list yang sudah disediakan, lalu
list tersebut dibuat ke dalam dictionary dan mengubahnya ke dalam bentuk dataframe.
8. <b>check_order()</b>:
Method ini untuk memeriksa pesanan pelanggan, berupa tabel 
sehingga pelanggan bisa memeriksa nama, jumlah, harga item pesanannya 
dan menentukan opsi proses selanjutnya. Didalamnya terdapat opsi "yes" 
untuk memeriksa dan menampilkan tabel pesanan yang diinput sebelumnya, 
"no" untuk tdak melakukan apa-apa dan melakukan proses selanjutnya, 
"cancel" untuk membatalkan proses transaksi dan keluar dari program.
9. <b>update_item()</b>:
Method ini untuk mengubah data pesanan hasil inputan pelanggan, 
sehingga pelanggan bisa mengubah nama, jumlah, harga item pesanannya 
sesuai opsi yang tersedia beserta data validasinya sehingga didapat
data yang sesuai dan valid. Di awal disediakan opsi "yes" untuk mengubah data pesanan,
dan "no" untuk tidak melakukan perubahan dan lanjut ke proses selanjutnya.
customer bisa memilih opsi 1: untuk mengubah nama item, opsi 2: untuk mengubah jumlah item 
dan opsi 3: untuk mengubah harga item. Pada masing opsi di uji validitas datanya, 
bila ada kesalahan pada nama item yang akan diubah, maka muncul warning dan diminta input ulang 
sampai valid, untuk jumlah dan harga item data yang dimasukkan harus berupa angka bila salah maka
muncul warning dan diminta input ulang sampai valid.
10. <b>update_item_name()</b>:
Merupakan method opsional perubahan item yang lebih spesifik dibandingkan update_item().
Method ini khusus untuk mengubah nama item pesanan, sesuai petunjuk/ ketentuan penginputan 
yang tersedia sehingga didapat data yang sesuai dan valid. Di awal disediakan opsi "yes" 
untuk mengubah data pesanan, dan "no" untuk tidak mengubah item dan lanjut ke proses selanjutnya.
bila ada kesalahan pada nama item yang akan diubah, maka muncul warning dan diminta input ulang 
sampai valid, untuk jumlah dan harga item data yang dimasukkan harus berupa angka bila salah maka
muncul warning dan diminta input ulang sampai valid.
11. <b>update_item_qty()</b>:
Merupakan method opsional perubahan item yang lebih spesifik dibandingkan update_item().
Method ini khusus untuk mengubah jumlah item pesanan, sesuai petunjuk/ ketentuan penginputan
yang tersedia sehingga didapat data yang sesuai dan valid.Di awal disediakan opsi "yes" 
untuk mengubah data pesanan, dan "no" untuk tidak mengubah item dan lanjut ke proses selanjutnya.
bila ada kesalahan pada nama item yang akan diubah, maka muncul warning dan diminta input ulang 
sampai valid, untuk jumlah dan harga item data yang dimasukkan harus berupa angka bila salah maka
muncul warning dan diminta input ulang sampai valid.
12. <b>update_item_price()</b>:
Merupakan method opsional perubahan item yang lebih spesifik dibandingkan update_item().
Method ini khusus untuk mengubah harga item pesanan, sesuai petunjuk/ ketentuan penginputan
yang tersedia sehingga didapat data yang sesuai dan valid.Di awal disediakan opsi "yes" 
untuk mengubah data pesanan, dan "no" untuk tidak mengubah item dan lanjut ke proses selanjutnya.
bila ada kesalahan pada nama item yang akan diubah, maka muncul warning dan diminta input ulang 
sampai valid, untuk jumlah dan harga item data yang dimasukkan harus berupa angka bila salah maka
muncul warning dan diminta input ulang sampai valid.
13. <b>delete_reset()</b>:
Method ini untuk menghapus pesanan dari daftar belanja  (1 baris belanjaan) Di awal disediakan 
opsi "yes" untuk menghapus pesanan, dan "no" untuk tidak menghapus pesanan dan lanjut ke proses 
selanjutnya. Ada 2 opsi penghapusan: 1. menghapus sebagian  pesanan, 2. menghapus seluruh pesanan 
(mengosongkan daftar belanja), nama item dijadikan data acuan untuk melakukan proses penghapusan
bila ada kesalahan pada nama item yang akan dihapus, maka muncul "warning" dan diminta input ulang 
sampai valid, untuk jumlah dan harga item data yang dimasukkan harus berupa angka bila salah maka
muncul "warning" dan diminta input ulang sampai valid.
14. <b>delete_item()</b>:
Method ini untuk penghapusan pesanan yang lebih spesifik dibandingkan <b>delete_reset()</b>, 
yaitu untuk menghapus sebagian pesanan (1 baris dalam tabel pesanan), sesuai petunjuk 
dan validasi data yang tersedia sehingga didapat data yang sesuai dan valid.
15. <b>reset_order()</b>:
 Method ini untuk penghapusan pesanan yang lebih spesifik dibandingkan 
 <b>delete_reset()</b>, yaitu untuk menghapus seluruh pesanan, dengan cara mengosongkan 
 list nama, list pesanan, list harga dan list subtotal item pesanan,
 sesuai petunjuk dan validasi data yang tersedia sehingga didapat data yang sesuai 
 dan valid.
16. <b>check_discount()</b>:
Method ini untuk mengecek diskon, sehingga pelanggan bisa memeriksa 
dapat diskon atau tidak, mengetahui berapa dapat diskonnya, mempertimbangkan 
menambah pesanan untuk mendapatkan diskon sebelum check out pesanan.
17. <b>check_out()</b>:
Method ini untuk melakukan check out atau pembayaran, selain itu tersedia opsi 
cancel bila mau membatalkan pesanan dan no sebagai opsi untuk ke proses selanjutnya, 
bila salah input data muncul warning dan diminta input ulang sampai datanya valid,
dalam resi pembayaran ditampilkan nama, jumlah, harga, subtotal harga item pesanan, 
total harga pesanan, diskon dan total harga setelah diskon.

Untuk lebih jelas mengenai pengaplikasian kode-kode diatas dapat dilihat pada file jupiter notebook
"super cashier fitur requirement dan test case".

## 5. Hasil Test Case
1. Menambah 2 (dua) item baru menggunakan method add_item().
nama item: Ayam Goreng, Qty: 2 Harga: 20000
nama item: Pasta Gigi, Qty: 2 Harga: 15000

output:

![test case 1 add item](https://github.com/indra2878/Python-Project-Super-Cashier/assets/129472057/f3fe399a-ad9b-4f1b-865e-5096f613cfa2)

2. Menghapus salah satu item pesananan menggunakan method delete_item().
item yang ingin dihapus: Pasta Gigi.
output:

![test case 2 delete item](https://github.com/indra2878/Python-Project-Super-Cashier/assets/129472057/c18dc2be-03b2-4223-9393-67e5f3ca8bda)

3. Menghapus semua item yang ditambahkan sebelumnya menggunakan method reset_order().
output:

![test case 3 reset order](https://github.com/indra2878/Python-Project-Super-Cashier/assets/129472057/86593995-5355-43ca-874f-6decf1427217)

4. Menghitung total harga belanjaan, menampilkan daftar belanjaannya dengan method check_out().
output:

![test case 4 check out](https://github.com/indra2878/Python-Project-Super-Cashier/assets/129472057/94bb1724-2b8c-4572-916c-f30a3e57589f)

untuk lebih jelasnya lihat file jupiter notebook "super cashier fitur requirement dan test case".
## 6. Kesimpulan
Program Super Cashier sederhana yang dibuat dengan bahasa pemrograman python ini
telah mampu memenuhi feature requirements dan menjawab test case test case yang umumnya ada.
Program Super Cashier ini pengolahan datanya berdasarkan pada sistem pengolahan data berupa list,  
sehingga dimungkinkan berbeda pengkodeannya pada pengolahan data berupa dictionary.
Sistem validasi data pada program ini berjalan dengan baik sehingga memungkinkan customer menginput data yang sesuai dan valid.

## 7. Saran
Perlu ditinjau lagi mengenai keefisienan kode-kode yang dibuat dalam memenuhi fitur-fitur yang dibutuhkan.
Untuk pengembangan lebih lanjut agar bisa diaplikasikan dengan nyaman oleh user (user friendly) perlu dibuat versi GUI nya.
