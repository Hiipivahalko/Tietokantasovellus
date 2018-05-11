
# Käyttöohje


* Uusi käyttäjä kun saapuu sivulle näkee sovelluksen introviestin ja lomakkeen mistä tehdä itselleen käyttäjä. Tämän jälkeen kun tili on luotu, niin käyttäjä syöttää juuri laittamansa tiedot ja kirjautuu sisään. Tämän jälkeen käyttäjä pääsee etusivulle (pääkanavalle).

* Nyt käyttäjä voi kirjoittaa viestejä kanaville ja kommentoida niitä. Käyttäjä voi luoda ylärivillä olevasta navigoinnista uuden kanavan jos omanlaista kanavaa ei löydy. Tämän jälkeen jos käyttäjä luo sellaisen hänellä on oikeudet muokata kanavaa. Tämä onnistuu jos käyttäjä painaa '...' Nappia ja sieltä update linkkiä.Nappi löytyy oikeasta yläkulmasta. Samaisesta dropdown napista voi myös poistaa kanavan jos siltä tuntuu. Viestien kirjoitus onnistuu helposti kunhan vain kirjoittaa teksti kenttään halutun viestin. Kommentin voi käydä jättämässä painamalla haluttua viestiä mihin haluaa kommentoida. Tämän jälkeen käyttäjä pääsee viestin sivulle jossa hän voi tämän kommentin kirjoittaa. Back nappulasta sivun ylälaidassa käyttäjä pääsee takaisin kanavan sivuille.

* Kaikkien sivujen vasemmassa sivulaidassa käyttäjä näkee listattuna kaikki kanavat hieman eriteltynä. Ensiksi hän näkee yleiset kanavat johon kaikki foorumin käyttäjät pääsevät laittamaan viestejä. Tämän jälkeen tulevat privaatit kanavat jossa virheällä värillä ovat ne kanavat jotka ovat käyttäjän itse luomia. Lopuksi käyttäjä näkee muut yksityiset kanavat joihin hän ei ole liittynyt.

* Käyttäjä voi kirjautua ulos sovelluksesta painamalla 'Manage account' nappulaa sivun oikeassa yläkulmassa ja sen jälkeen 'Logout'. Samaisesta napista ilmestyy näkyviin 'my account' linkki, jota painamalla käyttäjä pääsee omille sivuilleen. Siellä hän voi muokata tietojaan ja näkee omat tietonsa. Hän voi möyös muokata niitä muokkaus lomakkeen avulla. Sivulla on myös listattuna kaikki kanavat mihin käyttäjä on liittynyt (yksityiset vain) sekä käyttäjä näkee myös kaikki omat viestinsä ja kommenttinsa. Viestejä, kommentteja tai kanavia painamalle pääset juuri kyseisen asian sivulle suoraan jos haluat myöskin. Muut käyttäjät voivat myös tarkastella sinun sivuasi, mutta he eivät näe kuin tietosi ilman spotia sekä kanavat jolle olet liittynyt.

* Sovelluksen ylläpitäjällä on muutama lisätoiminto. Hän voi luoda uusia käyttäjiä yläpalkin navigoinnissa samoin kuin uusi käyttäjä tekisin oman tilin. Ylläpitäjä voi kuitenkin valita onko käyttäjä minkälaiset admin oikeudet. Ylläpitäjä voi myös hallita kaikkia tilejä samaan aikaan 'Manage accounts' linkin kautta. Siellä ylläpitäjä voi vaihtaa käyttäjän admin oikeuksia tai poistaa käyttäjän kokonaan. Ylläpitäjä voi myös 'Manage channels' linkin avulla päästä hallitsemaan kanavia poistaa tai muokata niitä. Ylläpitäjä voi myös vaihtaa käyttäjän admin statusta suoraan menemällä käyttäjän tilille ja siellä oikeasta yläkulmasta olevasta napista 'upgrade...'. Ylläpitäjällä on myös mahdollisuus poistaa jokainen viesti tai kommentti millä tahansa kanavalla. Poiston voi suorittaa viestin/kommentin vieressä olevasta 'x' nappulasta. Viestin kirjoittaja voi myös tehdä tämän toiminnon omille viesteillee/kommenteilleen.

# Asennusohje

* cloonaa projekti koneelle joko zip tiedostona tai ssh:n avulla

#### Tee seuraavat operaatiot terminaalissa projektin juuressa
* python3 -m venv venv
* pip install --upgrade pip
* pip install Flask
* pip install gunicorn
* pip install flask-sqlalchemy
* pip freeze | grep -v pkg-resources > requirements.txt
* pip install flask-wtf
* pip install flask-login
* python run.py

# Sovelluksesta puuttuva ominaisuudet

* Virheistä/törkeyksistä ilmoittaminen admin käyttäjälle
* Viestistä/kommentista tykkääminen/ ei tykkääminen
* Salaisten kanavien luonti ja niihin liittyminen
* Asioiden haku yleisesti, sellaisiin paikkoihin mihin käyttäjällä oikeudet
* datan sort monipuolisemmaksi
* salanojen suojaaminen
* ulkoasun monipuolistaminen



## omat kokemukset

* työtä riitti uudenoppimisessa, mutta jälkeenpäin tuntui hyvältä aina kun oivalsi jonkin asian
* dokumentaatio vastaa mielestäni hyvin sovellusta
* kurssin alun materiaali ajoin hyvin projektiin, oli helppo lähteä työstämään työtään. Toki kurssin dokumentaation loppui kuin seinään ja loppu jätettiin tekijän vastuulle. Tästä omat hyvät ja huonot fiilikset. Joitan jippoja/kikkoja olisi voinut vinkata.
* Validointeja en saanut lopulta toimimaan oikein kaikkiin formeihin, vaikka tein samallalailla kuten sellaisissa formeissa missä ne toimivat kuten pitää. Jos pystytte kertomaan miksi esim. accountin luonnissa olevat validoinnit ei toimi, olisin kiitollinen. Validoinnit siis toimivat kyllä, mutta virhe viestejä ei jostain syystä itse sivulla näy oikealla tavalla.
