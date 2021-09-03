"""
Aplication Latest Earthquake Detaction
MODULARISATION WITH FUNCTION
"""


def ekstraksi_data():
    """
    Tanggal: 02 September 2021
    Waktu: 07:22:36 WIB
    Magnitudo: 2.7
    Kedalaman: 13 km
    Lokasi: LS=4.01 BT=122.49
    Pusat Gempa: Pusat gempa berada di darat 2.8 Km BaratLaut Baruga
    Dirasakan (Skala MMI): II Kendari
    :return:
    """
    hasil = dict()
    hasil["tanggal"] = "02 September 2021"
    hasil["waktu"] = "07:22:36 WIB"
    hasil["magnitudo"] = 2.7
    hasil["kedalaman"] = "13 km"
    hasil["lokasi"] = {"ls": 4.01, "bt": 122.49}
    hasil["pusat_gempa"] = "Pusat gempa berada di darat 2.8 Km BaratLaut Baruga"
    hasil["dirasakan"] = "II Kendari"


    # print(hasil)
    return hasil


def tampilkan_data(result):
    print("Gempa Terakhir Berdasarkan BMKG")
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Lokasi : LS= {result['lokasi']['ls']}, BT= {result['lokasi']['bt']}")
    print(f"Pusat Gempa : {result['pusat_gempa']}")
    print(f"Dirasakan : {result['dirasakan']}")


if __name__ == "__main__":
    print("Aplikasi utama")
    result = ekstraksi_data()
    tampilkan_data(result)
