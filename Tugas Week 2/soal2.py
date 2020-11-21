# Melakukan Input untuk club
klub_a = input('Klub A : ')
klub_b = input('Klub B : ')

# Membuat Array
arr = []

i = 1 

# Input Pertama
si_a,si_b = input(f'Pertandingan {i} : ').split()
si_a = int(si_a)
si_b = int(si_b)

# Melakukan pengecekan untuk inputan dan setelah itu melakukan perulangan 
while (si_a) >= 0 and (si_b) >= 0:
    # Percabangan dan hasilnya dimasukan kedalam array
    if si_a > si_b:
        arr.append(klub_a)
    elif si_a < si_b:
        arr.append(klub_b)
    else:
        arr.append('Draw')
    i += 1
    # Melakukan input lagi
    si_a,si_b = input(f'Pertandingan {i} : ').split()
    si_a = int(si_a)
    si_b = int(si_b)

# Print Array
x = 1
for i in arr:
    print(f'Hasil ke {x} : {i}')
    x += 1

print('Pertandingan Seleai')    
