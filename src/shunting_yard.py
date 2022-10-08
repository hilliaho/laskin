class ShuntingYard():
    """Luokka, joka vastaa shunting yard -algoritmin toteuttamisesta
    """

    def __init__(self, numerot, kirjaimet):
        self.numerot = numerot
        self.kirjaimet = kirjaimet

    def muunna(self, lauseke):
        """Muuntaa lausekkeen shunting yard -algoritmin avulla postfix-muotoon

        Args:
            lauseke (merkkijono): Muunnettava lauseke

        Returns:
            jono (lista): Postfix-muotoon muunnettu matemaattinen lauseke
        """
        pino = []
        jono = []
        edellinen_operandi = ""

        try:
            for operandi in lauseke:
                if operandi == "(": #lisää pinoon
                    pino.append(operandi)

                elif operandi == ")":
                    while pino[-1] != "(":  #Lisää jonosta pinoon kaikki merkit niin kauan että tulee sulku
                        jono.append(pino[-1])
                        pino.pop()
                    pino.pop()

                elif operandi in ("+", "-"):   #Poista pinosta merkit *, /, ^
                    if operandi == "-" and edellinen_operandi not in self.numerot and edellinen_operandi not in self.kirjaimet:
                        jono.append("0")
                    while True:
                        if len(pino) == 0:
                            break
                        if pino[-1] not in ("+","-","*", "/", "^"):
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
                    else:
                        pino.append(operandi)

                elif operandi == "^":
                    pino.append(operandi)

                elif operandi in self.numerot:
                    if edellinen_operandi in self.numerot:
                        jono[-1] += operandi
                    else:
                        jono.append(operandi)

                elif operandi in self.kirjaimet:
                    if edellinen_operandi in self.kirjaimet:
                        jono[-1] += operandi
                    else:
                        jono.append(operandi)

                else:
                    return ["0"]

                edellinen_operandi = operandi

            while len(pino) > 0:
                jono.append(pino[-1])
                pino.pop()
            return jono
        except:
            return ["0"]
