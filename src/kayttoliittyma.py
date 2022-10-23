class Kayttoliittyma():

    def syote(self):
        """pyytää käyttäjältä syötettä

        Returns:
            lauseke (merkkijono): käyttäjän antama syöte
        """
        print("")
        lauseke = input("lauseke: ")
        return lauseke

    def tulos(self, tulos):
        """tulostaa laskutoimituksen tuloksen

        Args:
            tulos (liukuluku): laskimella laskettu tulos
        """
        print(tulos)

    def alkuviesti(self):
        print("___________________________________", "\n")
        print("Tervetuloa käyttämään laskinta")
        print("Sulje ohjelma komennolla -1")
        print("___________________________________")

    def virheviesti(self):
        print("virheellinen syöte")
