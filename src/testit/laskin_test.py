import unittest

from laskin import Laskin

class TestiLaskin(unittest.TestCase):
    def setUp(self):
        self.laskin = Laskin()

    def testi_shunting_yard(self):
        lauseke = self.laskin._shunting_yard("3+4*(2-1)")
        self.assertEqual(lauseke, ["3", "4", "2", "1", "-", "*", "+"])

    def testi_yhteenlasku(self):
        lauseke = self.laskin._shunting_yard("1+2")
        tulos = self.laskin._laske(lauseke)
        self.assertEqual(tulos, 3.0)

    def testi_vahennyslasku(self):
        lauseke = self.laskin._shunting_yard("5-3")
        tulos = self.laskin._laske(lauseke)
        self.assertEqual(tulos, 2.0)

    def testi_kertolasku(self):
        lauseke = self.laskin._shunting_yard("2*2")
        tulos = self.laskin._laske(lauseke)
        self.assertEqual(tulos, 4.0)

    def testi_jakolasku(self):
        lauseke = self.laskin._shunting_yard("6/3")
        tulos = self.laskin._laske(lauseke)
        self.assertEqual(tulos, 2.0)

    def testi_laskujarjestys(self):
        lauseke = self.laskin._shunting_yard("3*1+4/2-(1+2)")
        tulos = self.laskin._laske(lauseke)
        self.assertEqual(tulos, 2.0)