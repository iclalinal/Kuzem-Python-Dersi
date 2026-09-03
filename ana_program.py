try:
    with open('ana_program.txt', 'r') as dosya:
        icerik = dosya.read()
except FileNotFoundError:
    with open('ana_program.txt', 'w') as dosya:
        dosya.write("Bu bir dosya oluşturma testi.\n")
