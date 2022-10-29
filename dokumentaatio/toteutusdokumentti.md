# Toteutusdokumentti

## Laskin

Laskimella voi laskea yhteen, vähennys, kerto, jako ja potenssilaskuja, trigonometrisia funktioita ja niiden käänteisfunktioita, sekä lisätä ja käyttää omia muuttujia. Laskimella on ainoastaan tekstikäyttöliittymä.

## Ohjelman rakenne

Ohjelma koostuu kuudesta luokasta. *Laskin*-luokka sisältää silmukan, joka kutsuu muita luokkia oikeassa järjestyksessä. Silmukan suoritus jatkuu ohjelman käynnistyksestä lähtien siihen asti, että ohjelma suljetaan. *Käyttöliittymä*-luokka tulostaa ohjelman käynnistyksen yhteydessä lyhyen käyttöohjeen, sekä vastaa käyttäjän syötteen ottamisesta ja laskutoimituksen tuloksen tulostamisesta. *LausekkeenTarkistus*-luokka tarkistaa, onko lauseke sääntöjen mukainen ja voidaanko sen arvo laskea laskimella. *ShuntingYard*-luokka muuntaa käyttäjän syöttämän lausekkeen postfix-muotoon. Laskutoimitukset-luokka taas vastaa laskutoimitusten suorittamisesta. *Muuttujat*-luokan avulla ohjelma pitää kirjaa muuttujista, joita käyttäjä voi lisätä, muuttaa niiden arvoa ja käyttää laskutoimituksissa.

## Algoritmit ja tietorakenteet

Algoritmi, jota käytetään, on [shunting yard](https://en.wikipedia.org/wiki/Shunting_yard_algorithm) -algoritmi, 
joka muuntaa pinoa ja jonoa käyttäen käyttäjän antaman lausekkeen postfix-notaatioon, jolloin se on helpompi laskea oikeassa laskujärjestyksessä.

## Parannusehdotuksia

Ohjelmaa voisi vielä parantaa esimerkiksi tekemällä graafisen käyttöliittymän.

## Lähteet 

https://en.wikipedia.org/wiki/Shunting_yard_algorithm

