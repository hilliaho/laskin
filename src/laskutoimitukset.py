class Laskutoimitukset():
    """Luokka, joka vastaa laskutoimituksista
    """

    def __init__(self, muuttujat, numerot, kirjaimet, operaattorit):
        self.muuttujat = muuttujat
        self.numerot = numerot
        self.kirjaimet = kirjaimet
        self.operaattorit = operaattorit

    def _suorita_laskutoimitus(self, luku_1, luku_2, operaattori):
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
                elif merkki[0] in self.numerot:
                    pino.append(float(merkki))
                elif merkki[0] in self.kirjaimet:
                    if self.muuttujat.onko_muuttuja_olemassa(merkki) is False:
                        return "muuttujaa ei ole määritelty"
                    pino.append(self.muuttujat.muuttujat[merkki])
            return pino[-1]
        except IndexError:
            return "virheellinen syöte"
