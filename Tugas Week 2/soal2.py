# Melakukan Input untuk club
A = input('Klub A : ')
B = input('Klub B : ')

# Membuat Array
arr = []

i = 1 

# Input Pertama
siA,siB = input(f'Pertandingan {i} : ').split()
siA = int(siA)
siB = int(siB)

# Melakukan pengecekan untuk inputan dan setelah itu melakukan perulangan 
while (siA) >= 0 and (siB) >= 0:
    # Percabangan dan hasilnya dimasukan kedalam array
    if siA > siB:
        arr.append(A)
    elif siA < siB:
        arr.append(B)
    else:
        arr.append('Draw')
    i += 1
    # Melakukan input lagi
    siA,siB = input(f'Pertandingan {i} : ').split()
    siA = int(siA)
    siB = int(siB)

# Print Array
x = 1
for i in arr:
    print(f'Hasil ke {x} : {i}')
    x += 1

print('Pertandingan Seleai')    