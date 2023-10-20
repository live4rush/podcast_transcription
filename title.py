import csv
import difflib


def get_title_author(csv_file, filename):
    # Lists to store titles and authors from the CSV
    titles = []
    authors = []

    # Read the CSV and populate the lists
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            titles.append(row['Title'])
            authors.append(row['Author'])

    # Find the closest match to the filename in the titles list
    closest_matches = difflib.get_close_matches(filename, titles, n=1)

    # If a match is found, return the title and corresponding author
    if closest_matches:
        closest_title = closest_matches[0]
        index = titles.index(closest_title)
        return closest_title, authors[index]
    else:
        return None, None
