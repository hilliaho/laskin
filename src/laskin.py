from kayttoliittyma import Kayttoliittyma

class Laskin():

    def __init__(self):
        self.kayttoliittyma = Kayttoliittyma()

    def aloita(self):
        lauseke = self.kayttoliittyma.syote()
        postfix_lauseke = self._shunting_yard(lauseke)
        self.kayttoliittyma.tulos(self._laske(postfix_lauseke))

    def _shunting_yard(self, lauseke):
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
            else: pino.append(int(operandi))

        return pino
