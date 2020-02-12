import bibtexparser
import argparse
import random


with open('test.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

for entry in bib_database.entries:
    year = entry['year']
    month = random.randint(1,12)
    day = random.randint(1,30)
    if year == '2020':
        month = 1
    date = year + '-{:02d}-{:02d}'.format(month, day)
    ID = entry['ID']
    file = open(date + '-' + ID + '.md','w')
    file.write('---\n')
    file.write('layout: post\n')
    file.write('title: ' + '\"' + entry['title'] +  '\"' + '\n')
    file.write('date: ' + date + '\n')
    file.write('image: \n')
    file.write('categories: research\n')
    file.write('author: Ian Abraham\n')

    authors = ''
    names =entry['author'].split(' and ')
    for i, name in enumerate(names):
        name = name.replace(' ','')
        last_name, first_name = name.split(',')
        name = first_name + ' ' + last_name
        if first_name == 'Ian':
            name = '<strong>' + name + '</strong>'
        authors += name
        if i+1 != len(names):
            authors += ', '

    file.write('authors: ' + '\"' + authors + '\"' + '\n')

    if 'booktitle' in entry.keys():
        venue = entry['booktitle']
    else:
        venue = entry['journal']

    file.write('venue: ' + '\"' + venue + '\"' + '\n')

    if 'project_page' in entry.keys():
        site = entry['project_page']
        file.write('project_page: ' + '\"' + site + '\"' + '\n')

    if 'pdf' in entry.keys():
        pdf = entry['pdf']
        file.write('arxiv: ' + pdf + '\n')

    file.write('---\n')

    if 'abstract' in entry.keys():
        abstract = entry['abstract']
        file.write(abstract)

    file.close()
