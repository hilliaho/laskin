import unittest
import math

from laskutoimitukset import Laskutoimitukset
from muuttujat import Muuttujat


class TestiLaskutoimitukset(unittest.TestCase):
    def setUp(self):
        muuttujat = Muuttujat()
        numerot = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        kirjaimet = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "å", "a", "s",
                          "d", "f", "g", "h", "j", "k", "l", "ö", "ä", "z", "x", "c", "v", "b", "n", "m"]
        operaattorit = ["+", "-", "*", "/", "^", "=", "(", ")"]
        self.laskutoimitukset = Laskutoimitukset(
            muuttujat, numerot, kirjaimet, operaattorit)

    def testi_peruslaskutoimitukset(self):
        self.assertEqual(self.laskutoimitukset.laske(['1', '2', '+']), 3)
        self.assertEqual(self.laskutoimitukset.laske(['1', '2', '*']), 2)
        self.assertEqual(self.laskutoimitukset.laske(['1', '2', '/']), 0.5)
        self.assertEqual(self.laskutoimitukset.laske(['1', '2', '-']), -1)
        self.assertEqual(self.laskutoimitukset.laske(['1', '2', '^']), 1)
        self.assertEqual(self.laskutoimitukset.laske(
            ['1', '0', '/']), "virheellinen syöte")

    def testi_funktiot(self):
        self.assertEqual(self.laskutoimitukset.laske(
            ['3.141592653589793', 'sin']), 0)
        self.assertEqual(self.laskutoimitukset.laske(
            ['3.141592653589793', 'cos']), -1)
        self.assertEqual(self.laskutoimitukset.laske(
            ['3.141592653589793', 'tan']), 0)
        self.assertEqual(self.laskutoimitukset.laske(
            ['8', 'asin']), "virheellinen syöte")
        self.assertEqual(self.laskutoimitukset.laske(['1', 'acos']), 0)
        self.assertEqual(self.laskutoimitukset.laske(['0', 'atan']), 0)

    def testi_laskujarjestys(self):
        lauseke = ['3', '1', '*', '4', '2', '/', '+', '1', '2', '+', '-']
        tulos = self.laskutoimitukset.laske(lauseke)
        self.assertEqual(tulos, 2.0)

    def testi_muuttujat(self):
        self.laskutoimitukset.muuttujat.lisaa_muuttuja(['x', '=', '9'])
        self.laskutoimitukset.muuttujat.lisaa_muuttuja(['y', '=', '-1'])
        self.assertEqual(self.laskutoimitukset.laske(
            ['z', 'x', '+']), "virheellinen syöte")
        self.assertEqual(self.laskutoimitukset.laske(['y', 'x', '+']), 8)
