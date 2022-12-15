import random
number=[]

def vytvor_cislo():
    for i in range(4):
        x=random.randrange(0,9)
        number.append(x)
    if len(number)>len(set(number)):
        number.clear()
        vytvor_cislo()

vytvor_cislo()
cislo= ''.join(str(x) for x in number)

def kontroluje_vstup(input_check):
    while input_check:
        vstup = input("Vlož 4-místné číslo: ")
        if vstup.isnumeric() and len(vstup)==4 and vstup[0]!='0':
            triditko=dict()
            for cislo in vstup:
                if cislo not in triditko:
                    triditko[cislo]=1  
                else:
                    triditko[cislo]=triditko[cislo]+1
            if len(triditko)==4:
                input_check=False
            else:
                print("Duplicita")
        elif vstup[0]=='0':
            print('Začiná nulou')
        elif len(vstup)!=4:
            print('Špatný počet znaků')
        else:
            print('Neni cislo')
    return vstup
    
def vypis_hodnot(pocitadlo_cows, pocitadlo_bulls):
    cows=pocitadlo_cows-pocitadlo_bulls
    bulls=pocitadlo_bulls
    if cows==1:
        if bulls==1:
            print(f'{bulls} bull, {cows} cow')
        else:
            print(f'{bulls} bulls, {cows} cow')    
    else:
        if bulls==1:
            print(f'{bulls} bull, {cows} cows')
        else:
            print(f'{bulls} bulls, {cows} cows')




print(""" Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
""")
mod=True
tajenka: str= cislo
pocitadlo_pokusu=0
while mod:
    input_check=True
    check=kontroluje_vstup(input_check)
    print(check)
    print(f'>>> {check}')
    pocitadlo_pokusu+=1
    dissipation_tajenka=dict()
    for index, i in enumerate(tajenka):
        dissipation_tajenka[index]=i
    dissipation_input=dict()
    for index, i in enumerate(check):
            dissipation_input[index]=i
    pocitadlo_cows = 0
    for cislo in check:
        if cislo in tajenka:
            pocitadlo_cows+=1
    pocitadlo_bulls = 0
    for index in dissipation_input:
        if dissipation_input[index]==dissipation_tajenka[index]:
            pocitadlo_bulls+=1

    vypis_hodnot(pocitadlo_cows, pocitadlo_bulls)

    if check==tajenka:
        print(f"Hurá, vyhrál jsi! Potřeboval jsi k tomu {pocitadlo_pokusu} pokusů")
        mod=False
    else:
        input_check=True
    print('-----------------------------------------------')
        