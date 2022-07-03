def BuyukCollatz(n):
    sayi = 1
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n +1
        sayi += 1
    return sayi

def MaxUzunCollatz(n):
    max_uzunluk = 0
    for i in range(n):
        if BuyukCollatz(i) > max_uzunluk:
            max_uzunluk = BuyukCollatz(i)
            yeni_sayi = i
    return yeni_sayi

sonuc = MaxUzunCollatz(1000000)
print(sonuc)