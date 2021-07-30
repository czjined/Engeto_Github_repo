import string

TEXTS = ['''
    Situated about 10 miles west of Kemmerer, 
    Fossil Butte is a ruggedly impressive 
    topographic feature that rises sharply 
    some 1000 feet above Twin Creek Valley 
    to an elevation of more than 7500 feet 
    above sea level. The butte is located just 
    north of US 30N and the Union Pacific Railroad, 
    which traverse the valley. ''',

    '''At the base of Fossil Butte are the bright 
    red, purple, yellow and gray beds of the Wasatch 
    Formation. Eroded portions of these horizontal 
    beds slope gradually upward from the valley floor 
    and steepen abruptly. Overlying them and extending 
    to the top of the butte are the much steeper 
    buff-to-white beds of the Green River Formation, 
    which are about 300 feet thick.''',

    '''The monument contains 8198 acres and protects 
    a portion of the largest deposit of freshwater fish 
    fossils in the world. The richest fossil fish deposits 
    are found in multiple limestone layers, which lie some 
    100 feet below the top of the butte. The fossils 
    represent several varieties of perch, as well as 
    other freshwater genera and herring similar to those 
    in modern oceans. Other fish such as paddlefish, 
    garpike and stingray are also present.'''
    ]
def main():
    text_vyber = prihlaseni()
    text_list = TEXTS[text_vyber].split()
    statistika_textu(text_list)

def prihlaseni() -> int:
    """Zkontroluje prihlaseni uzivatele a zajisti vyber textu"""
    registrovani_uzivatele = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
    user_name = input('Username: ')
    if user_name in registrovani_uzivatele:
        user_password = input('password: ')
        if registrovani_uzivatele[user_name] == user_password:
            oddeleni_textu()
            print(f'Welcome to the app, {user_name}\nWe have 3 texts to be analyzed.')
            oddeleni_textu()
            vyber_textu = input('Enter a number btw. 1 and 3 to select: ')
            if vyber_textu.isnumeric() and int(vyber_textu) >= 1 and int(vyber_textu) <= 3:
                oddeleni_textu()
                return int(vyber_textu)-1
            else:
                spatne_zadani(2)
        else:
            spatne_zadani(1)
    else:
        spatne_zadani(0)
    oddeleni_textu()

def oddeleni_textu(oddelovac = '-', delka = 45):
    print(oddelovac * delka)

def spatne_zadani(pricina: int):
    list_pricin = ['username', 'password', 'input']
    oddeleni_textu()
    print(f'Wrong {list_pricin[pricina]}, quitting..')
    exit()

def statistika_textu(list_textu):
    slova_pocet, slova_capital, slova_lower, slova_upper = 0, 0, 0, 0
    cisla_pocet, cisla_suma = 0, 0
    slovnik_delek = dict()
    for slovo in list_textu:
        slovo = slovo.strip(string.punctuation)
        if slovo.isalpha() and slovo != ' ':
            slova_pocet += 1
            if slovo.islower():
                slova_lower += 1
            if slovo.isupper():
                slova_upper += 1
            if slovo.istitle():
                slova_capital += 1
        elif slovo.isnumeric():
            cisla_pocet += 1
            cisla_suma += int(slovo)
        else:
            print(f'Pozor, slovo {slovo} je mix cislic a znaku!')
        slovnik_delek = delky_slov(slovnik_delek, slovo)
    print(f'There are {slova_pocet} words in the selected text.')
    print(f'There are {slova_capital} titlecase words.')
    print(f'There are {slova_upper} uppercase words.')
    print(f'There are {slova_lower} lowercase words.')
    print(f'There are {cisla_pocet} numeric strings.')
    print(f'The sum of all the numbers {cisla_suma}')
    oddeleni_textu()
    graf_delek(slovnik_delek)

def delky_slov(slovnik_delek: dict, slovo: str) -> dict:
    klic = str(len(slovo))
    slovnik_delek[klic] = slovnik_delek.setdefault(klic, 0) + 1
    return slovnik_delek

def graf_delek(slovnik_delek: dict):
    hlavicka = ['LEN', 'OCCURENCES', 'NR.']
    sorted_list = list(slovnik_delek)
    for i, d in enumerate(sorted_list): sorted_list[i] = int(d)
    sorted_list.sort()
    nej_delka = max(slovnik_delek)
    nej_delka = slovnik_delek[nej_delka]
    formatted = '|{0:>3}|{1:<{sirka}}|{2:>3}|'.format(*hlavicka, sirka = 20)
    print(formatted)
    oddeleni_textu()
    for key in sorted_list:
        key = str(key)
        druhy = slovnik_delek[key] * '*'
        formatted = '|{0:>3}|{1:<{sirka}}|{2:>3}|'.format(key, druhy, str(slovnik_delek[key]), sirka = 20)
        print(formatted)
    oddeleni_textu()



if __name__ == "__main__":
    main()