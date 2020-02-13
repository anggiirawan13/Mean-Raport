class Menu:
    def __init__(self):
        print('=' * 50)
        print('HITUNG RATA-RATA NILAI SEMESTER')
        print('\t 1. Semester 1')
        print('\t 2. Semester 2')
        print('\t 3. Semester 3')
        print('\t 4. Semester 4')
        print('\t 5. Semester 5')


class Hitung:

    def __init__(self):
        __userInput = input('Masukan Pilihan Semester Anda (1/2/3/4/5) : ')

        if __userInput == '1' or __userInput == '2':
            S12()
        elif __userInput == '3' or __userInput == '4':
            S34()
        elif __userInput == '5':
            S5()
        else:
            print('=' * 50)
            print('Maaf, Kata Kunci Yang Anda Masukan Salah.')


class S12:
    def __init__(self):
        a = float(input('Masukan Nilai Agama : '))
        b = float(input('Masukan Nilai PKN : '))
        c = float(input('Masukan Nilai B. Indonesia : '))
        d = float(input('Masukan Nilai Matematika : '))
        e = float(input('Masukan Nilai Sejarah Indonesia : '))
        f = float(input('Masukan Nilai B. Inggris : '))
        g = float(input('Masukan Nilai Seni Budaya : '))
        h = float(input('Masukan Nilai Olahraga : '))
        i = float(input('Masukan Nilai Simulasi dan Komunikasi Digital : '))
        j = float(input('Masukan Nilai Fisika : '))
        k = float(input('Masukan Nilai Kimia : '))
        z = float(input('Masukan Nilai Sistem Komputer : '))
        m = float(input('Masukan Nilai Komputer dan Jaringan Dasar : '))
        n = float(input('Masukan Nilai Pemrograman Dasar : '))
        o = float(input('Masukan Nilai Dasar Desain Grafis : '))
        print('=' * 50)
        print('Nilai Rata-Rata Anda Adalah =', float(a + b + c + d + e + f + g + h + i + j + k + z + m + n + o) / 15)


class S34:
    def __init__(self):
        a = float(input('Masukan Nilai Agama : '))
        b = float(input('Masukan Nilai PKN : '))
        c = float(input('Masukan Nilai B. Indonesia : '))
        d = float(input('Masukan Nilai Matematika : '))
        e = float(input('Masukan Nilai B. Inggris : '))
        f = float(input('Masukan Nilai Olahraga : '))
        g = float(input('Masukan Nilai Teknologi Jaringan Berbasis Luas : '))
        h = float(input('Masukan Nilai Adm. Infrastruktur Jaringan : '))
        i = float(input('Masukan Nilai Adm. Sistem Jaringan : '))
        j = float(input('Masukan Nilai Teknologi Layanan Jaringan : '))
        k = float(input('Masukan Nilai Produk Kreatif dan Kewirausahaan : '))
        print('=' * 50)
        print('Nilai Rata-Rata Anda Adalah =', float(a + b + c + d + e + f + g + h + i + j + k) / 11)


class S5:
    def __init__(self):
        a = float(input('Masukan Nilai Agama : '))
        b = float(input('Masukan Nilai PKN : '))
        c = float(input('Masukan Nilai B. Indonesia : '))
        d = float(input('Masukan Nilai Matematika : '))
        e = float(input('Masukan Nilai B. Inggris : '))
        f = float(input('Masukan Nilai Adm. Infrastruktur Jaringan : '))
        g = float(input('Masukan Nilai Adm. Sistem Jaringan : '))
        h = float(input('Masukan Nilai Teknologi Layanan Jaringan : '))
        i = float(input('Masukan Nilai Produk Kreatif dan Kewirausahaan : '))
        print('=' * 50)
        print('Nilai Rata-Rata Anda Adalah =', float(a + b + c + d + e + f + g + h + i) / 9)
