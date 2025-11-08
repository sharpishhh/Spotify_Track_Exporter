import time
from itertools import zip_longest

with open("Full_Links.txt", "r") as file:
    full_links = file.readlines()

def extract_ids():
    result = []
    for track in full_links:
        result.append(track.removeprefix("https://open.spotify.com/track/").rstrip())
    return result

def get_batches():
    pass




    
def grouper(iterable, num, incomplete = 'fill', fillvalue=None):
    '''Collect data into non-overlapping fixed-length batches'''
    iterators = [iter(iterable)] * num
    match incomplete:
        case 'fill':
            return zip_longest(*iterators, fillvalue=fillvalue)
        case 'strict':
            return zip(*iterators, strict=True)
        case 'ignore':
            return zip(*iterators)
        case _:
            raise ValueError('Expected fill, strict, or ignore')
    

        

if __name__ == "__main__":
    # print(extract_ids())
    # print(get_batches())
    print(grouper(iterable=[1,2,3,4,5,5,6,7,8,8,9,9,9,6,5,4,3],num=5, incomplete='fill', fillvalue=None))