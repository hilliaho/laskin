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
        edellinen_operandi = ""
        for operandi in lauseke:
            if operandi == "(":
                pino.append(operandi)

            elif operandi == ")":
                while pino[-1] != "(":
                    jono.append(pino[-1])
                    pino.pop()
                pino.pop()

            elif operandi in ("+", "-"):
                while True:
                    if len(pino) == 0:
                        break
                    if pino[-1] not in ("*", "/", "^"):
                        break
                    jono.append(pino[-1])
                    pino.pop()
                pino.append(operandi)

            elif operandi in ("*", "/"):
                if len(pino) > 0:
                    if pino[-1] in ("*", "/", "^"):
                        jono.append(pino[-1])
                        pino.pop()
                    pino.append(operandi)
                else: pino.append(operandi)

            elif operandi == "^":
                pino.append(operandi)
                
            elif operandi in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                if edellinen_operandi in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                    jono[-1] += operandi
                else:
                    jono.append(operandi) 

            edellinen_operandi = operandi

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
            if operandi in ("+", "-", "*", "/","^"):
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
