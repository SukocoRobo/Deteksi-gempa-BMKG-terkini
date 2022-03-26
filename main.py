"""
Aplikasi deteksi gempa terkini
"""


def ekstraksi_data():
    """
    Tanggal: 26 Maret 2022
    Waktu : 16:54:31 WIB
    Magnitudo : 4.3
    Kedalaman : 10 km
    Lokasi : 3.83 lat - 122.72 long
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '26 Maret 2022'
    hasil['waktu'] = '16:54:31 WIB'
    hasil['magnitudo'] = 4.3
    hasil['lokasi'] = {'ls': 3.83, 'bt': 122.72}
    hasil['pusat'] = 'Pusat gempa berada di laut 11 km Timur Laut Soropia, Kab. Konawe'
    hasil['dirasakan'] = 'Pusat gempa berada di laut 11 km Timur Laut Soropia, Kab. Konawe'
#    print(hasil)

    return hasil

def tampilkan_data(result):
    print("Gempa Terakhir berdasarkan BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi: LS={result['lokasi']['ls']} - BT={result['lokasi']['bt']}")
#    print(result)


if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
