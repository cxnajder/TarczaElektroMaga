import math


czestotliwosc = 4.48 #GHz
dlugoscFali = 299.792458 / (czestotliwosc * 1000) #m
print(f"f = {czestotliwosc}GHz")
print(f"lambda = {dlugoscFali}m")
print(f"lambda = {dlugoscFali * 100}cm")

print("=" * 25)

class Prostokat:
    def __init__(self, x, y):
        self.x = x   #cm
        self.y = y #cm
        self.z = math.sqrt(pow(x, 2) + pow(y, 2))   # przekatna

class Przeslona:
    def __init__(self, x, y, wyciecie, przerwa):
        self.x = x #cm
        self.y = y #cm
        self.wyciecie = wyciecie
        self.przerwa=przerwa

        self.__ileWyciecY = int(self.y / (wyciecie.y + przerwa)) #sprawdzam ile otworow sie miesci w rzedzie - zakladam ze mniezy otworami bedzie przerwa wielkosci lambda
        self.__ileWyciecX = int(self.x / (wyciecie.x + przerwa))

        self.ileWyciec = self.__ileWyciecY * self.__ileWyciecX

        self.powWyciec = wyciecie.x * wyciecie.y * self.ileWyciec   #powierzchnia wyciec

        if przerwa >= dlugoscFali * 100:
            self.S = 20 * math.log(dlugoscFali * 100 / 2 * wyciecie.z) # dla odleglosi miedzy otoworami >= lambda
        elif przerwa >= dlugoscFali * 100 / 4:
            self.S = 20 * math.log(dlugoscFali * 100 / 2 * wyciecie.z) - 20 * math.log(math.sqrt(self.ileWyciec)) # dla odleglosci miedzy otworami < lambda i >= lambda/4




def tabela(przerwa_miedzy_wycie, x_start, stusunek_xy):

    x = x_start #cm
    y = x * stusunek_xy
    while(math.sqrt(pow(x, 2) + pow(y, 2)) <= dlugoscFali * 100 * 2):
        prostokat = Prostokat(x, y)
        przeslona = Przeslona(50, 50, prostokat, przerwa_miedzy_wycie)
        if przeslona.ileWyciec <= 0:
            break
        print(f"przerwa = {przeslona.przerwa} cm", f"x = {prostokat.x} cm", f"y = {round(prostokat.y, 3)} cm", f"n = {przeslona.ileWyciec}", f"pow = {round(przeslona.powWyciec, 2)} cm^2", f"S = {round(przeslona.S, 2)} dB", sep = "; \t")
        x += 0.1
        x = round(x, 1)
        y = x * 3/4


bok_x =0.5
stosunek_bokow = 3/4

tabela(round(dlugoscFali * 100, 1), bok_x, stosunek_bokow)
print("=" * 25)
tabela(round(dlugoscFali * 100, 1)/ 4, bok_x, stosunek_bokow)