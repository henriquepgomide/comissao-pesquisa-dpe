# python3
import re
from bs4 import BeautifulSoup
import requests


def find_lattes_url(regex):
    """
    Find lattes URL inside the department's page
    Parameters:
    regex(str): string with regex to match files

    """

    URL = "http://www.dpe.ufv.br/?page_id=1072"
    html = requests.get(URL)
    soup = BeautifulSoup(html.text, 'lxml')

    list_of_result = []
    for tag in soup.find_all('a', attrs={'href': re.compile(regex)}):
        href_str = tag.get('href')
        list_of_result.append(href_str)

    return list_of_result


if __name__ == '__main__':
    with open('../data/list_of_ids.txt', 'w') as myfile:
        part_a = find_lattes_url('lattes')
        part_b = find_lattes_url('cnpq')
        urls = part_a + part_b
        myfile.write('\n'.join(url for url in urls))

