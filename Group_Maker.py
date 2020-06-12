import random as rd

kelas = ["Udin", "Ucup", "Feby"
]
angka = []
for num in range (0, len(kelas)): angka.append(num)

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

nm = total-1
for kel_sub in kel:
    print("\n")
    print(f".:Kelompok {total-nm}:.")
    for name in kel_sub:
        print(f"{name}")
    nm = nm - 1
