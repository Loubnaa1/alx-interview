#!/usr/bin/python3
"""log entries from stdin and calculate relevant metrics"""
import sys
import re

if __name__ == "__main__":
    log_entry_counter = 0
    cumulative_file_size = 0
    status_code_counts = {}
    log_entry_pattern = (
        r'^(\d{1,3}\.){3}\d{1,3}'
        r' - '
        r'\[\d{4}-\d{2}-\d{2}'
        r' \d{2}:\d{2}:\d{2}\.\d+\]'
        r' "GET /projects/260 HTTP/1\.1"'
        r' \d{3}'
        r' \d+$'
    )

    def display_metrics():
        """Displays the accumulated file sizes and status code frequency"""
        print('File size: {}'.format(cumulative_file_size))
        for code, count in sorted(status_code_counts.items()):
            print('{}: {}'.format(code, count))

    try:
        while True:
            log_entry = sys.stdin.readline()
            if not log_entry:
                break

            if re.match(log_entry_pattern, log_entry):
                log_entry_counter += 1
                file_size_match = re.search(r'\d+$', log_entry)
                status_code_match = re.search(r'(\d+)\s+\d+$', log_entry)

                if file_size_match:
                    file_size = file_size_match.group()
                    cumulative_file_size += int(file_size)

                if status_code_match:
                    status_code = status_code_match.group(1)
                    if status_code in status_code_counts:
                        status_code_counts[status_code] += 1
                    else:
                        status_code_counts[status_code] = 1

                if log_entry_counter % 10 == 0:
                    display_metrics()
            else:
                continue

    except Exception as error:
        print("Error occurred:", error)
    finally:
        display_metrics()
