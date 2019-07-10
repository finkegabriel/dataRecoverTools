#!/usr/bin/env python

import os
import time

def main():
    with open("../scripts/runList.txt") as my_file:
        for x in my_file:
            print(x)
            os.system(x)
            time.sleep(2)

main()
