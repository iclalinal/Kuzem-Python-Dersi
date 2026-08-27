import os

print(os.getcwd())
print(os.listdir())

if os.path.exists("hesaplamalar.py"):
    print("hesaplamalar.py dosyası mevcut.")
else:
    print("hesaplamalar.py dosyası mevcut değil.")