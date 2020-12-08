#!/usr/bin/env python

# move_files_by_date.py
# Created: 8th Dec 2020

__author__ = 'Radek Warowny'
__version__ = '1.0'

import shutil
import time
import os


def main():
    os.system('clear')
    print("\n\t\tMOVE FILES BY DATE\n")
    src = str(input("\tFULL PATH OF SOURCE: "))
    dst = str(input("\tFULL PATH OF DESTINATION: "))
    days = int(input("\tNUMBER OF DAYS: "))

    if days < 0:
        days = 0

    now = time.time()  # current time

    if not os.path.exists(dst):  # create dst folder if not found
        os.mkdir(dst)
    try:
        for file in os.listdir(src):  # look for files
            if os.stat(file).st_mtime < now - days * 86400:  # find files older than given date
                if os.path.isfile(file):  # if file exists,
                    shutil.move(file)     # move file
                    print("\n\tFILES MOVED ")
    except FileNotFoundError as e:
        print(e)


if __name__ == '__main__':
    main()


