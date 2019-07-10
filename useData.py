#!/usr/bin/env python

import os


def main():
    with open("../scripts/runList.txt") as my_file:
        for x in my_file:
            print(x)

main()
