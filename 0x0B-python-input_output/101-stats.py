#!/usr/bin/python3
"""The 101-stats module"""
import sys


def print_stats(file_size, status_codes):
    """Prints the stats
    
    Args:
        file_size (int): The file size
        status_codes (dict): The status codes
    """
    print(f'File size: {file_size}')
    for key in sorted(status_codes):
        print(f'{key}: {status_codes[key]}')


if __name__ == "__main__":
    line_count = 0
    file_size = 0
    status_codes = {}

    while True:
        try:
            line = sys.stdin.readline().rstrip()
            line_count += 1
            file_size += int(line.split()[-1])
            code = line.split()[-2]

            status_codes[code] = status_codes.get(code, 0) + 1
            if line_count % 10 == 0:
                print_stats(file_size, status_codes)

        except KeyboardInterrupt:
            print_stats(file_size, status_codes)
            raise
