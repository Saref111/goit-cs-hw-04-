from multiprocessing import Process, Queue
import os

def process_files(files_list, words, queue):
    for file in files_list:
        with open(file, 'r') as f:
            for line in f:
                for word in words:
                    if word in line:
                        queue.put(f'Event in process {os.getpid()}: {word} found in {file}')
                        break

if __name__ == '__main__':
    files = ['./files/file_1.txt', './files/file_2.txt', './files/file_3.txt', './files/file_4.txt', './files/file_5.txt', './files/file_6.txt']
    words = ['Lorem', 'Suspendisse', 'Cras', 'Maecenas', 'Proin', 'Duis']
    queue = Queue()
    processes = []
    
    for i in range(0, len(files)):
        process = Process(target=process_files, args=([files[i]], words, queue))
        process.start()
        processes.append(process)
    
    for process in processes:
        process.join()
    
    while not queue.empty():
        print(queue.get())

    