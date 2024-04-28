from multiprocessing import Process, Queue
import os
import logging  
from math import ceil

def process_files(files_list, words, queue):
    for file in files_list:
        try:
            with open(file, 'r') as f:
                for line in f:
                    for word in words:
                        if word in line:
                            queue.put(f'Event in process {os.getpid()}: {word} found in {file}')
                            break
        except FileNotFoundError as e:
            logging.error(f'File {file} not found')
        except PermissionError as e:
            logging.error(f'Permission denied for {file}')
        except Exception as e:
            logging.error(f'Unexpected error with file {file}: {str(e)}')

if __name__ == '__main__':
    files = ['./files/file_1.txt', './files/file_2.txt', './files/file_3.txt', './files/file_4.txt', './files/file_5.txt', './files/file_6.txt']
    words = ['Lorem', 'Suspendisse', 'Cras', 'Maecenas', 'Proin', 'Duis']
    queue = Queue()
    processes = []
    
    num_processes = os.cpu_count()
    files_per_process = ceil(len(files) / num_processes)

    for i in range(num_processes):
        start = i * files_per_process
        end = min((i + 1) * files_per_process, len(files))
        process_files_list = files[start:end]
        process = Process(target=process_files, args=(process_files_list, words, queue))
        process.start()
        processes.append(process)
    
    for process in processes:
        process.join()
    
    while not queue.empty():
        print(queue.get())

    