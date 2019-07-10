#!/usr/bin/env python

import os
import time
import subprocess

def main():
    os.system("cd ../ && ls | grep HPdisk001 > scripts/files.txt")    
    time.sleep(1)
    with open("../scripts/files.txt","r") as my_file:           
        for x in my_file:
            print(x)
            i = f"cd ../ && ls | grep {x}"
            cmd = f"cd ../ && cat {x} | strings > scripts/{x}\n"
            f = open("../scripts/runList.txt","a")
            print(cmd)
            f.write(cmd) 
            f.close()
            time.sleep(2)
            
main()
