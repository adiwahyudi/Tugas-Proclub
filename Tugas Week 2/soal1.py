arrBerat = []
bMin = 0
bMax = 0

def hitungMinMax(arrBerat):
    global bMin, bMax
    bMin = min(arrBerat)
    bMax = max(arrBerat)


def rerata(arrBerat):
    total = 0
    total = sum(arrBerat)/len(arrBerat)    
    # Definisikan Proses Mencari Rerata Dari Total Berat
    return total
    # Return Hasil Rerata


print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')
    berat = float(input())
    arrBerat.append(berat)
    # Inisialisasi Input Data Berat
    
    # Masukkan Data Berat Ke Array (arrBerat)

# Panggil procedur hitungMinMax(arrBerat)
hitungMinMax(arrBerat)
print()
# Print Data Minimum, Maximum, dan Rerata Berat
print(f'Berat balita minimum : {bMin} kg')
print(f'Berat balita maximum : {bMax} kg')
print(f'Rerata berat balita : {rerata(arrBerat):.2f} kg')
