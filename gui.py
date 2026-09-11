import tkinter as tk

def buton_tiklandi():
    print("Buton tıklandı!")

def isim_goster():
    isim = giris.get()
    print(f"İsminiz: {isim}")

def mesaj_degistir():
    etiket.config(text="Butona tıklandı!")

pencere = tk.Tk()

etiket = tk.Label(pencere, text="adınız:")
etiket.grid(row=0, column=0)

giris = tk.Entry(pencere)
giris.grid(row=0, column=1)

pencere.title("Merhaba Dünya")
pencere.geometry("600x400")

pencere.mainloop()