import time
from itertools import zip_longest

with open("Full_Links.txt", "r") as file:
    full_links = file.readlines()

def clean_links(full_links):
    cleaned = []
    for link in full_links:
        cleaned.append(link.rstrip())
    return cleaned

def extract_ids(batch):
    parsed_ids = []
    for track in batch:
        parsed_ids.append(track.removeprefix("https://open.spotify.com/track/").rstrip())
    return parsed_ids

def get_batches(parsed_ids):
    length = len(parsed_ids)
    for i in range(0,length-1,10):
        yield parsed_ids[i:i+10]

def consume_batches():
    raw_batch = get_batches(full_links)
    for b in raw_batch:
        batch = extract_ids(raw_batch)
        return batch
        

if __name__ == "__main__":
    # print(extract_ids())
    # print(get_batches())
    # print(grouper(iterable=[1,2,3,4,5,5,6,7,8,8,9,9,9,6,5,4,3],num=5, incomplete='fill', fillvalue=None))
    # print(get_batches([1,2,3,4,5,5,6,7,8,8,9]))
    print(consume_batches())