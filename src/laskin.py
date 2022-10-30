import math

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
        self.kayttoliittyma.alkuviesti()
        while True:
            self.muuttujat.lisaa_muuttuja(['pi', '=', str(math.pi)])
            lauseke = self.kayttoliittyma.syote()
            if lauseke == "-1":
                break
            tarkistettu_lauseke = self.lausekkeen_tarkistus.tarkista(lauseke)
            if tarkistettu_lauseke is False:
                self.kayttoliittyma.virheviesti()
                continue
            if "=" in tarkistettu_lauseke:
                self.muuttujat.lisaa_muuttuja(tarkistettu_lauseke)
                continue
            postfix_lauseke = self.shunting_yard.muunna(tarkistettu_lauseke)
            self.kayttoliittyma.tulos(
                self.laskutoimitukset.laske(postfix_lauseke))
