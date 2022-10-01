import unittest

from laskin import Laskin

class TestiLaskin(unittest.TestCase):
    def setUp(self):
        self.laskin = Laskin()

    def testi_shunting_yard(self):
        lauseke = self.laskin.shunting_yard.muunna("3+4*(2-1)")
        self.assertEqual(lauseke, ["3", "4", "2", "1", "-", "*", "+"])

    def testi_yhteenlasku(self):
        lauseke = self.laskin.shunting_yard.muunna("1+2")
        tulos = self.laskin.laskutoimitukset.laske(lauseke)
        self.assertEqual(tulos, 3.0)

    def testi_vahennyslasku(self):
        lauseke = self.laskin.shunting_yard.muunna("5-3")
        tulos = self.laskin.laskutoimitukset.laske(lauseke)
        self.assertEqual(tulos, 2.0)

    def testi_kertolasku(self):
        lauseke = self.laskin.shunting_yard.muunna("2*2")
        tulos = self.laskin.laskutoimitukset.laske(lauseke)
        self.assertEqual(tulos, 4.0)

    def testi_jakolasku(self):
        lauseke = self.laskin.shunting_yard.muunna("6/3")
        tulos = self.laskin.laskutoimitukset.laske(lauseke)
        self.assertEqual(tulos, 2.0)

    def testi_potenssilasku(self):
        lauseke = self.laskin.shunting_yard.muunna("2^4")
        tulos = self.laskin.laskutoimitukset.laske(lauseke)
        self.assertEqual(tulos, 16.0)

    def testi_laskujarjestys(self):
        lauseke = self.laskin.shunting_yard.muunna("3*1+4/2-(1+2)")
        tulos = self.laskin.laskutoimitukset.laske(lauseke)
        self.assertEqual(tulos, 2.0)
        
    def testi_tunnistaa_huonon_lausekkeen(self):
        lauseke = "?"
        self.assertEqual(self.laskin._tarkista(lauseke), False)

    def testi_tunnistaa_hyvan_lausekkeen(self):
        lauseke = "1+2*4-(6-7)^(-3)"
        self.assertEqual(self.laskin._tarkista(lauseke), True)

    def testi_muuttuja(self):
        self.laskin.muuttujat.lisaa_muuttuja("x=5")
        self.assertEqual(self.laskin.muuttujat.arvo("x"), 5)

    def testi_muuttujaa_ei_ole(self):
        self.assertEqual(self.laskin.muuttujat.onko_muuttuja_olemassa("x"), False)