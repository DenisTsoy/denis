import os
import sys

if __name__ == "__main__":
    root_dir = sys.argv[1]
file_statistics = {}
for root, dirs, files in os.walk(root_dir):
    for file in files:
        corrent_file = os.path.join(root, file)
        size = os.stat(corrent_file).st_size
        key = 10 ** len(str(size))
        if key in file_statistics:
            file_statistics[key] += 1
        else:
            file_statistics[key] = 1
keys = list(file_statistics)
keys.sort()
for key in keys:
        print(f'{key}: {file_statistics[key]}')
