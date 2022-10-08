class Laskutoimitukset():
    """Luokka, joka vastaa laskutoimituksista
    """

    def __init__(self, muuttujat, numerot, kirjaimet):
        self.muuttujat = muuttujat
        self.numerot = numerot
        self.kirjaimet = kirjaimet

    def laske(self, lauseke):
        """Laskee matemaattisen lausekkeen arvon

        Args:
            lauseke (lista): matemaattinen lauseke

        Returns:
            tulos (liukuluku): laskettu lausekkeen arvo
        """
        try:
            pino = []
            for operandi in lauseke:
                if operandi in ("+", "-", "*", "/", "^"):
                    eka = pino.pop()
                    toka = pino.pop()
                    if operandi == "+":
                        tulos = eka + toka
                    elif operandi == "-":
                        tulos = toka - eka
                    elif operandi == "*":
                        tulos = eka * toka
                    elif operandi == "/":
                        tulos = toka / eka
                    elif operandi == "^":
                        tulos = toka**eka
                    pino.append(tulos)
                elif operandi[0] in self.numerot:
                    pino.append(float(operandi))
                elif operandi[0] in self.kirjaimet:
                    if self.muuttujat.onko_muuttuja_olemassa(operandi)==False:
                        return
                    else:
                        pino.append(self.muuttujat.muuttujat[operandi])
            return pino[-1]
        except:
            return "error"
