import csv
import traceback
from requests import get
from bs4 import BeautifulSoup as bs
import argparse
#vložené argumenty přečti a ulož jako proměnné 'url' a 'výstup'
parser = argparse.ArgumentParser(description='rozcleni vstupni argumenty')
parser.add_argument('url', type=str)
parser.add_argument('vystup', type=str)
args = parser.parse_args()
vystup=args.b
url = args.a

urla=url[:38]+'11'+url[39:]
url_prefix=url[:35]


######funkce######

def vyber_atributy_z_radku (tr_tag):
     cislo=tr_tag[0].string
     platne_hlasy_strana=tr_tag[2].string
     return{
          cislo: platne_hlasy_strana
     }
# zapiš data do csv.
def zapis_data(data:dict, jmeno_souboru:str):
     try: 
          csv_soubor= open (jmeno_souboru, mode='w', encoding='utf-8',newline='')
          sloupce = data[0].keys()
     except FileExistsError:
          return traceback.format_exc()
     except IndexError:
          return traceback.format_exc()
     else:
          zapis= csv.DictWriter(csv_soubor, fieldnames=sloupce)
          zapis.writeheader()
          zapis.writerows(data)
          return 'Saved'
     finally:
          csv_soubor.close()


###hlavni kod###

#vysledny list
vysledky=[]
#Stáhni názvy politických stran a jejich čísel
list_stran=dict()
list_stran.update({'code':'code','obec':'obec','volici_v_seznamu': 'volici_v_seznamu', 'vydane_obalky':'vydane_obalky', 'platne_hlasy':'platne_hlasy'})
# stáhni HTML kód stránky
htmla=get(urla)
# vytvoř soup objekt ze staženého kódu
soupa = bs(htmla.content, 'html.parser')
# najdi tabulku a iteruj přes řádky td tagy, následně ulož čísla a názvy stran do slovníku
tablea= soupa.find_all('table',{'class':'table'})
for tabulkaa in tablea[1:]:
     rowsa=tabulkaa.find_all('tr')[2:]
     for tra in rowsa:
          if tra.find("td", {"class": "hidden_td"}):
               break          
          else:
               colsa=tra.find_all('td')
               list_stran.update ({colsa[0].string:colsa[1].string})
vysledky.append(list_stran)

# stáhni HTML kód stránky s výsledky
html = get(url)

# vytvoř soup objekt ze staženého kódu
soup = bs(html.content, 'html.parser')

# najdi tabulku obsahující názvy obcí a URL odkazy na další stránky
table= soup.find_all('table',{'class':'table'})
for tabulka in table:
     rows=tabulka.find_all('tr')[2:]
# pokud najdeš td tag hidden_td, skonči hledání
     for tr in rows:
          if tr.find("td", {"class": "hidden_td"}):
               break          
          else:
#najdi a ulož kód, název obce a URL odkaz na výsledky v jednotlivých obcích
               cislo_hlasy={}
               cols=tr.find_all('td')
               code=cols[0].string
               obec=cols[1].string
               odkaz=url_prefix+cols[0].find('a').get('href')
               cislo_hlasy['code']=code
               cislo_hlasy['obec']= obec
#projdi výsledky voleb u obce a ulož voliče v seznamu, vydané obálky a platné hlasy
               html1=get(odkaz)
               soup1=bs(html1.content, 'html.parser')
               cislo_hlasy['volici_v_seznamu'] = soup1.find_all('td', {'headers': 'sa2'})[-1].text
               cislo_hlasy['vydane_obalky' ] = soup1.find_all('td', {'headers': 'sa3'})[-1].text
               cislo_hlasy['platne_hlasy']= soup1.find_all('td', {'headers': 'sa6'})[-1].text
#najdi tabulky s výsledky a po řádku čti td tagy
               table1=soup1.find_all('table',{'class':'table'})#vyber tabulek
               for tabulka1 in table1[1:]:
                    rows1 = tabulka1.find_all('tr') [2:] # najdu vsechny 'tr'
                    for tr1 in rows1:
                         td_na_radku=tr1.find_all('td') 
                         if td_na_radku[0]({"class": "hidden_td"}):
                              break
                         else:
                             data_obec=vyber_atributy_z_radku(td_na_radku)
                             cislo_hlasy.update(data_obec)
               vysledky.append(cislo_hlasy)                     
data=zapis_data(vysledky,vystup)
