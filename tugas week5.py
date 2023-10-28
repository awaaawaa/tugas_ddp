a=1

print(a)

kendaraan = ["Mobil 1", "bmw i7", "bmw", 4396]
    
print(kendaraan)
kendaraan.append("Hitam")
print(kendaraan)
kendaraan.append("4 Roda")
print(kendaraan)
kendaraan.append("52.9M")
print(kendaraan)
kendaraan.remove("bmw i7")
print(kendaraan)
 #Menampilkan data kendaraan
 
print("")

a=2

print(a)

b=input("Mau menghitung bangunan apa?")

match b:
    case "Persegi":
        c= int(input("Berapa Sisinya?"))
        d= c * c
        print(d)
    case "Lingkaran":
        c= int(input ("Berapa Jari-jarinya"))
        d= 2 * 3.14 * c
        print(d)
    case "Segitiga":
        c= int(input("Berapa alasnya?"))
        d= int(input("Berapa tingginya?"))
        e= 0.5 * c * d
        print(e)
    
    
