from kayttoliittyma import Kayttoliittyma
from laskutoimitukset import Laskutoimitukset
from shunting_yard import ShuntingYard
from muuttujat import Muuttujat
from lausekkeen_tarkistus import LausekkeenTarkistus


class Laskin():
    """Luokka, joka vastaa laskimen sovelluslogiikasta
    """

    def __init__(self):
        """Luokan konstruktori
        """
        self.operaattorit = ["+", "-", "*", "/", "^", "=", "(", ")"]
        self.numerot = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
        self.kirjaimet = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "å", "a", "s",
                          "d", "f", "g", "h", "j", "k", "l", "ö", "ä", "z", "x", "c", "v",
                           "b", "n", "m"]
        self.kayttoliittyma = Kayttoliittyma()
        self.muuttujat = Muuttujat()
        self.laskutoimitukset = Laskutoimitukset(
            self.muuttujat, self.numerot, self.kirjaimet, self.operaattorit)
        self.shunting_yard = ShuntingYard(self.numerot, self.kirjaimet)
        self.lausekkeen_tarkistus = LausekkeenTarkistus(
            self.numerot, self.kirjaimet, self.operaattorit)

    def aloita(self):
        """Pyörittää laskimen toimintaa silmukan avulla
        """
        while True:
            lauseke = self.kayttoliittyma.syote()
            lauseke = lauseke.replace(" ", "")
            lauseke = lauseke.replace("**", "^")
            if self.lausekkeen_tarkistus.tarkista(lauseke) is False:
                print("virheellinen syöte")
                continue
            if lauseke == "-1":
                break
            if "=" in lauseke:
                self.muuttujat.lisaa_muuttuja(lauseke)
                continue
            postfix_lauseke = self.shunting_yard.muunna(lauseke)
            self.kayttoliittyma.tulos(
                self.laskutoimitukset.laske(postfix_lauseke))
