from kayttoliittyma import Kayttoliittyma
from laskutoimitukset import Laskutoimitukset
from shunting_yard import ShuntingYard
from muuttujat import Muuttujat


class Laskin():
    """Luokka, joka vastaa laskimen sovelluslogiikasta
    """

    def __init__(self):
        """Luokan konstruktori
        """
        self.kayttoliittyma = Kayttoliittyma()
        self.laskutoimitukset = Laskutoimitukset()
        self.shunting_yard = ShuntingYard()
        self.muuttujat = Muuttujat()

    def aloita(self):
        """Pyörittää laskimen toimintaa silmukan avulla
        """
        while True:
            lauseke = self.kayttoliittyma.syote()
            lauseke = lauseke.replace(" ","")
            if lauseke == "-1":
                break
            if "=" in lauseke:
                self.muuttujat.lisaa_muuttuja(lauseke)
                continue
            postfix_lauseke = self.shunting_yard.muunna(lauseke)
            self.kayttoliittyma.tulos(self.laskutoimitukset.laske(postfix_lauseke))

    