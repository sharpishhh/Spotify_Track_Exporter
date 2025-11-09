def my_generator():
    yield "Hello world!!(first line)"
    yield "This yields the second line"

def double(val):
    return val * 2
a = [1, 2, 6, 8]
res = list(map(double, a))

def get_batch():
    lst = [num for num in range(101)]
    for i in range(0, len(lst) - 1, 6):
        yield lst[i:i+6]

def display_batches():
    batch = get_batch()
    print(batch)

if __name__ == "__main__":
    # print(res)
    # g = my_generator()
    # print(type(g))  
    # print(next(g)) 
    # print(next(g))
    print(display_batches())