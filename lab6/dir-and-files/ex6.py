import os

def generate_26_files():
    for i in range(65, 91): 
        with open(f"{chr(i)}.txt", 'w') as file:
            file.write(chr(i))
