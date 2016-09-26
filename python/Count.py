import string


def count(*args):
    result = [
    (c, sum([element == c for element in args]))
    for c in string.ascii_lowercase]
    return result

print(count("a", "b", "c"))
