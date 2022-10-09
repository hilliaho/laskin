import unittest

from laskutoimitukset import Laskutoimitukset


class TestiLaskutoimitukset(unittest.TestCase):
    def setUp(self):
        muuttujat = {'x': 3.0}
        numerot = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        kirjaimet = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "å", "a", "s",
                          "d", "f", "g", "h", "j", "k", "l", "ö", "ä", "z", "x", "c", "v", "b", "n", "m"]
        operaattorit = ["+", "-", "*", "/", "^", "=", "(", ")"]
        self.laskutoimitukset = Laskutoimitukset(muuttujat, numerot, kirjaimet, operaattorit)

    def testi_yhteenlasku(self):
        lauseke = ['1', '2', '+']
        tulos = self.laskutoimitukset.laske(lauseke)
        self.assertEqual(tulos, 3.0)

    def testi_vahennyslasku(self):
        lauseke = ['1', '2', '-']
        tulos = self.laskutoimitukset.laske(lauseke)
        self.assertEqual(tulos, -1.0)

    def testi_kertolasku(self):
        lauseke = ['1', '2', '*']
        tulos = self.laskutoimitukset.laske(lauseke)
        self.assertEqual(tulos, 2.0)

    def testi_jakolasku(self):
        lauseke = ['1', '2', '/']
        tulos = self.laskutoimitukset.laske(lauseke)
        self.assertEqual(tulos, 0.5)

    def testi_potenssilasku(self):
        lauseke = ['1', '2', '^']
        tulos = self.laskutoimitukset.laske(lauseke)
        self.assertEqual(tulos, 1.0)

    def testi_laskujarjestys(self):
        lauseke = ['3', '1', '*', '4', '2', '/', '+', '1', '2', '+', '-']
        tulos = self.laskutoimitukset.laske(lauseke)
        self.assertEqual(tulos, 2.0)
