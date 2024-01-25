#!/usr/bin/python3
"""
This script contains the function definition for print_stat
"""
import sys
import signal


# Initialize variables
codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_codes = {str(code): 0 for code in codes}
total_size = 0
line_count = 0


def print_stats():
    """
        print_stats function
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """
        signal_handler function
    """
    print_stats()
    sys.exit(0)


# Set the signal handler
signal.signal(signal.SIGINT, signal_handler)


try:
    for line in sys.stdin:
        try:
            parts = line.split()
            size = int(parts[-1])
            status_code = parts[-2]

            if status_code in status_codes:
                status_codes[status_code] += 1
                total_size += size

            line_count += 1
            if line_count % 10 == 0:
                print_stats()

        except Exception:
            continue

except KeyboardInterrupt:
    pass

finally:
    print_stats()
