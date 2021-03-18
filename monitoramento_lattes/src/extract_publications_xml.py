import lxml
from bs4 import BeautifulSoup as bs 
import pandas as pd

from utils import unzip_files


def extract_scientific_papers(bs_content):
    list_of_publications = []
    result = bs_content.find_all('artigo-publicado')
    for paper in result:
        title = paper.find('dados-basicos-do-artigo').get('titulo-do-artigo')
        title_en = paper.find('dados-basicos-do-artigo').get('titulo-do-artigo-ingles')
        year = paper.find('dados-basicos-do-artigo').get('ano-do-artigo')
        doi = paper.find('dados-basicos-do-artigo').get('doi')
        journal = paper.find('detalhamento-do-artigo').get('titulo-do-periodico-ou-revista')

        list_of_publications.append({
            'title': title_en if len(title_en) > 1 else title,
            'year': year, 
            'journal': journal,
            'doi': doi})

    return(list_of_publications)


def extract_books(bs_content):
    list_of_books = []
    result = bs_content.find_all('capitulo-de-livro-publicado')
    for book in result:
        title = book.find('dados-basicos-do-capitulo').get('titulo-do-capitulo-do-livro')
        title_en = book.find('dados-basicos-do-capitulo').get('titulo-do-capitulo-do-livro-ingles')
        year = book.find('dados-basicos-do-capitulo').get('ano')

        list_of_books.append({
            'title': title_en if len(title_en) > 1 else title,
            'year': year })

    return(list_of_books)


def extract_conference_presentations(bs_content):
    list_of_conference_presentations = []

    result = bs_content.find_all('trabalho-em-eventos')
    for presentation in result:
        title = presentation.find('dados-basicos-do-trabalho').get('titulo-do-trabalho')
        title_en = presentation.find('dados-basicos-do-trabalho').get('titulo-do-trabalho-ingles')
        year = presentation.find('dados-basicos-do-trabalho').get('ano-do-trabalho')
        conference_title = presentation.find('detalhamento-do-trabalho').get('nome-do-evento')

        list_of_conference_presentations.append({
            'title': title_en if len(title_en) > 1 else title,
            'year': year,
            'conference_title': conference_title})

    return(list_of_conference_presentations)


if __name__ == '__main__':

    cv_path = '../data/xmls/2710436780723053.xml'

    content = []
    with open(cv_path, 'r', encoding='ISO-8859-1') as file:
        content = file.readlines()
        content = ''.join(content)
        bs_content = bs(content, features='lxml')


    # Get scientific papers
    scientific_papers = extract_scientific_papers(bs_content)
    scientific_papers = pd.DataFrame(data=scientific_papers)

    # Get books and chapters
    books = extract_books(bs_content)
    books = pd.DataFrame(data=books)

    # Get conference presentation
    conferences = extract_conference_presentations(bs_content)
    conferences = pd.DataFrame(data=conferences)



