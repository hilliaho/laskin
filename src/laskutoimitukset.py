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
        pino = []
        if len(lauseke)>2:
            if lauseke[1] not in self.numerot:
                pino.append(0)
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
                arvo = self.muuttujat.arvo(operandi)
                pino.append(arvo)

        return pino[-1]
