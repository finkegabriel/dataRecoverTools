#!/usr/bin/env python

import os
import time
import subprocess

def main():
    file = []

    os.system("cd ../ && ls | grep HPdisk001 > scripts/files.txt")    
    time.sleep(1)
    with open("../scripts/files.txt","r") as my_file:           
        for x in my_file:
            print(x)
            i = f"cd ../ && ls | grep {x}"
            cmd = f"cd ../ && cat {x} | strings > scripts/{x}"
            #cmdd = f"cd ../ && cat {x} |  >>  scripts/runList.txt "
            
            print(cmd)
            time.sleep(2)
            
main()
