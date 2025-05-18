import hashlib

type_of_hash=str(input('Which type of hash you want to bruteforce: '))
file_path=str(input('Enter path to the file to bruteforce with: '))
hash_to_decrypt=str(input('Enter Hash Value to Bruteforce: '))

with open(file_path, 'r') as file: