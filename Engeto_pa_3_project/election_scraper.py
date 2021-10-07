import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import sys


def input_check() -> bool:
    input_list = sys.argv
    if len(input_list) != 3:
        text_for_stop = 'Three arguments expecting!'
        script_stop(text_for_stop)
    else:
        print('Input arguments are OK')
        return True


def request_site() -> str:
    try:
        home_site = requests.get('https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ')
        home_site.raise_for_status()
    except HTTPError as http_err:
        text_for_stop = 'HTTP error occurred: {}'.format(http_err)
        script_stop(text_for_stop)
    except Exception as error:
        text_for_stop = 'Other error occurred: {}'.format(error)
        script_stop(text_for_stop)
    else:
        return home_site.text


def script_stop(stop_text: str):
    print(stop_text)
    print('QUITTING..')
    exit()


if __name__ == '__main__':
    if input_check():
        req_site = request_site()
        print(type(req_site))
