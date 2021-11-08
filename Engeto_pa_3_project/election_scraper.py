import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import sys
# import unicodedata


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


def htmltable_to_list(soup, class_sel='', tag_sel='td', id_sel='', href_sel=False) -> list:
    result_list = list()
    for row in soup.findAll(tag_sel, attrs={'class': class_sel,'id': id_sel}):
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
    input_list = ['SYS', 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103', 'vysledky_prostejov.csv']
    # input_list = sys.argv()
    if input_check(input_list):
        req_site = request_site(input_list[1])
        election_result = crt_rslt_structure()
        running_check, attempts = False, 1
        soup_site = BeautifulSoup(req_site, 'html.parser')
        # selected_location = soup_site.find_all('h3')[:2]
        # election_result[0].update({"region": selected_location[0].string.split()[1] + ' kraj'})
        # election_result[1].update({"district": selected_location[1].string.split()[1]})
        while not running_check:
            soup_table = soup_site.find('table', attrs={'class': 'table'})
            cities_number = htmltable_to_list(soup_table, class_sel='cislo')
            # election_result[2].update({"city_number": cities_number})
            # cities_names = htmltable_to_list(soup_table, class_sel='overflow_name')
            # election_result[3].update({"city_name": cities_names})
            cities_links = htmltable_to_list(soup_table, class_sel='cislo', href_sel=True)
            # election_result[4].update({"city_link": cities_links})
            if len(cities_number) == len(cities_links):
                print(f'City links and numbers got properly on {attempts}. attempt.')
                running_check = True
            elif attempts < 6:
                print(f'Diference between number of city lists on {attempts} attempts.')
                print('Trying to get the data once more...')
                attempts += 1
            else:
                script_stop(f'Not able to get lists of city links and numbers after {attempts} attempts.')

        election_result = [['region'], ['district'], ['city_name'], ['city_number']]
        election_result += [['registered'], ['envelope'], ['valid']]

        # registered_list, envelope_list, valid_list = list(), list(), list()
        strany, strany_list = list(), list()
        hlasy, hlasy_list = list(), list()
        for i, odkaz in enumerate(cities_links):
            odkaz = 'https://volby.cz/pls/ps2017nss/' + odkaz
            req_cities = request_site(odkaz)
            soup_cities = BeautifulSoup(req_cities, 'html.parser')
            election_result[3].append(cities_number[i])
            for a in range(3):
                scrapped_text = soup_cities.findAll('h3')[a].string
                scrapped_text = scrapped_text.split(':')[1].strip()
                election_result[a].append(scrapped_text)


            soup_2uroven = soup_cities.find_all('table', attrs={'class': 'table'})

            ReqHeaders = {'result_pos': [4, 5, 6], 'header': ['sa2', 'sa5', 'sa6']}
            for row in soup_2uroven:
                for b, result_position in enumerate(ReqHeaders['result_pos']):
                    try:
                        scrapped_text = row.find('td', attrs={'class': 'cislo', 'headers': ReqHeaders['header'][b]}).text

                    except AttributeError:
                        continue
                    else:
                        scrapped_text = scrapped_text.replace(u'\xa0', u'')
                    print(scrapped_text)
                    election_result[ReqHeaders['result_pos'][b]].append(scrapped_text)
            print(election_result)
            script_stop('debug')

            soup_2table = soup_2uroven.find('table', attrs={'class': 'table'})
            hlasy = soup_2table.find('td', attrs={'class': 'cislo', 'headers': 't1sa2 t1sb3'})
            hlasy_list.append(hlasy.text.replace(u'\xa0', u''))
            if i < 1:
                for z in range(len(soup_2uroven)):
                    strany = htmltable_to_list(soup_2uroven[z], class_sel='overflow_name')
                    strany_list += strany
                print(len(strany_list))
            soup_table = soup_cities.find('table', attrs={'class': 'table'})
            cities_registered = soup_table.find('td', attrs={'class': 'cislo', 'headers': 'sa2'})
            cities_envelope = soup_table.find('td', attrs={'class': 'cislo', 'headers': 'sa3'})
            cities_valid = soup_table.find('td', attrs={'class': 'cislo', 'headers': 'sa6'})
            parties_list = soup_table.find('td', attrs={'class': 'cislo', 'headers': 'sa6'})
            try:
                registered_list.append(cities_registered.text.replace(u'\xa0', u''))
                envelope_list.append(cities_envelope.text.replace(u'\xa0', u''))
                valid_list.append(cities_valid.text.replace(u'\xa0', u''))
            except AttributeError:
                print(f'Mesto {election_result[3]["city_name"][i]} ma problem!')
        print(hlasy_list)
        election_result[5].update({"registered": registered_list})
        election_result[6].update({"envelope": envelope_list})
        election_result[7].update({"valid": valid_list})
        print(election_result, '\n')


