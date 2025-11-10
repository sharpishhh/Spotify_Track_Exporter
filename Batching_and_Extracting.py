import time
import csv
from itertools import zip_longest

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
    for i in range(0,length,10):
        yield parsed_ids[i:i+10]

# Convert batches to CSV file.
# Use to create CSV file upon completion of parsing and batching.
def consume_batches():
    pass

def run_exporter():
    full_links = read_links("Full_Links.txt")
    cleaned = clean_links(full_links)
    parsed_ids = extract_ids(cleaned)
    batch = get_batches(parsed_ids)
    converted_tracks = consume_batches(batch)
    return converted_tracks
        

if __name__ == "__main__":
    # print(extract_ids())
    # print(get_batches())
    # print(grouper(iterable=[1,2,3,4,5,5,6,7,8,8,9,9,9,6,5,4,3],num=5, incomplete='fill', fillvalue=None))
    # print(get_batches([1,2,3,4,5,5,6,7,8,8,9]))
    print(consume_batches())