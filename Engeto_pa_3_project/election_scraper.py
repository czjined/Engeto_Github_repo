import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import sys
import csv


def input_check(list_for_check: list) -> bool:
    if len(list_for_check) != 3:
        text_for_stop = 'Three arguments expecting!'
        script_stop(text_for_stop)
    else:
        print('Input arguments are OK')
        return True


def request_site(html_argument: str) -> str:
    try:
        home_site = requests.get(html_argument)
        home_site.raise_for_status()
    except HTTPError as http_err:
        text_for_stop = 'HTTP error occurred: {}'.format(http_err)
        script_stop(text_for_stop)
    except Exception as error:
        text_for_stop = 'Other error occurred: {}'.format(error)
        script_stop(text_for_stop)
    else:
        return home_site.text


def crt_rslt_structure() -> list:
    result_structure = list()
    main_row = ['region', 'district', 'city_number', 'city_name', 'registered', 'envelope', 'valid']
    for item in main_row:
        tmp_dict = dict()
        tmp_dict.setdefault(item, '')
        result_structure.append(tmp_dict)
    return result_structure


def htmltable_to_list(soup, class_sel='', tag_sel='td', href_sel=False) -> list:
    result_list = list()
    for table in soup:
        tmp_soup = table.find_all(tag_sel, attrs={'class': class_sel})
        for row in tmp_soup:
            if href_sel:
                result_list.append(row.a['href'])
            else:
                result_list.append(row.text.replace(u'\xa0', u''))
    return result_list


def script_stop(stop_text: str):
    print(stop_text)
    print('QUITTING..')
    exit()


if __name__ == '__main__':
    input_list = ['SYS', 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103']
    input_list += ['vysledky_prostejov.csv']
    # input_list = sys.argv()
    if input_check(input_list):
        req_site = request_site(input_list[1])
        election_result = crt_rslt_structure()
        running_check, attempts = False, 1
        cities_number, cities_names, cities_links = list(), list(), list()
        soup_site = BeautifulSoup(req_site, 'html.parser')
        selected_location = soup_site.find_all('h3')[:2]
        kraj = selected_location[0].string.split()[1] + ' kraj'
        okres = selected_location[1].string.split()[1]
        while not running_check:
            soup_table = soup_site.find_all('table', attrs={'class': 'table'})
            cities_number = htmltable_to_list(soup_table, class_sel='cislo')
            cities_names = htmltable_to_list(soup_table, class_sel='overflow_name')
            cities_links = htmltable_to_list(soup_table, class_sel='cislo', href_sel=True)
            if len(cities_number) == len(cities_links) and len(cities_number) == len(cities_names):
                print(f'City links and numbers ({len(cities_links)}) got properly on {attempts}. attempt.')
                running_check = True
            elif attempts < 6:
                print(f'Diference between number of city lists on {attempts} attempts.')
                print('Trying to get the data once more...')
                attempts += 1
            else:
                script_stop(f'Not able to get lists of city links and numbers after {attempts} attempts.')
        election_result = {'hlavicka': ['region', 'district', 'city_number', 'city_name']}
        election_result['hlavicka'] += ['registered', 'envelope', 'valid']
        for j in range(len(cities_links)):
            radek = {f'radek{j}': [kraj, okres, cities_number[j], cities_names[j]]}
            election_result.update(radek)
        strany_list = list()
        for i, odkaz in enumerate(cities_links):
            odkaz = 'https://volby.cz/pls/ps2017nss/' + odkaz
            req_cities = request_site(odkaz)
            soup_cities = BeautifulSoup(req_cities, 'html.parser')
            hlasy_list = list()
            soup_2uroven = soup_cities.find_all('table', attrs={'class': 'table', 'id': 'ps311_t1'})
            ReqHeaders = ['sa2', 'sa5', 'sa6']
            for row in soup_2uroven:
                for ReqHeader in ReqHeaders:
                    try:
                        scrapped_text = row.find('td', attrs={'class': 'cislo', 'headers': ReqHeader})
                        scrapped_text = scrapped_text.text
                    except AttributeError:
                        print('Attribute error, jedu dal...')
                        continue
                    else:
                        scrapped_text = scrapped_text.replace(u'\xa0', u'')
                    election_result[f'radek{i}'].append(scrapped_text)
            strany_tab = soup_cities.find_all('div', attrs={'class': 't2_470'})
            for x, strana in enumerate(strany_tab):
                if i == 0:
                    strany_list = htmltable_to_list(strany_tab, class_sel='overflow_name')
                    election_result['hlavicka'] += strany_list
                vote_header = f't{x+1}sa2 t{x+1}sb3'
                votes_soup = strana.find_all('td', attrs={'class': 'cislo', 'headers': vote_header})
                for polozka in votes_soup:
                    hlasy_list.append(polozka.text.replace(u'\xa0', u''))
            if len(strany_list) == len(hlasy_list):
                election_result[f'radek{i}'] += hlasy_list
            else:
                script_stop('Number of parties does not equal to votes.')
        print('Web Scraping successfully finished!')
        with open(input_list[2], mode='w', newline='') as csv_file:
            voting_writer = csv.writer(csv_file, delimiter=',')
            voting_writer.writerow(election_result['hlavicka'])
            for j in range(len(cities_links)):
                voting_writer.writerow(election_result[f'radek{j}'])
