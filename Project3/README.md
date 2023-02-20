# Engeto_repo
Třetí projekt na Python Akademii od Engeta
- Finální projekt zaměřený na Web Scraping

Popis projektu 
- Tento program slouží ke stahování výsledků voleb do Poslanecké sněmovny PČR z roku 2017.

Instalace knihoven
- Knihovny, které jsou použity v programu, jsou uloženy v souboru requirements.txt
- Pro instalaci doporučuji použít nové virtuální prostředí a s nainstalovaným manažerem spustit následovně:
    pip3 -- version                 # overim verzi manazeru
    pip3 instal -r requirements.txt #nainstaluji knihovnu

Spuštění projektu 
- Spouštění souboru elections_scraper_final.py vyžaduje dva vstupní argumenty:
    odkaz na vybranou URL stránku z webu volby.cz
    název výstupního souboru s příponou .csv

    python elections_scraper_final.py <url_odkaz> <vystupni_soubor>

Ukázka projektu
- Výsledky hlasování pro okres Hradec Králové:
    1. argument: 'https://www.volby.cz/pls/ps2017/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5201'
    2. argument: 'hradec_vysledky.csv'

Spuštění programu:

python elections_scraper_final.py 'https://www.volby.cz/pls/ps2017/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5201' 'hradec_vysledky.csv'


Částečný výstup:
code,obec,volici_v_seznamu,vydane_obalky,platne_hlasy,1,2,3,4,6,7,8,9,10,12,13,14,15,19,20,21,22,23,24,26,27,28,29,30
code,obec,volici_v_seznamu,vydane_obalky,platne_hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
569828,Babice,165,109,108,7,1,0,4,0,7,19,3,0,0,1,0,6,0,9,36,0,0,2,1,0,0,12,0
569836,Barchov,227,141,140,21,0,0,9,0,5,16,2,0,2,0,0,19,1,4,46,1,0,3,2,1,1,6,1
569852,Běleč nad Orlicí,269,207,206,38,0,0,8,0,9,1,3,0,7,0,0,16,0,12,76,0,0,10,1,0,0,25,0


Poznámka k programu:
Program mi při zápisu dat do .csv neuměl přečíst všechny znaky v názvu politických stran. Výsledkem pak byl nedokončený .csv soubor. Obešel jsem to nakonec tak, že místo názvu stran v hlavičce jsou čísla, která měly strany vylosované a hned po nimi je řádek, kde jsou již politická uskupení vypsána. 
'Čisté řešení' s názvy stran v prvním řádku mi fungovalo pouze u okresu Prostějov.
