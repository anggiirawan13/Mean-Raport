import functions as fungsi

while True:
    try:
        fungsi.logo()
        fungsi.Menu()
        fungsi.Hitung()
        print('=' * 50)

    except ValueError:
        print('=' * 50)
        print('Maaf, Yang Anda Masukan Bukan Angka.')
        print('=' * 50)

    __userAgain = input('Apakah Anda Ingin Menghitung Ulang ? ( Y / N ) : ')
    if __userAgain == 'y' or __userAgain == 'Y':
        continue
    elif __userAgain == 'n' or __userAgain == 'N':
        break
    else:
        print('=' * 50)
        print('Maaf, Kata Kunci Yang Anda Masukan Salah.')
        break

print('=' * 50)
print('TERIMA KASIH')
