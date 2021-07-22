def text_template() -> list:
    """Tato funkce pouze nacte list textu"""
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
    return TEXTS

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
            if vyber_textu.isnumeric():
                oddeleni_textu()
                return int(vyber_textu)-1
            else: spatne_zadani(2)
        else: spatne_zadani(1)
    else: spatne_zadani(0)
    oddeleni_textu()




def oddeleni_textu(oddelovac = '-', delka = 45):
    print(oddelovac * delka)

def spatne_zadani(pricina: int):
    list_pricin = ['username', 'password', 'input']
    oddeleni_textu()
    print(f'Wrong {list_pricin[pricina]}, quitting..')
    exit()