#hash files in md5 with multiple threads
from concurrent.futures import thread
import threading
import time
import os
import sys
import hashlib

location = input("Enter the location of the file or directory: ")
threads = int(input("Enter the number of threads: "))
output = input("Enter the output file name: ")

def hash_file(file_name):
    with open(file_name, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def hash_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_name = os.path.join(root, file)
            print(hash_file(file_name))

def hash_files(file_list):
    with open(output, 'w') as f:
        for file in file_list:
            f.write(hash_file(file) + '\n')

def main():
    if os.path.isfile(location):
        file_list = [location]
        hash_files(file_list)
    elif os.path.isdir(location):
        file_list = []
        for root, dirs, files in os.walk(location):
            for file in files:
                file_list.append(os.path.join(root, file))
        hash_files(file_list)
    else:
        print("Invalid location")

def thread_function(file_list):
    with open(output, 'w') as f:
        for file in file_list:
            f.write(hash_file(file) + '\n')
            print(file+" is done!")

file_list = []
for root, dirs, files in os.walk(location):
    for file in files:
        file_list.append(os.path.join(root, file))

for i in range(threads):
    thread_list = []
    for j in range(threads):
        thread_list.append(threading.Thread(target=thread_function, args=(file_list,)))
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()