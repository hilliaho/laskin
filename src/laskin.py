from kayttoliittyma import Kayttoliittyma

class Laskin():
    """Luokka, joka vastaa laskimen sovelluslogiikasta
    """

    def __init__(self):
        """Luokan konstruktori
        """
        self.kayttoliittyma = Kayttoliittyma()

    def aloita(self):
        """Pyörittää laskimen toimintaa silmukan avulla
        """
        while True:
            lauseke = self.kayttoliittyma.syote()
            if lauseke == "-1":
                break
            postfix_lauseke = self._shunting_yard(lauseke)
            self.kayttoliittyma.tulos(self._laske(postfix_lauseke))

    def _shunting_yard(self, lauseke):
        """Muuntaa lausekkeen shunting yard -algoritmin avulla postfix-muotoon

        Args:
            lauseke (merkkijono): Muunnettava lauseke

        Returns:
            jono (lista): Postfix-muotoon muunnettu matemaattinen lauseke
        """
        pino = []
        jono = []
        for operandi in lauseke:
            if operandi == "(":
                pino.append(operandi)

            elif operandi == ")":
                while pino[-1] != "(":
                    jono.append(pino[-1])
                    pino.pop()
                pino.pop()

            elif operandi == "+" or operandi == "-":
                if len(pino) > 0:
                    while pino[-1] == "*" or pino[-1] == "/":
                        jono.append(pino[-1])
                        pino.pop()
                pino.append(operandi)

            elif operandi == "*" or operandi == "/":
                if len(pino) > 0:
                    if pino[-1] == "*" or pino[-1] == "/":
                        jono.append(pino[-1])
                        pino.pop()
                    pino.append(operandi)
                else: pino.append(operandi)
            else:
                jono.append(operandi)
            
        while len(pino)>0:
            jono.append(pino[-1])
            pino.pop()

        return jono

    def _laske(self, lauseke):
        """Laskee matemaattisen lausekkeen arvon

        Args:
            lauseke (lista): matemaattinen lauseke

        Returns:
            tulos (liukuluku): laskettu lausekkeen arvo
        """
        pino = []
        for operandi in lauseke:
            if operandi == "+" or operandi == "-" or operandi == "*" or operandi == "/":
                eka = pino.pop()
                toka = pino.pop()
                if operandi == "+":
                    tulos = eka + toka
                    pino.append(tulos)
                elif operandi == "-":
                    tulos = toka - eka
                    pino.append(tulos)
                elif operandi == "*":
                    tulos = eka * toka
                    pino.append(tulos)
                elif operandi == "/":
                    tulos = toka / eka
                    pino.append(tulos)
            else: 
                pino.append(float(operandi))

        return pino[-1]
