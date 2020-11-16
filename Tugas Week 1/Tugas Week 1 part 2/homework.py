def half_pyramid_pattern(rows):
    for i in range(rows):
        for j in range(i+1):
            print("*",end=" ")
        print("")

def half_pyramid_pattern_inverted(rows):
    for i in range(rows,0,-1):
        for j in range(0,i):
            print("*",end=" ")
        print("")

def half_pyramid_pattern_mirrored(rows):
    for i in range(rows):
        for j in range(rows,0,-1):
            if j > i+1:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        print("")
def full_pyramid_pattern(rows):
    for i in range(rows):
        for j in range(rows-1,i,-1):
            print(end=" ")
        for k in range(0,i+1):
            print("*",end=" ")
        print("")
    
def full_pyramid_pattern_inverted(rows):
    for i in range(rows):
        for j in range(i):
            print(end=" ")
        for k in range(0,rows-i):
            print("*",end=" ")
        print("")
    
def print_pattern(pattern,row):
    if pattern == 1:
        half_pyramid_pattern(row)
    elif pattern == 2:
        half_pyramid_pattern_inverted(row)
    elif pattern == 3:
        half_pyramid_pattern_mirrored(row)
    elif pattern == 4:
        full_pyramid_pattern(row)
    elif pattern == 5:
        full_pyramid_pattern_inverted(row)
    else:
        print("Jenis Pattern tidak diketahui")

#¯\_(ツ)_/¯
def tampil_menu_segitiga():
    print('1.Half Pyramid Pattern')
    print('2.Half Pyramid Pattern Inverted')
    print('3.Half Pyramid Pattern Mirrored')
    print('4.Full Pyramid Pattern')
    print('5.Full Pyramid Inverted Pattern')

tampil_menu_segitiga()
pattern = int(input('Pilih jenis pattern \t: '))
row = int(input('Pilih banyak baris \t: '))
print('===============================')
print_pattern(pattern,row)

"""
while version
def half_pyramid_pattern(rows):
    i = 0
    while i < rows:
        j = 0
        while j < i+1:
            print("*",end=" ")
            j += 1
        print("")
        i += 1

def half_pyramid_pattern_inverted(rows):
    i = 0
    while i < rows:
        j = 0
        while rows > j:
            print("*",end=" ")
            j += 1
        print("")
        rows -= 1

def half_pyramid_pattern_mirrored(rows):
    i = 0 
    while i < rows:
        j = 0
        x = rows
        while x > j:
            if x > i+1:
                print(" ", end=" ")
            else:
                print("*", end=" ")
            x -= 1
        i += 1
        print("")
        
def full_pyramid_pattern(rows):
    i = 0
    while i < rows:
        j = rows-1
        while j > i:
            print(end=" ")
            j -= 1
        x = 0
        while x <= i:
            print("*",end=" ")
            x += 1
        print("")
        i += 1

def full_pyramid_pattern_inverted(rows):
    i = 0
    while i < rows:
        j = 0
        while j < i:
            print(end=" ")
            j += 1
        k = i
        while k < rows:
            print("*",end=" ")
            k += 1
        print("")
        i += 1
"""
#maaf saya masih menggunakan while , di for masih bingung hehe.