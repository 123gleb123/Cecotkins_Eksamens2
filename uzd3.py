text = input("Ievadi tekstu: ")
vowels = "aāeēiīouū"
count = 0

for char in text.lower():
    if char in vowels:
        count += 1

print("Garsu skaits:", count)
