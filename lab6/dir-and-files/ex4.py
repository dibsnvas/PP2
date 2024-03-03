import os

def count_lines(file_path):
    with open(file_path, 'r') as file:
        print("Number of lines:", len(file.readlines()))
