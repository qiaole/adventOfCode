import re


def read_data (file, path = 'inputs/'):
    with open(path+file, 'r', encoding="utf-8") as f:
        raw_lines = f.readlines()
    return  [x[:-1] for x in raw_lines]