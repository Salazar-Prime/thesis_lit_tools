import chord
import bibtexparser

with open('export.bib') as bibtex_file:
	bib_database = bibtexparser.load(bibtex_file)

print(bib_database.strings)
