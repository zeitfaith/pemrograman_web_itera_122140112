# main.py

import math_operations as mo
from math_operations import celsius_ke_kelvin, luas_lingkaran

# Geometri
print("Luas persegi sisi 4:", mo.luas_persegi(4))
print("Keliling persegi:", mo.keliling_persegi(4))

print("Luas persegi panjang 5x3:", mo.luas_persegi_panjang(5, 3))
print("Keliling persegi panjang:", mo.keliling_persegi_panjang(5, 3))

print("Luas lingkaran jari 7:", luas_lingkaran(7))
print("Keliling lingkaran:", mo.keliling_lingkaran(7))

# Konversi suhu
print("25°C ke Fahrenheit:", mo.celsius_ke_fahrenheit(25))
print("25°C ke Kelvin:", celsius_ke_kelvin(25))
