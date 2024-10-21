import os

# Select the directory
directory_path = '/Users/ARPAN'

contents = os.listdir(directory_path)

for item in contents:
    print(item)