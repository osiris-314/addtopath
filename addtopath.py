#!/usr/bin/env python3
import subprocess
import os
from colorama import Fore
from pathlib import Path
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Move a file to a new directory and add it to the PATH.")
parser.add_argument('-f', '-file', type=str, required=True, help='The file name to be moved')
parser.add_argument('-c', '-command', type=str, required=True, help='The new directory name to move the file to')

args = parser.parse_args()
file_name = args.f
new_directory = args.c

# Resolve paths
file_name_path = Path(file_name)
new_directory_path = Path(new_directory)

if file_name_path.is_file():
    if not new_directory_path.is_file():
        try:
            subprocess.run(f'chmod +x {file_name}', shell=True, check=True)
            subprocess.run(f'sudo mv {file_name} /usr/local/bin/{new_directory}', shell=True, check=True)
            print(Fore.LIGHTGREEN_EX + 'Successfully Added ' + Fore.LIGHTBLUE_EX + str(new_directory) + Fore.LIGHTGREEN_EX + ' To The ' + Fore.LIGHTYELLOW_EX + 'PATH' + Fore.WHITE)
        except subprocess.CalledProcessError as e:
            print(Fore.RED + 'Error: ' + Fore.LIGHTRED_EX + str(e) + Fore.WHITE)
    else:
        print(Fore.RED + 'Directory ' + Fore.LIGHTBLUE_EX + str(new_directory) + Fore.RED + ' Already Exists' + Fore.WHITE)
else:
    print(Fore.RED + 'File ' + Fore.LIGHTBLUE_EX + str(file_name) + Fore.RED + ' Does Not Exist' + Fore.WHITE)
