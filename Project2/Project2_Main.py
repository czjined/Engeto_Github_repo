import random

def main():
    bulls, cows = 0, 0
    pokusy = 0
    print("Hi there!")
    oddeleni_textu()
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    oddeleni_textu()
    hidden_number = random.sample(range(1,10), k=1) + random.choices(range(10), k=3)
    print(hidden_number)
    while cows < 4:
        input_number = list(input('Enter a number: '))
        if kontrola_vstupu(input_number):
            print("Zadani v poradku, zahajuji vyhodnocovani.")
            cows += 1

def oddeleni_textu(oddelovac = '-', delka = 45):
    print(oddelovac * delka)

def kontrola_vstupu(vst_list: list, vysledek_kontroly = False):
    if len(vst_list) != 4:
        print("Four digits expected!")
    elif not ''.join(vst_list).isdigit():
        print("Decimal numbers only!")
    elif vst_list[0] == '0':
        print("Your input can not start with 0!")
    else:
        vst_list = set(vst_list)
        if len(vst_list) != 4:
            print("Unique numbers!")
        else:
            vysledek_kontroly = True
    oddeleni_textu()
    return vysledek_kontroly



if __name__ == "__main__":
    main()