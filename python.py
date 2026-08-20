notlar = [45, 78, 92, 30, 55, 60, 40] 
gecenler = list(filter(lambda n: n >= 50, notlar))
ikiKati = list(map(lambda n: n * 2, gecenler))


print("Geçenlerin notları:", gecenler)
