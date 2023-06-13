#!/usr/bin/python3
# 101-stats.py

"""
========================================================================
Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file a_size up to that point.
    - a_count of read status codes up to that point.
========================================================================    
"""


def print_stats(a_size, a_status_codes):
    """Accumulated metrics.

    Args:
        a_size (int): accumulated read file size.
        a_status_codes (dict): accumulated a_count of status codes.
    """
    print("File a_size: {}".format(a_size))
    for key in sorted(a_status_codes):
        print("{}: {}".format(key, a_status_codes[key]))

if __name__ == "__main__":
    import sys

    a_size = 0
    a_status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    a_count = 0

    try:
        for line in sys.stdin:
            if a_count == 10:
                print_stats(a_size, a_status_codes)
                a_count = 1
            else:
                a_count += 1

            line = line.split()

            try:
                a_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if a_status_codes.get(line[-2], -1) == -1:
                        a_status_codes[line[-2]] = 1
                    else:
                        a_status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(a_size, a_status_codes)

    except KeyboardInterrupt:
        print_stats(a_size, a_status_codes)
        raise
