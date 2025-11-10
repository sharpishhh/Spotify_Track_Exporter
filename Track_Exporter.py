import time
import csv
from itertools import zip_longest
import os

# Open file and read in links
def read_links(file_path):
    with open(file_path, "r") as file:
       return file.readlines()

# Clean extra space from end of the links
def clean_links(full_links):
    cleaned = []
    for link in full_links:
        cleaned.append(link.rstrip())
    return cleaned

# Using the cleaned links, parse and extract the track IDs
def extract_ids(cleaned):
    parsed_ids = []
    for link in cleaned:
        parsed_ids.append(link.removeprefix("https://open.spotify.com/track/").rstrip())
    return parsed_ids

# Generate batches of digestable size to give to Spotify
def get_batches(parsed_ids):
    length = len(parsed_ids)
    for i in range(0,length,50):
        yield parsed_ids[i:i+50]

# Convert batches to CSV file.
# Use to create CSV file upon completion of parsing and batching.
def consume_batches(batch):
    path = "track_list.csv"
    if os.path.isfile(path):
        with open("track_list.csv", "a", newline="") as f:
            writer = writer(f)
            writer.writerow(batch)
    else:
        with open("track_list.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(batch)
            print("CSV file created")

def run_exporter():
    full_links = read_links("Full_Links.txt")
    cleaned = clean_links(full_links)
    parsed_ids = extract_ids(cleaned)
    batch = get_batches(parsed_ids)
    converted_tracks = consume_batches(batch)
    return converted_tracks

if __name__ == "__main__":
    run_exporter()