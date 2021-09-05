"""
Aplication Latest Earthquake Detaction
MODULARISATION WITH FUNCTION
MODULARISATION WITH PACKAGE

"""
# from earthquake_detection import ekstraksi_data, tampilkan_data
import earthquake_detection

if __name__ == "__main__":
    result = earthquake_detection.ekstraksi_data()
    earthquake_detection.tampilkan_data(result)
