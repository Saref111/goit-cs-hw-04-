from threading import Thread

def process_files(files_list, words):
    for file in files_list:
        with open(file, 'r') as f:
            for line in f:
                for word in words:
                    if word in line:
                        print(f'Event in thread: {word} found in {file}')
                        break

if __name__ == '__main__':
    files = ['./files/file_1.txt', './files/file_2.txt', './files/file_3.txt', './files/file_4.txt', './files/file_5.txt', './files/file_6.txt']
    words = ['Lorem', 'Suspendisse', 'Cras', 'Maecenas', 'Proin', 'Duis']
    thread1 = Thread(target=process_files, args=(files[:3], words))
    thread2 = Thread(target=process_files, args=(files[3:], words))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print('Done')