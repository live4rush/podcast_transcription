import requests
import csv
import xml.etree.ElementTree as ET

url = "https://marketingsecrets.libsyn.com/rss"
response = requests.get(url)

if response.status_code != 200:
    raise Exception(f"Error fetching XML from {url}")

root = ET.fromstring(response.content)

# Extract items from the XML
items = root.find('channel').findall('item')

# Prepare CSV file for writing
with open('episodes.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Title', 'Author', 'MP3 URL'])  # Write the header

    for item in items:
        title = item.find('title').text

        # Check if title ends with "..." or "...!" and trim it
        if title.endswith("…"):
            title = title[:-1]
        elif title.endswith("..."):
            title = title[:-3]
        elif title.endswith("...!"):
            title = title[:-4]

        # Extracting the 'itunes:author' requires using the namespace
        author = item.find(
            '{http://www.itunes.com/dtds/podcast-1.0.dtd}author').text

        mp3_url = item.find('enclosure').attrib['url']

        # Write data to CSV
        writer.writerow([title, author, mp3_url])
