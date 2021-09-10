import random
import time

def main():
    bulls, cows = 0, 0
    pokusy = 0
    print("Hi there!")
    oddeleni_textu()
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    oddeleni_textu()
    hidden_number = generator_cisla()
    print(hidden_number)
    start_time = time.time()
    while cows < 4:
        bulls, cows = 0, 0
        input_number = list(input('Enter a number: '))
        print(input_number)
        pokusy += 1
        if kontrola_vstupu(input_number):
            for i, cislo in enumerate(input_number):
                if cislo == hidden_number[i]:
                    cows += 1
                elif cislo in hidden_number:
                    bulls += 1
            if cows < 4:
                print(f"{bulls} bulls, {cows} cows.")
    else:
        print(f"Correct, you've guessed the right number in {pokusy} guesses!")
        stop_timer(start_time)
        oddeleni_textu()

def oddeleni_textu(oddelovac = '-', delka = 45):
    print(oddelovac * delka)

def generator_cisla() -> list:
    rozsah = list(range(10))
    print(rozsah)
    nahodne_cislo = list()
    for i in range(4):
        if i == 0:
            nahodne_cislo.append(str(rozsah.pop(random.randrange(1,10))))
        else:
            index = 10 - i
            nahodne_cislo.append(str(rozsah.pop(random.randrange(index))))
    return nahodne_cislo

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

def stop_timer(pocatek):
    cas = time.time() - pocatek
    sekundy = round(cas % 60)
    minuty = int(cas // 60)
    hodiny = int(minuty // 60)
    print(f"It took {hodiny} hours, {minuty} minutes and {sekundy} seconds.")

if __name__ == "__main__":
    main()