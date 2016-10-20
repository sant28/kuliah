# Ahmad Idham T Lubis
# Sistem & Teknologi Informasi
# Institut Teknologi Bandung

baris = int(input("Masukkan sebuah angka: "))
print
print "Angka tersebut akan menjadi jumlah baris dan kolom"
print

# Inisialisasi

seq = baris/2 # Variabel untuk membatasi panah

# Eksekusi
# Program membentuk panah yang terbuat dari spasi dan bintang
# Program ini dibuat dengan perspektif gambar disusun dari panah spasi yang menunjuk ke kanan dan ke kiri

# Variabel i adalah variabel baris, sedangkan J untuk kolom
# Program bekerja dengan membagi panah menjadi 3 bagian, bagian kiri, tengah, dan kanan
# Variabel tempseq adalah variabel acuan untuk membentuk lambang " " atau "*"
# Nilai tempseq berubah-ubah tiap kolomnya, dan pada tiap kolom akan dibandingkan nilainya dengan i
# Perbandingan antara tempseq dan variabel i menentukan lambang mana yang akan dikeluarkan
# Nilai tempseq mula-ula bertambah, lalu berkurang. Hal ini menggambarkan penambahan lambang " " tiap kolomnya

i = 0
while (i < seq + 1):	# Bagian untuk pengulangan baris
	tempseq = 0
	j = seq
	while (j > 0):	# Untuk Sisi Kiri
		if tempseq<i:
			print " ",
		else :
			print "*",
		tempseq = tempseq + 1
		j = j - 1
	print "*",	# Untuk Tengah
	j, tempseq = seq, tempseq-1	# Untuk Sisi Kanan
	while (j > 0):
		if tempseq<i:
			print " ",
		else :
			print "*",
		tempseq = tempseq - 1
		j = j - 1
	print
	i = i + 1

# Bagian pengulangan berikutnya, setelah hanya ada satu bintang di bagian tengah

i=0			
while (i < seq):
	tempseq = seq - 1	# Bagian Sisi Kiri
	j = 0
	while (j < seq):
		if tempseq>i:
			print " ",
		else :
			print "*",
		tempseq = tempseq-1
		j = j + 1
	print "*",		# Bagian Tengah
	j, tempseq = 0, tempseq+1	# Bagian Sisi Kanan
	while (j < seq):
		if tempseq>i:
			print " ",
		else :
			print "*",
		tempseq = tempseq+1
		j = j + 1
	print
	i = i + 1
print
print "Selamat menikmati ;)"
