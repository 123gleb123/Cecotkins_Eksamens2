#Uzrakstiet programmu, kas izmanto ligzdotus for ciklus, 
# lai izdrukātu taisnstūri ar # simboliem ar lietotāja norādītu platumu un augstumu. 
# Piemēram, ja lietotājs ievada platumu = 5, augstumu = 3, 
# programmai jāizdrukā 3 rindas ar 5 # simboliem katrā.

# Lietotājs ievada taisnstūra platumu
width = int(input("Ievadi platumu : "))
# Lietotājs ievada taisnstūra augstumu
height = int(input("Ievadi augstumu: "))

# Ārējais cikls atkārtojas par katru rindu (augstums)
for _ in range(height):
    row = "" # Sākam ar tukšu rindu
    # Iekšējais cikls pievieno '#' simbolus rindā (platums)
    for _ in range(width):
        row += "#"
    # Izdrukājam vienu rindu
    print(row)