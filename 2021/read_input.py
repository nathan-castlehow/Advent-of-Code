import os


def read_input_as_string(path):
    with open(path) as f:
        lines = f.read().splitlines()
    return lines


def read_input_as_int(path):
    with open(path) as f:
        lines = [int(i) for i in f.read().splitlines()]
    return lines
