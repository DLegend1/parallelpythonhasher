#hash all files in a directory in md5, using threading
from concurrent.futures import thread
import threading
import time
import os
import sys
import hashlib
from time import time


#code here

location = input("Enter the location of the file or directory: ")
threads = int(input("Enter the number of threads: "))
output = input("Enter the output file name: ")
with open(output, 'w') as f:
    f.write("")

start = time()

file_list = []
for root, dirs, files in os.walk(location):
    for file in files:
        file_list.append(os.path.join(root, file))

def hash_file(file_name):
    print(file_name + " is being hashed...")
    with open(file_name, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()
        
def hash_files(file_list):
    with open(output, 'a') as f:
        f.write(hash_file(file_list) + '\n')

if len(file_list) < threads:
    threads = len(file_list)

while len(file_list) > 0:
    thread_list = []
    for i in range(threads):
        if len(file_list) > 0:
            thread_list.append(threading.Thread(target=hash_files, args=(file_list.pop(),)))
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()

print(f'Time taken to run: {time() - start} seconds')