import math

class Laskutoimitukset():
    """Luokka, joka vastaa laskutoimituksista
    """

    def __init__(self, muuttujat, numerot, kirjaimet, operaattorit):
        self.muuttujat = muuttujat
        self.numerot = numerot
        self.kirjaimet = kirjaimet
        self.operaattorit = operaattorit

    def laske(self, lauseke):
        """Laskee matemaattisen lausekkeen arvon

        Args:
            lauseke (lista): matemaattinen lauseke

        Returns:
            tulos (liukuluku): laskettu lausekkeen arvo
        """
        try:
            pino = []
            for merkki in lauseke:
                if merkki in ("+", "-", "*", "/", "^"):
                    eka = pino.pop()
                    toka = pino.pop()
                    tulos = self._suorita_laskutoimitus(eka, toka, merkki)
                    pino.append(tulos)
                elif merkki in ("sin", "cos", "tan", "asin", "acos", "atan"):
                        luku = pino.pop()
                        tulos = self._suorita_laskutoimitus(luku,0,merkki)
                        pino.append(tulos)
                elif merkki[0] in self.numerot:
                    if "." in merkki:
                        pino.append(float(merkki))
                    else:
                        pino.append(int(merkki))
                elif merkki[0] in self.kirjaimet:
                    if self.muuttujat.onko_muuttuja_olemassa(merkki) is False:
                        return "virheellinen syöte"
                    pino.append(self.muuttujat.muuttujat[merkki])
            return pino[-1]
        except IndexError:
            return "virheellinen syöte"

    def _suorita_laskutoimitus(self, luku_1, luku_2, operaattori):
        try:
            if operaattori == "+":
                return luku_2 + luku_1
            if operaattori == "-":
                return luku_2 - luku_1
            if operaattori == "*":
                return luku_2 * luku_1
            if operaattori == "/":
                return luku_2 / luku_1
            if operaattori == "^":
                return luku_2**luku_1
            if operaattori == "sin":
                if luku_1%math.pi==0:
                    return 0
                return math.sin(luku_1)
            if operaattori == "cos":
                if luku_1%math.pi==math.pi/2:
                    return 0
                return math.cos(luku_1)
            if operaattori == "tan":
                return math.tan(luku_1)
            if operaattori == "asin":
                return math.asin(luku_1)
            if operaattori == "acos":
                return math.acos(luku_1)
            if operaattori == "atan":
                return math.atan(luku_1)
        except ValueError:
            return "virheellinen syöte"
        except ZeroDivisionError:
            return "virheellinen syöte"

