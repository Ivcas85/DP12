from math import pi
class Tvary:
    def rozdil_obsahu(self,tvar_druhy):
        return self.obsah() - tvar_druhy.obsah()

class Ctverec(Tvary):
    def __init__(self,strana):
        self.strana = strana

    def obvod(self):
        return self.strana*4

    def obsah(self):
        return self.strana**2

class Kruh(Tvary):
    def __init__(self,polomer):
        self.polomer = polomer

    def obvod(self):
        return self.polomer*2*pi

    def obsah(self):
        return pi*self.polomer**2


class Obdelnik(Tvary):
    def __init__(self,strana_a,strana_b):
        self.strana_a = strana_a
        self.strana_b = strana_b

    def obvod(self):
        return 2*(self.strana_a+self.strana_b)

    def obsah(self):
        return self.strana_a*self.strana_b

ctverec_prvni=Ctverec(9)
ctverec_druhy=Ctverec(3)
kruh_prvni=Kruh(9)
kruh_druhy=Kruh(3)
obdelnik_prvni=Obdelnik(9,6)
obdelnik_druhy=Obdelnik(6,3)



print(obdelnik_prvni.rozdil_obsahu(kruh_prvni))
