import random

def istatistik_hesapla(*notlar):
    return min(notlar), max(notlar), sum(notlar) / len(notlar)

def random_uret(adet):
    return [random.randint(0, 100) for _ in range(adet)]