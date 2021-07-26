from project1_def import *

def main():
    texty = text_template()
    text_vyber = prihlaseni()
    text_list = texty[text_vyber].split()
    statistika_textu(text_list)





if __name__ == "__main__":
    main()