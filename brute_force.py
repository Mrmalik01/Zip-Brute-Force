#!/usr/bin/python
# -*- coding: utf-8 -*-

##################################
# SCRIPT : Zip Brute Force
#    JOB : Brute Force Attack on Zip File
# Author : Khizar Malik
##################################

import socket, sys, os, re, random, optparse, time

## COLORS ###############
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
#########################
 
os.system("cls||clear")
error_message = lambda msg: rd+"\n["+yl+"!"+rd+"] Error: "+yl+msg+rd+ " !!!\n"+wi

try:import zipfile
except ImportError:
    print(error_message("[ zipfile ] module is missing"))
    print(error_message("[*] Please use: 'pip install zipfile' to install it"))
    sys.exit(1)
    
try:from tqdm import tqdm
except ImportError:
    print(error_message("[ tqdm ] module is missing"))
    print(error_message("[*] Please use: 'pip install tqdm' to install it"))
    sys.exit(1)

    
class ZipBruteForce:
    def __init__(self, target_file=None, wordlist=None, *args, **kwargs):
        try:
            self.total_words = len(list(open(wordlist, 'rb')))
        except:
            print(error_message("Wordlist file path is invalid"))
            sys.exit(1)
            
        self.target_file = target_file
        self.wordlist = wordlist
        
    def start(self):
        self.banner()
        zip_file = zipfile.ZipFile(self.target_file)
        with open(self.wordlist, "rb") as wordlist:
            for word in tqdm(wordlist, total=self.total_words, unit="word"):
                try:
                    zip_file.extractall(pwd=word.strip())
                except:
                    continue
                else:
                    print(yl+"====> Password "+gr+"Found: "+rd+word.decode().strip())
                    self.end()
        print("[!] Password not found, try other wordlist")
        self.end()
        
    def end(self):
        print(gr+"=========================THANK YOU===========================")
        sys.exit(1)
        
    def banner(self):
        print(gr+"""
=======================================================
[-----]          """+wi+"""   ZIP BRUTE FORCE  """+gr+"""           [-----]
=======================================================
[-----]          """+wi+"""   AUTHOR - KHIZAR MALIK  """+gr+"""     [-----]
[-----] """+wi+"""     EMAIL - khizarmalik.ai@gmail.com  """+gr+""" [-----]
=======================================================
[-----]          """+wi+"""       CONFIG  """+gr+"""                [-----]
=======================================================
[>] Target                :> """+wi+str(self.target_file)+gr+"""
[>] Wordlist              :> """+wi+str(self.wordlist)+gr+"""
[>] Total words           :> """+wi+str(self.total_words)+gr+"""
=======================================================
"""+wi+"""[~]"""+yl+""" Brute"""+rd+""" ForceAttack:"""+gr+""" Enabled"""+wi+""" [~]"""+gr+"""
=======================================================\n"""+wi)
        
        
parse = optparse.OptionParser(wi+"""

Usage: python ./brute_force.py [OPTIONS...]
-------------
OPTIONS:
       |
    |--------
    | -t <target zip file>          ::> Specify the path of the targeted ZIP file
    |--------
    | -w <wordlist Path>            ::> Specify the path of the Wordlist file
    |--------
       |
-------------    
Examples:
       |
    |--------
    | python brute_force.py -t secret_file.zip -w rockyou.txt
    |--------
    | python brute_force.py -t somepath/secret_file.zip -w somepath/rockyou.txt
    |--------
       |
""")    

def Main():
    parse.add_option("-t", "--target", '-T', "--TARGET", dest="tarfile", type="string", help="Specify the path of the targeted ZIP file")
    parse.add_option("-w", "--wordlist", '-W', "--WORDLIST", dest="wrdlst", type="string", help="Specify the path of the targeted ZIP file")
    (option, args) = parse.parse_args()
        
    if option.tarfile is None:
        print(error_message("Target file is not passed"))
        print(parse.usage)
        sys.exit(1)
    if option.wrdlst is None:
        print(error_message("Wordlist file is not passed"))
        print(parse.usage)
        sys.exit(1)
        
    attack = ZipBruteForce(option.tarfile, option.wrdlst)
    attack.start()
    
if __name__ =="__main__":
    Main()
    
        
        
# import zipfile
# from tqdm import tqdm

# wordlist = "rockyou.txt"
# zip_file = "secret_file.zip"

# # Initialize the Zip File object
# zip_file = zipfile.ZipFile(zip_file)

# # Count the number of words in this wordlist
# n_words = len(list(open(wordlist, "rb")))

# # Print the total number of passwords 
# print("Total passwords to test: ", n_words)

# with open(wordlist, "rb") as wordlist:
#     for word in tqdm(wordlist, total=n_words, unit="word"):
#         try:
#             zip_file.extractall(pwd=word.strip())
#         except:
#             continue
#         else:
#             print("[+] Password found: ",word.decode().strip())
#             exit(0)
# print("[!] Password not found, try other wordlist")

# import argparse
# import sys

# def getOption
