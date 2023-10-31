# Searches Entrez Databases
# db = nucleotide || searches GenBank
# db = pubmed || searches PubMed

# installs Biopython and imports the Entrez database search
!pip install Bio
from Bio import Entrez

# Gather user input for search restrictions (Genus, Start date, End date)
genus = input("Genus: ")
date1 = input("Start date: ")
date2 = input("End date: ")

# NOTE: REPLACE YOUR EMAIL HERE! ENTREZ USES THIS TO NOTIFY YOU IF SOMETHING GOES WRONG!
Entrez.email = "your_name@your_mail_server.com"

# Searches Entrez with specified restrictions (Genus, Start Date, End date)
handle = Entrez.esearch(db="nucleotide", term = '{0}[Organism] AND {1}:{2}[Publication Date]'.format(genus, date1, date2)) # searches database
record = Entrez.read(handle) # reads data and converts into a viewable form
ids = '\n'.join(sorted(record["IdList"])) # shows the ID's of matching entries

print(ids)
