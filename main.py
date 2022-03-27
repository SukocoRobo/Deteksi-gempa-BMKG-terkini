"""
Aplikasi deteksi gempa terkini
"""
import gempaTerkini as Gt

if __name__ == '__main__':
    print('Aplikasi utama')
    result = Gt.ekstraksi_data()
    Gt.tampilkan_data(result)
