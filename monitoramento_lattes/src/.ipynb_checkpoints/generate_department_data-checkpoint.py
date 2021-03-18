import os
import re
import pandas as pd

from bs4 import BeautifulSoup as bs 

from extract_publications_xml import (extract_books,
        extract_scientific_papers,
        extract_conference_presentations)


def combine_department_production():

    books_list, conferences_list, papers_list = [], [], []
    cvs = [file for file in os.listdir('../data/xmls')]
    cv_path = '../data/xmls/'

    for cv in cvs:
        with open(os.path.join(cv_path, cv), 'r', encoding='ISO-8859-1') as file:
            content = file.readlines()
            content = ''.join(content)
            bs_content = bs(content, features='lxml')

            books = extract_books(bs_content)
            df_books = pd.DataFrame(data=books)

            conferences = extract_conference_presentations(bs_content)
            df_conferences = pd.DataFrame(data=conferences)

            scientific_papers = extract_scientific_papers(bs_content)
            df_papers = pd.DataFrame(data=scientific_papers)

            df_books['prof_id'] = re.sub('\\D', '', cv)
            df_conferences['prof_id'] = re.sub('\\D', '', cv)
            df_papers['prof_id'] = re.sub('\\D', '', cv)

            books_list.append(df_books)
            conferences_list.append(df_conferences)
            papers_list.append(df_papers)

    return pd.concat(books_list), pd.concat(conferences_list), pd.concat(papers_list)


if __name__ == '__main__':
    df_books, df_conferences, df_papers = combine_department_production()
    print(df_books.shape, df_conferences.shape, df_papers.shape)
