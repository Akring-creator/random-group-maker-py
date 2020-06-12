import random as rd

kelas = [
'Muhammad Rizky Juniarto', 'Raisa Putri Sekar Arum', 
'Muhammad Fahrul Ramadhan', 'Aylika Rizkia Putri',
'Stefan Primananda', 'Wildan Zidan Ramadhan', 
'Siti Nur Vauziyah', 'Adila Fitriani', 'Dwi Larasaty',
'Nadira Novitasari', 'Elbarra Gifary B', 'Ivan T Akbar', 
'Muh Fathan Roy', 'Zahra Hasna', 
'Desy Natalia', 'Isma Khoirunnisa', 'Eirene', 
'Aldi Dwi Cahyo', 'Lelining Tias', 
'Oriza Sotifa', 'Luthfiyah Aulia', 'Fika Auliana', 
'Alifia Nur Annisa', 'Sahla Azkiya', 
'Nabila Siti Mardiah', 'Wahyu Rahmatulloh', 'Aliya Yamin', 
'Gunawan W', 'Nur Achmad Subchi', 
'Mararosa F', 'M Ilham', 'Rizky R N', 'M Akmalul Iman L',
'Yohanna F M', 'Alliqa Dafa', 'M Alfathan', 
'Ibnu Abdillah', 'Salwaa R', 'Mayang Indriati', 
'Sherina Atika Citra', 'Karliana Ageng Wahyuni',
'Haikal Amjad', 'Miswa Kamila', 'Bayu Widodo', 
'Haura LZSL', 'Alfin Diaz Fadhila', 'Tarisa Maharani', 
'Desi Fitriani', 'Lathifa Zahrah'
]

# print(kelas.index("Lathifa Zahrah"))
angka = []
for num in range (0, len(kelas)): angka.append(num)
# print (len(angka))

total = int(input(" Berapa Kelompok : "))
kel = []
for x in range(total):
    sub= []
    kel.append(sub)

count = 0
while len(angka) > 0:

    acak = rd.randint(0, len(angka)-1)
    hasil = angka[acak]
    # print(hasil)
    del (angka[acak])

    kel[count].append(kelas[hasil])
    if count == len(kel)-1: 
        count = 0
    else: 
        count+=1

# print(kel)
nm = total-1
for kel_sub in kel:
    print("\n")
    print(f".:Kelompok {total-nm}:.")
    for name in kel_sub:
        print(f"{name}")
    nm = nm - 1
