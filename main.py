"""
Aplikasi deteksi gempa terkini
"""
import gempaTerkini as Gt
import bs4
import request

if __name__ == '__main__':
    print('Aplikasi utama')
    result = Gt.ekstraksi_data()
    Gt.tampilkan_data(result)
