#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics."""

import sys


def print_stats(total_file_size, status_counts):
    """Print accumulated statistics."""
    print("File size: {:d}".format(total_file_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    total_file_size = 0
    status_counts = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) >= 2:
                try:
                    # File size is always the last element
                    total_file_size += int(parts[-1])
                except ValueError:
                    pass

                try:
                    # Status code is the second to last element
                    status = parts[-2]
                    if status in status_counts:
                        status_counts[status] += 1
                except IndexError:
                    pass

            if line_count % 10 == 0:
                print_stats(total_file_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_file_size, status_counts)
        raise

    print_stats(total_file_size, status_counts)
