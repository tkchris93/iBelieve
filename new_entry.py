#!/home/tanner/anaconda/bin/python

import os

os.system("clear")

summary = raw_input("Summary: ")
author = raw_input("Author: ")
source = raw_input("Source: ")
tags = raw_input("Tags: ")

os.system("echo " + summary + " >> data.txt")
os.system("echo " + author + " >> data.txt")
os.system("echo " + source + " >> data.txt")
os.system("echo " + tags + " >> data.txt")
os.system("cat >> data.txt")
os.system('echo "\nend\n" >> data.txt')
