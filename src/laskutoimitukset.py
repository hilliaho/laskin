class Laskutoimitukset():
    """Luokka, joka vastaa laskutoimituksista
    """

    def laske(self, lauseke):
        """Laskee matemaattisen lausekkeen arvon

        Args:
            lauseke (lista): matemaattinen lauseke

        Returns:
            tulos (liukuluku): laskettu lausekkeen arvo
        """
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
            else:
                pino.append(float(operandi))

        return pino[-1]
