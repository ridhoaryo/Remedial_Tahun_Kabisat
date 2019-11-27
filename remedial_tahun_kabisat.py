def div_4(tahun):
    if tahun%4 == 0:
        print('TAHUN KABISAT')
    else:
        print('BUKAN TAHUN KABISAT')

div_4(int(input('Input tahun: ')))