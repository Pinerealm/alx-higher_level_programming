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
        if status_codes[key] > 0:
            print(f'{key}: {status_codes[key]}')


if __name__ == "__main__":
    line_count = 0
    file_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                print_stats(file_size, status_codes)
                break
            line = line.rstrip()
            line_count += 1
            file_size += int(line.split()[-1])
            code = int(line.split()[-2])

            if code in status_codes:
                status_codes[code] += 1
            if line_count % 10 == 0:
                print_stats(file_size, status_codes)

        except KeyboardInterrupt:
            print_stats(file_size, status_codes)
            raise
