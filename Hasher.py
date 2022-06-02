#hash files in md5 with multiple threads
from concurrent.futures import thread
import threading
import time
import os
import sys
import hashlib


def hash_file(filename):
    with open(filename, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def find_files(location):
    for root, dirs, files in os.walk(location):
        for file in files:
            yield os.path.join(root, file)
                
def write_to_file(filename, hashes):
    with open(filename, 'w') as f:
        for h in hashes:
            f.write(h[0] + ' ' + h[1] + '\n')

def main():
    if os.path.isfile(location):
        hashes = [hash_file(location)]
    elif os.path.isdir(location):
        hashes = list(hash_dir(location))
    else:
        print("Invalid location")
        sys.exit(1)
    write_to_file(output, hashes)

def thread_function(location, output, threads):
    if os.path.isfile(location):
        hashes = [hash_file(location)]
    else:
        print("Invalid location")
        sys.exit(1)
    write_to_file(output, hashes)


location = input("Enter the location of the file or directory: ")
threads = int(input("Enter the number of threads: "))
output = input("Enter the output file name: ")

for i in range(threads):
    threading.Thread(target=thread_function, args=(location, output, threads)).start()
for thread in threading.enumerate():
    if thread is not threading.currentThread():
        thread.join()

