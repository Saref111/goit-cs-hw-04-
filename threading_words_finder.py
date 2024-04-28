from concurrent.futures import ThreadPoolExecutor
import logging
from collections import defaultdict

def process_files(file, words):
    results = {}
    try:
        with open(file, 'r') as f:
            for line in f:
                for word in words:
                    if word in line:
                        print(f'Event in thread: {word} found in {file}')
                        if word in results:
                            results[word] += 1
                        else:
                            results[word] = 1
                        break
    except FileNotFoundError as e:
        logging.error(f'File {file} not found')
    except PermissionError as e:
        logging.error(f'Permission denied for {file}')
    except Exception as e:
        logging.error(f'Unexpected error with file {file}: {str(e)}')
    return results

if __name__ == '__main__':
    files = ['./files/file_1.txt', './files/file_2.txt', './files/file_3.txt', './files/file_4.txt', './files/file_5.txt', './files/file_6.txt']
    words = ['Lorem', 'Suspendisse', 'Cras', 'Maecenas', 'Proin', 'Duis']
    results = {}

    with ThreadPoolExecutor() as executor:
            results = list(executor.map(process_files, files, [words]*len(files)))

    merged_results = defaultdict(int)
    for result in results:
        for key, value in result.items():
            merged_results[key] += value

    print('Done')
    print(merged_results)