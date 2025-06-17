#Uzrakstiet programmu, kas izmanto for ciklu, 
# lai izvadītu lietotāja norādīta skaitļa no 1 līdz 10 (ieskaitot) 
# reizināšanas tabulu. Piemērs: ja tiek ievadīts 3, 
# izvadei jābūt šādai: 3 x 1 = 3, 3 x 2 = 6, ..., 3 x 10 = 30

# Lietotājs ievada skaitli
number = int(input("Ievadi skaitli: "))
# Cikls, kas iet cauri skaitļiem no 1 līdz 10
for i in range(1, 11):
    # Izdrukā reizināšanas tabulas rindu
    print(f"{number} x {i} = {number * i}")