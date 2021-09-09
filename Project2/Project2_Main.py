import random

def main():
    print("Hi there!")
    oddeleni_textu()
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    oddeleni_textu()
    hidden_number = random.sample(range(1,10), k=4)
    print(hidden_number)

def oddeleni_textu(oddelovac = '-', delka = 45):
    print(oddelovac * delka)

if __name__ == "__main__":
    main()