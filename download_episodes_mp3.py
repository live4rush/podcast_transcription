import csv
import requests
import os


def sanitize_filename(filename):
    """Sanitize the filename by removing invalid characters."""
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename


# File path
file_path = "episodes.csv"

# Check if the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file '{file_path}' does not exist.")

# Read the CSV data from the file
with open(file_path, 'r') as file:
    reader = list(csv.DictReader(file))

# Create the PodcastEpisodes directory if it doesn't exist
directory = "PodcastEpisodes"
if not os.path.exists(directory):
    os.makedirs(directory)

# Download the MP3 files
total_episodes = len(reader)
for index, row in enumerate(reader, start=1):
    mp3_url = row['MP3 URL']
    sanitized_title = sanitize_filename(row['Title'])
    filename = os.path.join(directory, sanitized_title + ".mp3")

    # Check if the file already exists
    if os.path.exists(filename):
        print(
            f'File "{sanitized_title}.mp3" already exists. Skipping download.')
        continue

    print(f'Downloading "{row["Title"]}" - {index}/{total_episodes}')
    response = requests.get(mp3_url, stream=True)

    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=4096):
            file.write(chunk)

print("Downloaded all MP3 files to the PodcastEpisodes directory!")
