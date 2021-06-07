#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser(description="Generate a secure, memorable password using the XKCD method")
parser.add_argument("-w","--words", type=int, default=4, help = "include WORDS words in the password")
parser.add_argument("-c","--caps",type=int, default=0, help = "capitalize the first letter of CAPS random words")
parser.add_argument("-n","--numbers",type=int, default=0, help = "insert NUMBERS random numbers in the password")
parser.add_argument("-s","--symbols",type=int,default=0, help = "insert SYMBOLS random symbols in the password")
args = parser.parse_args()

f =  open('words_alpha.txt', "r")

allWords = f.read().split()
allSymbols = ['~','!','@','#','$','%','^','&','*','.',':',';']
allNumbers = ['0','1','2','3','4','5','6','7','8','9']
numSymbols = args.symbols
numNumbers = args.numbers
numCaps = args.caps

output = ""

import random

if args.words == 0:
    for x in range(numSymbols):
        output+= random.choice(allSymbols)
    for x in range(numNumbers):
        output += random.choice(allNumbers)
else:
    for x in range(args.words):
        if numSymbols >= 1:
            output += random.choice(allSymbols)
            numSymbols -= 1
        if numNumbers >= 1:
            output += random.choice(allNumbers)
            numNumbers -= 1
        if numCaps >= 1:
            output += random.choice(allWords).capitalize()
            numCaps -= 1
        else:
            output += random.choice(allWords)

print(output)


