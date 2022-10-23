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
                if operandi == "(":  # lisää pinoon
                    pino.append(operandi)

                elif operandi == ")":
                    # Lisää pinosta jonoon kaikki merkit niin kauan että tulee toinen sulku
                    while pino[-1] != "(":
                        jono.append(pino[-1])
                        pino.pop()
                    pino.pop()
                    if len(pino)==0:
                        continue
                    if pino[-1] in ("sin", "cos", "tan"):
                        jono.append(pino[-1])
                        pino.pop()

                elif operandi in ("+", "-"):  # Poista pinosta merkit *, /, ^
                    if operandi == "-" and edellinen_operandi not in self.numerot and edellinen_operandi not in self.kirjaimet:
                        jono.append("0")
                    while True:
                        if len(pino) == 0:
                            break
                        if pino[-1] not in ("+", "-", "*", "/", "^"):
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

                elif operandi[0] in self.numerot:
                    jono.append(operandi)

                elif operandi[0] in self.kirjaimet:
                    if operandi in ("sin", "cos", "tan", "asin", "acos", "atan"):
                        pino.append(operandi)
                    else:
                        jono.append(operandi)
                else:
                    print("tääl")
                    return ["0"]

                edellinen_operandi = operandi

            while len(pino) > 0:
                jono.append(pino[-1])
                pino.pop()
            return jono
        except IndexError:
            print("indexError")
            return ["0"]
