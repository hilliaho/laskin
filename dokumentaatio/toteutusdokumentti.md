# Toteutusdokumentti

Laskimella voi laskea yhteen, vähennys, kerto, jako ja potenssilaskuja, sekä käyttää omia muuttujia.
Algoritmi, jota käytetään, on [shunting yard](https://en.wikipedia.org/wiki/Shunting_yard_algorithm) -algoritmi, 
joka muuntaa pinoa ja jonoa käyttäen käyttäjän antaman lausekkeen postfix-notaatioon, jolloin se on helpompi laskea oikeassa laskujärjestyksessä.
Käyttöliittymä on ainoastaan tekstipohjainen, eli ei ole graafista käyttöliittymää.

Ohjelma ottaa käyttäjältä syötteenä lausekkeen, joka voi olla laskutoimitus (esim. (1+2)*3) tai muuttujan määrittely (esim. x=5).

Ohjelmaa voisi vielä parantaa esimerkiksi niin, että laskin osaisi sieventää lausekkeita joissa on joku kirjainvakio.
